__author__ = 'host3d'
import maya.cmds as mc

#mc.file(newFile=True, force=True)
if mc.objExists("maSphere"):
    mc.delete("maSphere")

sub = 20
coef = 0.001
radius = 1
sphere = mc.polySphere(name="maSphere", sa=sub, sh=sub, radius=radius)

mc.setAttr('%s.ty' % sphere[0], radius)
mc.select(sphere)
for i in range( mc.polyEvaluate(f=True)):
    if i%2 == 0:
        val = (coef * i) / 2
    elif i%3 == 0:
        val = (coef * i) / 3
    elif i%4 == 0:
        val = (coef * i) / 4
    else:
        val = coef * i
    node = '%s.f[%s]' % (sphere[0], i)
    mc.polyExtrudeFacet(node, lt=(0,0,val), ls=(0.01,0.01,0.01) )
    mc.delete(sphere[0],ch=True)
    mc.refresh()
