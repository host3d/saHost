import os
pathRoot = 's' + os.sep + 'prod' + os.sep + 'captain'
pathEntity = ['Asset', 'Sequence']
pathType = ['Character', 'Prop', 'Shot']

# MODE STRING
print "#### MODE STRING #####"
print "pathRoot: " + pathRoot

path = pathRoot + os.sep + pathEntity[0]
print "path: " + path

path = path + os.sep + pathType[0]
# on peut ecrire aussi: path += '/' + pathThype[0]
print "path: " + path

print "######################"
print ""
# MODE LIST
print "#### MODE LIST ####"
print "pathRoot: " + pathRoot
path = pathRoot.split(os.sep)
print "path: " + str(path)
path.append(pathEntity[1])
print "path: " + str(path)

path.append(pathType[-1])
print "path: " + os.sep.join(path)
print "###################"


# BOUCLE

# FOR
import maya.cmds as mc
nodesSelected = mc.ls(selection=True)

#Pour tout les elements selectionner on set l'attribut visiblity a 0.
for node in nodesSelected:
    print node
    mc.setAttr(node + ".visibility", False)

#Identique

for node in mc.ls(selection=True):
    print node
    mc.setAttr(node + ".visibility", False)


# IF
#Pour tout les elements selectionner on set l'attribut visiblity a 0 si l'attribut visibility exists sur le node
for node in mc.ls(selection=True):
    if mc.attributeQuery('visibility', node=node, exists=True):
        print node
        mc.setAttr(node + ".visibility", False)

#Pour tout les elements selectionner on set l'attribut visiblity a 0 si l'attribut visibility exists sur le node
# et que l'attribute soit setter a True.
for node in mc.ls(selection=True):
    if mc.attributeQuery('visibility', node=node, exists=True) and mc.getAttr(node + ".visibility") == True:
        print node
        mc.setAttr(node + ".visibility", False)
#identique
for node in mc.ls(selection=True):
    if mc.attributeQuery('visibility', node=node, exists=True) and mc.getAttr(node + ".visibility"):
        print node
        mc.setAttr(node + ".visibility", False)

#Pour tout les elements selectionner on set l'attribut visiblity a 0 si l'attribut visibility exists sur le node
# et que l'attribute est setter a True puis que le nom du node ne doit par commencer __.
for node in mc.ls(selection=True):
    if mc.attributeQuery('visibility', node=node, exists=True) and mc.getAttr(node + ".visibility") and not node.startswith('__'):
        print node
        mc.setAttr(node + ".visibility", False)

#Pour tout les transform dans la scene si l'attribut visibility est egale a False et qu'il est pas locker et n'a pas de connectiond
#Alors on set sa valeur a True
for node in mc.ls(transforms=True):
    if not mc.getAttr(node + ".visibility") and not mc.getAttr(node + ".visibility", l=True) and not mc.listConnections(node + ".visibility"):
        print node
        mc.setAttr(node + ".visibility", True)


#DOC MAYA

#Lien doc : http://help.autodesk.com/cloudhelp/2016/ENU/Maya-Tech-Docs/CommandsPython/index.html

#import maya.cmds as mc : permet d'acceder au commande maya <3

#ls  : commande pout lister des noeud dans maya
#Presentement on l'utilise pour recuperer la selection courante dans maya

#setAttr : permet de changer la valeur d'un attribut dans maya.

#getAttr : permet de recuperer la valeur d'un attribut dans maya.

#AttributeQuery : Permet de questionner un attribute d'un node maya.

#listConnections : Permet de lister les connection d'un noeud ou un attribut donne