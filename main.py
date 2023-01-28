from cadastros import (Pessoas,Cadastrar)
from conectionbd import (DataBase)

p = Pessoas('107.978.217.67','Pablo Libalde','Pablo','Rua Argeu Resende, 96','Centro')   

db = DataBase()
db.connect()
db.create_table_pessoas()
db.close_connection()


pessoa_input = (p.cpf,p.nome,p.apelido,p.endereco,p.bairro)

c = Cadastrar
c.pessoa(pessoa_input)