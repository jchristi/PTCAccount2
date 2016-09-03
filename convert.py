#!/usr/bin/env python2
import sys

from collections import OrderedDict

try:
    filename = sys.argv[1]
except:
    filename = 'accounts.txt'

accounts = OrderedDict()

with open(filename, 'r') as infile:
    for line in infile:
        username, password = [x.strip() for x in line.split(':', 1)]
        accounts[username] = password

print 'username: [' + ','.join(accounts.keys()) + ']'
print 'password: [' + ','.join(accounts.values()) + ']'
