#!/usr/bin/env python

import re

l=[m.start() for m in re.finditer('test', 'test test test test')]
print len(l)
