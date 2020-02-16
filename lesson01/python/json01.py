# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 14:21:18 2020

@author: Administrator
"""
import json
from collections import OrderedDict
import pprint

s = r'{"C": "\u3042", "A": {"i": 1, "j": 2}, "B": [{"X": 1, "Y": 10}, {"X": 2, "Y": 20}]}'

print(s)
# {"C": "\u3042", "A": {"i": 1, "j": 2}, "B": [{"X": 1, "Y": 10}, {"X": 2, "Y": 20}]}

d = json.loads(s)

pprint.pprint(d, width=40)
# {'A': {'i': 1, 'j': 2},
#  'B': [{'X': 1, 'Y': 10},
#        {'X': 2, 'Y': 20}],
#  'C': 'あ'}

print(type(d))