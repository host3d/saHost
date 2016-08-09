#String
varStr = "gfjhfgj_+"


#var = 'gfjhfgj_+'

#Int
varInt = 3543676
#var = -3543676

#Float
varFloat = 1.0686
#var = -1.0686

#List
var = ['DSFDS', "dfss"]
var = [varStr, varInt, varFloat]
var = [varStr, varInt, False, None, ['toto', 'fak']]

#Tuple
var = ('DSFDS', "dfss")

#Boolean
var = False
var = True

#NoneType
var = None

#Dict
var = {
    'test' : 0,
    'cours' : "python",
    0 : False,
    'toto': [varStr, varInt, varFloat],
    'toto2': {
        'dsfds':True,
    },
}

print var
print(var)

print "Done"
print 'Done' + varStr
print 'Done' + str(varFloat) #varFloat = 1.0686
print 'Done' + str(var)

print 'Done',
print 'dsfdsf'
print 'Done',',','dsfdsf'

msg = 'val =' + str(varFloat) + ':' + str(varInt)
print msg



#######################
#String
varStr = "toto_001:abrand:r_toto_mod"
print type(varStr)
#pprint( dir(varStr))

varStr.startswith("g")
varStr.endswith("+")

s = ':'
res = varStr.split(s)
print res[0]
print res[-1]
print varStr[-1]



str() # to string
int() # to int
float() # to float
list()# to list
tuple()# to tuple
bool()# to boolean
dict()# to dict