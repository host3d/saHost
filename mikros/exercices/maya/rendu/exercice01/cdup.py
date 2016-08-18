#!/usr/bin/env python
# coding:utf-8
""":mod:`cours01` -- dummy module
===================================

.. module:: moduleName
   :platform: Unix
   :synopsis: module idea
"""
# Python built-in modules import

# Third-party modules import

# Mikros modules import

__author__ = "cdupin"
__copyright__ = "Copyright 2016, Mikros Image"

import maya.cmds as mc
import time
t = time.time()

## Clean Scene befor running script

if mc.objExists('mySphere'):
    mc.delete('mySphere')

## Create sphere
mc.polySphere(name="maSphere")
for i in range(mc.polyEvaluate(face=True)):
    if i % 2 == 0:
        index = 'maSphere.f[' + str(i) + ']'
        mc.polyExtrudeFacet(index, ltz=0.8, ls=(.5,.5,.5))
        mc.refresh(f=True)
    elif  i % 5 == 0:
        index = 'maSphere.f[' + str(i) + ']'
        mc.polyExtrudeFacet(index, ltz=0.2, ls=(.2,.2,.2))
        mc.refresh(f=True)
    else:
        index = 'maSphere.f[' + str(i) + ']'
        mc.polyExtrudeFacet(index, ltz=0.5, ls=(.2,.2,.2))
        mc.refresh(f=True)
        
print "Code execute in %.3f sec" % (time.time() - t)