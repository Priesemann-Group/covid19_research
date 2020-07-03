# covid19_research
Collection of jupyter notebooks and python scripts related to COVID-19 research.


### Notes on usage
This git repository uses submodules to link to different versions of our [toolbox](https://github.com/Priesemann-Group/covid19_inference). They can be easily imported without haveing to be installed via pip.


Import python module:
``` python
import sys
sys.path.append("../toolbox/[version]")
import covid19_inference as cov19
```


Add a new version of the toolbox as submodule via terminal:
```
cd toolbox
git submodule add -b [branch of version] git@github.com:Priesemann-Group/covid19_inference.git [folder name for submodule]
```