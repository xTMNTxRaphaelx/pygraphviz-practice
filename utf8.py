#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Example showing use of unicode and UTF-8 encoding
"""

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division

import pygraphviz as pgv

A=pgv.AGraph(encoding='UTF-8')
A.add_node(1, label='plain string')
A.add_node(2, label='unicode')

hello='Здравствуйте!'
A.add_node(3, label=hello)

hello='\u0417\u0434\u0440\u0430\u0432\u0441\u0442\u0432\u0443\u0439\u0442\u0435!'
A.add_node(4, label=hello)

goodbye="До свидания"
A.add_edge(1, hello, key=goodbye)

A.add_edge("שלום",hello)
A.add_edge(1,"こんにちは")

print(A)
A.write('utf8.dot')

B=pgv.AGraph('utf8.dot')
B.layout()
B.draw('utf8.png')
print('wrote utf png')