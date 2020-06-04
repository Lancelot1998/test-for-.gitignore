#!/bin/python
import os
import sys
from config import *

def partition(nodes, timeout):
  n=len(nodes)
  print(n)
  nodes1 = nodes[:int(n/2)]
  print(nodes1)
  nodes2 = nodes[int(n/2):]
  for n1 in nodes1:
     for n2 in nodes2:
         cmd = partition_cmd.format(n1, n2, timeout)
         os.system(cmd)

if __name__=='__main__':
    partition(NODES, TIMEOUT)
