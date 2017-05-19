#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A simple example to create a graphviz dot file and draw a graph
"""

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division

__author__ = """Fish (rahul@heartit.tech)"""

import pygraphviz as pgv

A=pgv.AGraph()

A.add_edge(1, 2)
A.add_edge(2, 3)
A.add_edge(1, 3)

print(A.string())
print("Write simple.dot")
A.write('simple.dot')

B=pgv.AGraph('simple.dot')
B.layout()
B.draw('simple.png')
print('wrote simple.png')