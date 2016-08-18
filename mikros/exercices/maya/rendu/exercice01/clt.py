import maya.cmds as mc
import time
t = time.time()
## clean previous created spheres
if mc.objExists('turlute'):
    mc.delete('turlute')
## create sphere
mc.polySphere(name="turlute", sx=9, sy=9, r=10)
for i in range(mc.polyEvaluate(face=True)):
    rand = ''+ str(i) +''
    if rand.endswith('0') or rand.endswith('3') or rand.endswith('6'):
        name = 'turlute.f['+ str(i) + ']'
        mc.polyExtrudeFacet(name, ltz=1, ls=(.5,.5,.5))
        mc.refresh(f=True)
    elif rand.endswith('1') or rand.endswith('4') or rand.endswith('7'):
        name = 'turlute.f['+ str(i) + ']'
        mc.polyExtrudeFacet(name, ltz=4, ls=(.5,.5,.5))
        mc.refresh(f=True)
    elif rand.endswith('2') or rand.endswith('8'):
        name = 'turlute.f['+ str(i) + ']'
        mc.polyExtrudeFacet(name, ltz=1.5, ls=(.75,.75,.75))
        mc.refresh(f=True)  
    elif rand.endswith('5') or rand.endswith('9'):
        name = 'turlute.f['+ str(i) + ']'
        mc.polyExtrudeFacet(name, ltz=3, ls=(.3,.3,.3))
        mc.refresh(f=True)
        
print "Code execute in %.3f sec" % (time.time() - t)
    
    
    
    



