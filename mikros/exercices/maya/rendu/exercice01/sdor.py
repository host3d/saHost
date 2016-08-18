import maya.cmds as cmds
import random

oName='Sphere'
#test l'existence de l'objet pour ne pas en creer un double
if cmds.objExists(oName):
    cmds.delete(oName)
cmds.polySphere ( name=oName ,radius= 3, subdivisionsX =10,subdivisionsY =10)

#recupere le mombre de face de l'objet
oNombreFace= cmds.polyEvaluate(oName, f=True )


for oFaceNumber in range (0,oNombreFace ):
    oModulo= oFaceNumber%6
    if  oModulo==0:
        oExtrude=0.1
    elif  oModulo==1:
        oExtrude=0.8
    elif  oModulo==2:
        oExtrude=0.5
    elif  oModulo==3:
        oExtrude=0.4
    elif  oModulo==4:
        oExtrude=0.7
    else:
        oExtrude=0.1
  
cmds.refresh()    