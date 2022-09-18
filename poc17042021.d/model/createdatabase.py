
class Sql():
    def __init__(self):
        pass
    def createtable(self,banco):
        query = {}
        query['ALUNO'] = 'CREATE TABLE {}.ALUNO(ID INT(2),NOME VARCHAR(255))'.format(banco)
        query['MATRICULA'] = 'CREATE TABLE {}.MATRICULA(ID INT(2),MATRICULA INT(10))'.format(banco)
        query['BigA'] = Sql().big()
        return query

    def big(self):
        aux = 'foobarbaz'
        aux2 = 'barbara'
        query = {}
        query['A'] = '''DROP TABLE IF EXISTS urls;
        CREATE TABLE urls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        original_url TEXT NOT NULL,
        clicks INTEGER NOT NULL DEFAULT 0
        );'''

        query['B'] = '''DROP TABLE IF EXISTS urls;
        CREATE TABLE urls (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        {} TEXT NOT NULL,
        {} INTEGER NOT NULL DEFAULT 0
        );'''.format(aux,aux2)



        return query
