from cadastros import (Pessoas,Cadastrar,Deletar)
from conectionbd import (DataBase)


nome = input("Digite Seu nome Completo:")
apelido = input("Agora seu Apelido:")
cpf = input("Seu CPF:")
endereco = input("Seu Endereço:")
bairro = input("Por ultimo /n Seu Bairro:")



p = Pessoas('null',f'{cpf}',f'{nome}',f'{apelido}',f'{endereco}',f'{bairro}')   

db = DataBase()
db.connect()
db.create_table_pessoas()
db.close_connection()


pessoa_input = (p.cpf,p.nome,p.apelido,p.endereco,p.bairro)
# #pessoa_input = (p.nome)


# j = (1, '107.978.217.67', 'Pablo Libalde', 'Pablo', 'Rua Argeu Resende, 96', 'Centro')


# Cadastrar.pessoa(pessoa_input)

# print(db.select_all_pessoas())

<<<<<<< HEAD
x = DataBase.select_all_pessoas()
print(x)
for y in x:
    print(y)
    d = ()
    d = Pessoas(y)
    print(d.id, d.nome)
=======
<<<<<<< HEAD
# x = db.select_all_pessoas()
# for y in x:
#     # print(y)
#     lista =['cpf','nome','apelido','endereco','bairro','id']
#     # print(lista[0])
#     dic={}
#     for col in y:
#         print(col)
#     #     p= 0
#         dic[f'{lista[p]}']=col
#     # print(dic)
=======
x = DataBase.select_pessoas(retorno='ID',condicao='NOME LIKE "%Pablo%"')
print(x)
# for y in x:
#     if 'Pablo' in y:
#         print(y)
#         print(y[0])
>>>>>>> f4e8fdfdc44cd1db1e8e77a9b57d6f1b12b5fede
>>>>>>> ebc43a3691e7c5c84eaf83feed6eb87546025c52


nome(f'{Ketully.nome}')
nome(f'{Pablo.nome}')
nome('Feio_Raquelle')
nome('Feio_Cassio')
nome('Feio_Loren')

{''}