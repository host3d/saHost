"""
EXERCICE 01 :
    Creer une sphere et faire un extrude de taille aleatoire sur chaque face.

    Il est interdit d'utiliser le module random ;).

    Consigne + :
         - le code doit cleaner se qui a ete creer si on le relance.

    Aide commande Maya :
        penser a regarder la doc ou le quick help de chacune de ses fonctions.

        objExists : permet de savoir si un node exists
        delete : permet de supprimer un node
        polyShpere : permet de creer une sphere
        polyEvaluate : permet de recuperer des information sur un meshe.
        polyExtrudeFacet : Permet de faire un extrude.
        refresh : permet de fair un refresh dans maya.

    Aide python :
        range : En lui donner un chiffre il nous retourne une liste de chiffre de la taille du fchiffre donnee
            exemple :
                range(10)
                -> result : [0,1,2,3,4,5,6,7,8,9]

    merci de me copier votre code dans un fichier python avec votre nom de user ici :
    /s/prods/captain/_sandbox/salexis/saHost/mikros/exercices/maya/rendu/exercice01/

    exemple du nom de fichier : salexis.py

    merci a vous et bonne chance :)

"""
import maya.cmds as mc
import time
t = time.time()

#################################################
#             CODER EN DESSOUS                  #
#################################################


# Good luck :)
mc.polySphere(name="maSphere")
for i in range(mc.polyEvaluate(face=True)):
    print 'Face :' + str(i)



#################################################
#             CODER AU DESSUS                   #
#################################################

print "Code execute in %.3f sec" % (time.time() - t)
