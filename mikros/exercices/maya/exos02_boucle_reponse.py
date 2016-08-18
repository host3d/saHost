__author__ = 'host3d'
import maya.cmds as mc
import random
#mc.file(newFile=True, force=True)
if mc.objExists("maSphere"):
    mc.delete("maSphere")

sub = 20
coef = 0.001
radius = 1
sphere = mc.polySphere(name="maSphere", sa=sub, sh=sub, radius=radius)

mc.setAttr('%s.ty' % sphere[0], radius)
mc.select(sphere)
faces = range( mc.polyEvaluate(f=True))
for i in faces:
    if i%10 == 0:
        val = (coef * i) * 2
    elif i%3 == 0:
        val = (coef * i) / 3
    elif i%2 == 0:
        val = (coef * i) / 4
    else:
        val = coef * i

    node = '%s.f[%s]' % (sphere[0], i)

    vertexCount = 0
    for info in mc.polyInfo(node, fv=True)[0].replace('\n', '').split(':')[-1].split(' '):
        if info == '':
            continue
        num = int(info)
        if num%10 == 0 and num:
            vertexCount /= 1.5
        else:
            vertexCount += num

    vertexCount /= 400.0
    val *= vertexCount


    mc.polyExtrudeFacet(node, localTranslateZ=val , localScale=(0.01,0.01,0.01))
    mc.delete(sphere[0],ch=True)
    print node
    if i == 0:
        node = '%s.f[%s:%s]' % (sphere[0], len(faces) + i ,len(faces) + 4)
    else:
        node = '%s.f[%s:%s]' % (sphere[0], len(faces) + i ,len(faces) + (i*4))

    myBlinn = mc.shadingNode('blinn', asShader=True)
    mc.select(node, r=True)
    mc.hyperShade( assign=myBlinn )

    r = random.randrange(0,1000) / 1000.0
    g = random.randrange(0,1000) / 1000.0
    b = random.randrange(0,1000) / 1000.0

    mc.setAttr('%s.color' % myBlinn , r, g, b, type='double3')
    mc.refresh()