#!/usr/bin/env python3.7
#coding:utf-8

import datetime
import time
import pickle
import os

from zeep import Client
from lxml import etree

from Landkreise import Landkreise


# Tools to crawl  https://survstat.rki.de/Content/Query/Select.aspx
# the Website allows queries for Covid19 cases with:
#   - 1-year age stratification of cases
#   - sex
#   - by definition (lab,clinical,epi)
#   - federal / state / county
#   - weekly resolution

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

def Request(client):
    lastUpdated = client.service.GetCubeInfo({"Cube":"SurvStat"})
    print(lastUpdated)
        
    print("Namespaces",client.namespaces)
    factory = client.type_factory('ns2')
    
    f1 = { "Key":{"HierarchyId":"[PathogenOut].[KategorieNz].[Krankheit DE]","DimensionId":"[PathogenOut].[KategorieNz]"},"Value":factory.FilterMemberCollection( ["[PathogenOut].[KategorieNz].[Krankheit DE].&[COVID-19]"] ) }
    f2 = {"Key":{"HierarchyId":"[Falldefinition].[ID]","DimensionId":"[Falldefinition].[ID]"},"Value":factory.FilterMemberCollection(["[Falldefinition].[ID].&[3]"])}
    f3 = { "Key":{"HierarchyId":"[DeutschlandNodes].[Kreise71Web].[FedStateKey71]","DimensionId":"[DeutschlandNodes].[Kreise71Web]"},"Value":factory.FilterMemberCollection( ["[DeutschlandNodes].[Kreise71Web].[FedStateKey71].&[03].&[DE92].&[03241]"] ) }
    f4 = { "Key":{"HierarchyId":"[Geschlecht].[SortGruppe]","DimensionId":"[Geschlecht]"},"Value":factory.FilterMemberCollection( ["[Geschlecht].[SortGruppe].&[1]"] ) }
    filters = factory.FilterCollection([f1,f2,f3,f4])

    
    request = {}
    request["Cube"] = "SurvStat"
#    request["ColumnHierarchy"] = "[AlterPerson80].[AgeGroupName8].[AgeGroupName8]"
    request["ColumnHierarchy"] = "[AlterPerson80].[AgeGroupName6].[AgeGroupName6]"

    request["RowHierarchy"] = "[ReportingDate].[YearWeek].[YearWeek]"
    request["IncludeNullColumns"] = True
    request["InculdeTotalColumn"] = True
    request["IncludeNullRows"] = False
    request["InculdeTotalRow"] = True
    
    request["HierarchyFilters"] = filters
    
    node = client.create_message(client.service,'GetOlapData',request) 
    
    # Let's see if the query looks correct.
    print( etree.tostring(node,pretty_print=True).decode() )
    
    response = client.service.GetOlapData(request)
    return response
 


if __name__=="__main__":
    client = Client("https://tools.rki.de/SurvStat/SurvStatWebService.svc?singleWsdl")
    
    response = Request(client)
    print(response)