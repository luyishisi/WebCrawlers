#!/usr/bin/env python
# coding=utf-8
import json
d = [{'first': 'One', 'second':2}]
json.dump(d, open('test.json', 'w'))
