import os
PATH = r'/s/prods/captain/assets/Anim/'
banks = [f for f in os.listdir(PATH)]
# banks = ['leaf_bunch_a', 'leaf_bunch_b', 'leaf_bunch_c', 'branch_a', 'grass_clumps', 'grass_borders', 'grass_small_clumps', 'grass_flat_clumps', 'test_bank', 'pebbles', 'clover', 'dead_leaves', 'flowers']

# ARRAY
print banks
#append <3
# Permet d'ajout un element a la FIN de la list
print '\n'+"#"*20 + " append " + "#"*20
prop = 'bob'
banks.append(prop)
print banks

#extend <3
# Permet d'ajouter des elements dans un liste depuis une autres lite
print '\n'+"#"*20 + " extend " + "#"*20
character = ['george', 'harold', 'krupp']
banks.extend(character)
print banks

#insert <3
#Permet d'inserer un element dans un list a une position bien defini.
print '\n'+"#"*20 + " insert " + "#"*20
i = 0
print 'insert '+ prop +' at index ' + str(i)
banks.insert(i, prop)
print banks

#count
# Permet de compter le nombre de fois que lq liste contient l'element donne
print '\n'+"#"*20 + " count " + "#"*20
print "Il y a " + str(banks.count(prop)) + " " + prop + " dans la list banks"

#index
# Retourne l'index du premier element trouver demander.
print '\n'+"#"*20 + " index " + "#"*20
print banks
print banks.index(prop)
print prop + ' at index ' + str(banks.index(prop))

#pop <3
#Remove l'element d'un liste a une postion defini.
print '\n'+"#"*20 + " pop " + "#"*20
i = 5
print banks
print "Remove element " + str(i) + " in list banks ---> " + banks[i]
banks.pop(i)
print banks

#remove <3
print '\n'+"#"*20 + " remove " + "#"*20
# remove le premier element donnee trouver dans la list
print banks
print 'Remove element ' + prop
banks.remove(prop)
print banks

#reverse
# permet d'inverse l'odre de la liste
print '\n'+"#"*20 + " reverse " + "#"*20
print banks
banks.reverse()
print banks

#sort
# permet de trier la liste
print '\n'+"#"*20 + " sort " + "#"*20
print banks
banks.sort()
print banks
banks.sort(reverse=True)
print banks

print "\n"+"*" * 80

# Array manipulation <3

#join
# Permet de transformer un list en str en mettant un string entre chaque element
print '\n'+"-"*20 + " join " + "-"*20
print '|'.join(banks)

#len
# Permet de compter le nombre d'element contenu dans la list
print '\n'+"-"*20 + " len " + "-"*20
print "Il y a " + str(len(banks)) + " element(2) dans la list."

#sorted
print '\n'+"-"*20 + " sorted " + "-"*20
# Permet de trier un list sans modifier le veritable ordre de la liste.
print sorted(banks)
print sorted(banks, reverse=True)


# NERD Manipulation
print '\n'+":) "*20 + " NERD " + "(: "*20
#reverse
print banks[::-1]
#first item
print banks[0]
#last item
print banks[-1]
# item betweem index 5 and 6
print banks[5:6]
#all item after index 5
print banks[5:]
#all item beofre index 6
print banks[:6]

print '\n'+":) "*20 + " VERY NERD " + "(: "*20

print banks
# Afficher un elemnr sur 2 a partie de l'index 0
print banks[0::2]
# Afficher un elemnr sur 2 a partie de l'index 1
print banks[1::2]