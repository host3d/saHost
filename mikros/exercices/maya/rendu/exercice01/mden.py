import maya.cmds as mc

if mc.objExists ("maSphere"):
   mc.delete  ("maSphere")
   
mc.polySphere(name="maSphere")
bouboule = "maSphere"
i = bouboule
for i in range(mc.polyEvaluate(face=True)):
    var = 'bouboule face :' + str(i)
    print var
    mc.polyExtrudeFacet("maSphere", localTranslateZ Length=1)
mc.refresh

print "Code execute in %.3f sec" % (time.time() - t)