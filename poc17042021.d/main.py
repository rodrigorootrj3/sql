from lib.libgenerica import Conecta 
from model.createdatabase import Sql

#var = Conecta().pegabancos()
#var = Sql().createtable()
#print(var['ALUNO'])
'''
banco = 'biruleibe'
valor = Sql().createtable(banco)
valor = valor['ALUNO']
Conecta().query(valor)
valor = Sql().createtable(banco)
valor = valor['MATRICULA']
Conecta().query(valor)
'''


banco = 'biruleibe'
#Diagnostico#
aux = Conecta().pegabancos(banco)
print(aux)
aux = Conecta().pegatabelas(banco)
print(aux)
query = "select * from ALUNO;"
aux = Conecta().query(query,banco)
print(aux)
query = "describe biruleibe.MATRICULA;"
aux = Conecta().query(query,banco)
print(aux)