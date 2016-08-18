import maya.cmds as mc
import time
t = time.time()


#################################################
# test pour lister le range, mais rien su en faire...

list_a = range(0, 400, 2)
print list_a
list_b = range(1, 400, 2)
print list_b


for i in range(mc.polyEvaluate(face=True)):
    print i %2
    if i %2 == 0 :
        print 'toto'
        elif i %2 == 1:
            print 'tata'
            

for i in range(mc.polyEvaluate(face=True)):
    print i %2
    liste.count ("0")
    liste.count ("1")         
    
r=range(400)  
print r[-3:]

    
#################################################
# extrude de face precise
mc.polyExtrudeFacet('masphere.f[0:10]','masphere.f[20:30]','masphere.f[40:50]', keepFacesTogether=False, ltz=.1 )
#################################################


  
            
#################################################

mc.polySphere(name="maSphere")
for i in range(mc.polyEvaluate(face=True)):
    print 'Face :' + str(i)
    
## bon j'ai pas reussit a en faire si ca fait ca tu fait ca sinon si ca fait ca tu fait ca...    
    if ... == :
        mc.polyExtrudeFacet('masphere.f[*]', keepFacesTogether=False, ltz=.1 ):
    elif ... ==  :
        mc.polyExtrudeFacet('masphere.f[*]', keepFacesTogether=False, ltz=.5 ):


 
# clean scene
mc.delete ('maSphere')
mc.refresh


#################################################
#             CODER AU DESSUS                   #
#################################################

print "Code execute in %.3f sec" % (time.time() - t)