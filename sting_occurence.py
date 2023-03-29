
from collections import OrderedDict
import numpy as np
 
test_str = "ALLTHEBESTFORYOUREXAMS"
 
res = {}
 
for keys in test_str:
    res[keys] = res.get(keys, 0) + 1
 
print(res)

keys = list(res.keys())
values = list(res.values())
print(keys)
print(values)