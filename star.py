#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Create and draw a star with varying node properties.
"""

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division

__author__ = """Fish (rahul@heartit.tech)"""

from pygraphviz import *

A=AGraph()
A.node_attr['style']='filled'
A.node_attr['shape']='circle'
A.node_attr['fixedsize']='true'
A.node_attr['fontcolor']='#ffffff'

for i in range(16):
    A.add_edge(0, i)
    n=A.get_node(i)
    n.attr['fillcolor']="#%2x0000"%(i*16)
    n.attr['height']="%s"%(i/16+0.5)
    n.attr['width']="%s"%(i/16+0.5)

print(A.string())
A.write("star.dot")
print("Wrote star.dot")
A.draw('star.png', prog="circo")
print('wrote star.png')