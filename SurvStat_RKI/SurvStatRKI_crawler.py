#!/usr/bin/env python3.7
#coding:utf-8

# ------------------------------------------------------------------------------ #
# @Author:        Matthias Linden
# @Email:         matthias.linden@ds.mpg.de
# @Created:       2020-09-25 
# @Last Modified: 2020-09-26 
# ------------------------------------------------------------------------------ #
# Tools to crawl  https://survstat.rki.de/Content/Query/Select.aspx
# the Website allows queries for Covid19 cases with:
#   - 1-year age stratification of cases
#   - sex
#   - by definition (lab,clinical,epi)
#   - federal / state / county
#   - weekly resolution
# 
# Inspiration taken from https://twitter.com/StefFun/status/1309223050718711814
# Thanks to @risklayer for publishing Landkreise meta-data
# ------------------------------------------------------------------------------ #


import datetime
import time
import pickle
import os

#import xarray as xr

from zeep import Client
from lxml import etree

from Landkreise import Landkreise


# XML is the devil. This is what the components of the request should look like
""" -- FilterCollection --
<xs:complexType name="FilterCollection">
    <xs:annotation>
        <xs:appinfo>
            <IsDictionary xmlns="http://schemas.microsoft.com/2003/10/Serialization/">true</IsDictionary>
        </xs:appinfo>
    </xs:annotation>
    <xs:sequence>
        <xs:element minOccurs="0" maxOccurs="unbounded" name="KeyValueOfFilterCollectionKeyFilterMemberCollectionb2rWaiIW">
            <xs:complexType>
                <xs:sequence>
                    <xs:element name="Key" nillable="true" type="tns:FilterCollectionKey"/>
                    <xs:element name="Value" nillable="true" type="tns:FilterMemberCollection"/>
                </xs:sequence>
            </xs:complexType>
        </xs:element>
    </xs:sequence>
</xs:complexType>
<xs:element name="FilterCollection" nillable="true" type="tns:FilterCollection"/>
"""
    
""" -- KEY --
<xs:complexType name="FilterCollectionKey">
    <xs:sequence>
        <xs:element minOccurs="0" name="DimensionId" nillable="true" type="xs:string"/>
        <xs:element minOccurs="0" name="HierarchyId" nillable="true" type="xs:string"/>
    </xs:sequence>
</xs:complexType>
<xs:element name="FilterCollectionKey" nillable="true" type="tns:FilterCollectionKey"/>
"""

# Case Definitions
"""
<option value="[Falldefinition].[ID].&amp;[-1]">- not obtainable -</option>
<option value="[Falldefinition].[ID].&amp;[1]">clinical criteria met</option>
<option value="[Falldefinition].[ID].&amp;[2]">clinical and epidemiological criteria met</option>
<option value="[Falldefinition].[ID].&amp;[3]">clinical and laboratory criteria met</option>
<option value="[Falldefinition].[ID].&amp;[4]">laboratory criteria met, clinical criteria not met</option>
<option value="[Falldefinition].[ID].&amp;[5]">laboratory criteria met, clinical criteria undetermined</option>
"""

"""
male:1,female:2,divers:3,unknown:999999
<option value="[Geschlecht].[SortGruppe]" optiongroup="Person" title="Sex">Sex</option>
<option value="[AlterPerson80].[AgeGroupName8]" optiongroup="Person" title="from 0, 1, 2, 3, 4, 5, …., 79, 80 years">Age stratification: 1 year intervals</option>
<option value="[AlterPerson80].[AgeGroupName3]" optiongroup="Person" title="from 0, 15, 20, 25, 30, 40, 50, 60, 70, 80 years">Age stratification: children coarse</option>
<option value="[AlterPerson80].[AgeGroupName1]" optiongroup="Person" title="from 0, 1, 2, 3, 4, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80 years">Age stratification: children fine</option>
<option value="[AlterPerson80].[AgeGroupName2]" optiongroup="Person" title="from 0, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80 years">Age stratification: children medium</option>
<option value="[AlterPerson80].[AgeGroupName6]" optiongroup="Person" title="from 0, 1, 5, 10, 15, 20, … , 75, 80 years">Age stratification: 5 year intervals</option>
"""

# Test out single request
def Request(client):
    lastUpdated = client.service.GetCubeInfo({"Cube":"SurvStat"})
    print(lastUpdated)
        
    print("Namespaces",client.namespaces)
    factory = client.type_factory('ns2')
    
    f1 = { "Key":{"HierarchyId":"[PathogenOut].[KategorieNz].[Krankheit DE]","DimensionId":"[PathogenOut].[KategorieNz]"},"Value":factory.FilterMemberCollection( ["[PathogenOut].[KategorieNz].[Krankheit DE].&[COVID-19]"] ) }
    f2 = { "Key":{"HierarchyId":"[Falldefinition].[ID]","DimensionId":"[Falldefinition].[ID]"},"Value":factory.FilterMemberCollection(["[Falldefinition].[ID].&[3]"]) }
    f3 = { "Key":{"HierarchyId":"[DeutschlandNodes].[Kreise71Web].[FedStateKey71]","DimensionId":"[DeutschlandNodes].[Kreise71Web]"},"Value":factory.FilterMemberCollection( ["[DeutschlandNodes].[Kreise71Web].[FedStateKey71].&[03].&[DE92].&[03241]"] ) }
    f4 = { "Key":{"HierarchyId":"[Geschlecht].[SortGruppe]","DimensionId":"[Geschlecht]"},"Value":factory.FilterMemberCollection( ["[Geschlecht].[SortGruppe].&[1]"] ) }
    f5 = { "Key":{"HierarchyId":"[ReportingDate].[WeekYear]","DimensionId":"[ReportingDate]"},"Value":factory.FilterMemberCollection( ["[ReportingDate].[WeekYear].&[2020]"] ) }
    filters = factory.FilterCollection([f1,f2,f3,f4,f5])
    
    request = {}
    request["Cube"] = "SurvStat"
#    request["ColumnHierarchy"] = "[AlterPerson80].[AgeGroupName8]"
    request["ColumnHierarchy"] = "[AlterPerson80].[AgeGroupName6]"

    request["RowHierarchy"] = "[ReportingDate].[YearWeek].[YearWeek]"
    request["IncludeNullColumns"] = False
    request["InculdeTotalColumn"] = False
    request["IncludeNullRows"] = True
    request["InculdeTotalRow"] = False
    
    request["HierarchyFilters"] = filters
    
    node = client.create_message(client.service,'GetOlapData',request) 
    
    # Let's see if the query looks correct.
    print( etree.tostring(node,pretty_print=True).decode() )
    
    response = client.service.GetOlapData(request)
    return response

# Now the serious stuff:

class Crawler(object):
    def __init__(self):
        self._InitFilters()
        self.lks = Landkreise()
        
        self.client = Client("https://tools.rki.de/SurvStat/SurvStatWebService.svc?singleWsdl")
        self.client_factory = self.client.type_factory('ns2')
        
        self.debug = False
        
    def _InitFilters(self):
        
        self.filters = {}
        self.filter_values = {}
        
         # AgeGrouping
        age_filters = {}
        age_filters["1year"] = "[AlterPerson80].[AgeGroupName8]"
        age_filters["0,15,20,25,30,40..."] = "[AlterPerson80].[AgeGroupName3]"
        age_filters["children_fine"] = "[AlterPerson80].[AgeGroupName1]"
        age_filters["children_medium"] = "[AlterPerson80].[AgeGroupName2]"
        age_filters["5year"] = "[AlterPerson80].[AgeGroupName6]"
        age_filters["default"] = age_filters["5year"]
        self.filter_values["age"] = age_filters
        self.filters["age"] = {"default":"[AlterPerson80].[AgeGroupName8]"}
        
        # SexGrouping
        sex_groups = {}
        sex_groups["male"] = "[Geschlecht].[SortGruppe].&[1]"
        sex_groups["female"] = "[Geschlecht].[SortGruppe].&[2]"
        sex_groups["divers"] = "[Geschlecht].[SortGruppe].&[3]"
        sex_groups["unknown"] = "[Geschlecht].[SortGruppe].&[999999]"
        self.filter_values["sex"] = sex_groups
        self.filters["sex"] = {"default":"[Geschlecht].[SortGruppe]"}
       
        # Case definition
        def_groups = {}
#        def_groups["not obtainable"] = "[Falldefinition].[ID].&[-1]"
        def_groups["clinical met"] = "[Falldefinition].[ID].&[1]"
        def_groups["clinical and epidemiological met"] = "[Falldefinition].[ID].&[2]"
        def_groups["lab and clinical met"] = "[Falldefinition].[ID].&[3]"
        def_groups["lab met, clinical not met"] = "[Falldefinition].[ID].&[4]"
        def_groups["lab met, clinical undetermined"] = "[Falldefinition].[ID].&[5]"
        self.filter_values["clinical_def"] = def_groups
        self.filters["clinical_def"] = {"default":"[Falldefinition].[ID]"}
        
        # Location
        loc_filters = {}
        loc_filters["LKs"] = "[DeutschlandNodes].[Kreise71Web].[FedStateKey71]"
        loc_filters["default"] = loc_filters["LKs"]
        self.filters["location"] = loc_filters
        
        # Pathogen
        self.filter_values["pathogen"] = {"COVID-19":"[PathogenOut].[KategorieNz].[Krankheit DE].&[COVID-19]"}
        self.filters["pathogen"] = {"default":"[PathogenOut].[KategorieNz].[Krankheit DE]"}
       
    def Request(self,hierarchy,values):
        cf = self.client_factory
        
        f = []
        for h,v in zip(hierarchy,values):
            short_h = "].[".join(h.split("].[")[:-1])+"]"
            f.append({ "Key":{"HierarchyId":h,"DimensionId":short_h},"Value":cf.FilterMemberCollection( v ) })
        filters = cf.FilterCollection(f)
        
        request = {}
        request["HierarchyFilters"] = filters
        
        request["Cube"] = "SurvStat"
        #    request["ColumnHierarchy"] = "[AlterPerson80].[AgeGroupName8]"
        request["ColumnHierarchy"] = "[AlterPerson80].[AgeGroupName6]"

        request["RowHierarchy"] = "[ReportingDate].[YearWeek].[YearWeek]"
        request["IncludeNullColumns"] = True
        request["InculdeTotalColumn"] = False
        request["IncludeNullRows"] = False
        request["InculdeTotalRow"] = False
        
        if self.debug:
            node = self.client.create_message(self.client.service,'GetOlapData',request) 
            print( etree.tostring(node,pretty_print=True).decode() )
        
        t1 = time.time()
        response = self.client.service.GetOlapData(request)
        t2 = time.time()
        print("in %.4fs"%(t2-t1))
#        print(response)
        
#        print(f)
   #     rfilters = []
    #    for k,v in filters:
      #      
       #     print(short_key)
      #      f = { "Key":{"HierarchyId":"[PathogenOut].[KategorieNz].[Krankheit DE]","DimensionId":"[PathogenOut].[KategorieNz]"},"Value":factory.FilterMemberCollection( ["[PathogenOut].[KategorieNz].[Krankheit DE].&[COVID-19]"] ) }
       #     rfilters.append(f)
        
    #    for x in rfilters:
     #       print(x)
        
class LK_Crawler(Crawler):
    def __init__(self,use_backup=False):
        super(LK_Crawler,self).__init__()
        
        
        if not use_backup or not self.HasBackup():
            self.Crawl()
    
    def HasBackup(self):
        return False
        
    def PermutateFilters(self,filters):
        """ filters as filter:filter_values """
        keys = [k for k in filters.keys()]
        
        cfilters = filters.copy()
        ckey = keys[-1]
        cfilter = cfilters.pop(ckey)
        
        if len(keys) > 1:
            r = self.PermutateFilters(cfilters)
            rhierarchy,rnames,rvalues = r["hierarchy"].copy(),r["names"].copy(),r["values"].copy()
            
            lfilters,lnames,lhierarchy = [],[],[]
            for k,v in cfilter["values"].items():
                for rh,rn,rv in zip(rhierarchy,rnames,rvalues):
                    lhierarchy.append([cfilter["hierarchy"]]+rh)
                    lnames.append([k]+rn)
                    lfilters.append([v]+rv)
                
            return {"hierarchy":lhierarchy,"names":lnames,"values":lfilters,"groups":[ckey]+r["groups"]}
            
        else:
            rfilters,rnames,rhierarchy = [],[],[]
            for k,v in cfilter["values"].items():
                rfilters.append([v]),rnames.append([k])
                rhierarchy.append([cfilter["hierarchy"]])
            return {"hierarchy":rhierarchy,"names":rnames,"values":rfilters,"groups":[ckey]}
    
    def AsyncRequest(self,filters):
        t1 = time.time()
        for hierarchy,values in zip(filters["hierarchy"],filters["values"]):
            self.Request(hierarchy,values)
#            print(hierarchy,value)
        
        t2 = time.time()
        print("in %.4fs"%(t2-t1))
        
    def Crawl(self):
        # Prepare the filters to grab all definitions for all sexes
        filters = {}
        filters["pathogen"] = {"hierarchy":self.filters["pathogen"]["default"],"values":self.filter_values["pathogen"]}
        filters["year"] = {"hierarchy":"[ReportingDate].[WeekYear]","values":{2020:"[ReportingDate].[WeekYear].&[2020]"}}
        for k in ["sex","clinical_def"]:
            fkey = self.filters[k]["default"]
            gvalues = self.filter_values[k].copy()
            gvalues.pop("default",None)
            filters[k] = {"hierarchy":fkey,"values":gvalues}

        for k,v in filters.items():
            print(k,v)
        
#        for lk in in self.lks.GetLandkreisIDs():
        for lk in [x for x in self.lks.GetLandkreisIDs()][:1]:
            cfilters = filters.copy()
        #    cfilters["location"] = {"hierarchy":"[DeutschlandNodes].[Kreise71Web].[FedStateKey71]","values":{lk:["[DeutschlandNodes].[Kreise71Web].[FedStateKey71]"+self.lks.GetSurvStatRKI_Suffix(lk)]}}
            pfilters = pfilters = self.PermutateFilters(cfilters)
            
            self.AsyncRequest(pfilters)
            

if __name__=="__main__":
    
    lkc = LK_Crawler()
#    response = Request(client)
#    print(response)