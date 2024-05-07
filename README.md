# Minimum Plant Model
Derived from [Generic Crop Growth Model](https://github.com/RTGS-Lab/Generic_Crop_Growth/tree/main).

# MPM Versions
See [here for working verisons](https://docs.google.com/spreadsheets/d/1SK-l4JeugyJpgluEuVgbR2luuB4z7Lki/edit#gid=920949739).

#
|Version|Name|Description|
|-------|----|-----------|
|v0.0|Base C++ Model| Ported directly from Teh 2006. Code [here](v0-0-procedural-mpm-c). Separate repo with code [here](https://github.com/RTGS-Lab/Generic_Crop_Growth/tree/main)|
|v0.1|Base Python Model|Ported directly from C++. Code in this repo [here](v0-1-procedural-mpm)|
|v1.0|Conceptual advance procedural model|See [here](v1-0-procedural)|
|v2.0|Object oriented interface|See code [here](v2-0-OOP-Interface-Class)|
|v3.0|Object oriented functional model|See code [here](v3-0-OOP-operational)|

# Cases to Consider
1. Simple growing degree model for maize
2. Within-species variation (morphology substantially different *Brassica rapa L.*; see data from [Wang et al. 2019](https://academic-oup-com.ezp1.lib.umn.edu/jxb/article/70/9/2561/5368547?login=true&token=))
3. Cotton (lack strong selection for morphology, but some differences across genotypes; more modifications in physiology)
