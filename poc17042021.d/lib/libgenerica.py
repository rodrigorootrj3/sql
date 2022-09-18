import os
import mysql.connector


class Conecta():
    def __init__(self):
        self.user = 'root'
        self.passwd = 'dbpass'
        self.url = '127.0.0.1'
        self.db = 'database'
        self.port = 8081

    def concreate(self):
        mydb = mysql.connector.connect(
            user = self.user,
            passwd = self.passwd,
            host = self.url,
            port = self.port        
        )
        return mydb

    def con(self,database):
        mydb = mysql.connector.connect(
            user = self.user,
            passwd = self.passwd,
            host = self.url,
            database = database,
            port = self.port 
        )
        return mydb

    def pegatabelas(self,banco):
        con = Conecta().con(banco)
        banco = banco
        query = "show tables;"
        _cursor = con.cursor()
        _cursor.execute(query)    
        _result = _cursor.fetchall()
        _cursor.close()
        array = []
        for x in range(0,len(_result)):        
            array.append(_result[x][0])
        return array
    
    def pegabancos(self,banco):
        con = Conecta().con(banco)
        query = "show databases;"
        _cursor = con.cursor()
        _cursor.execute(query)    
        _result = _cursor.fetchall()
        _cursor.close()
        array = []
        for x in range(0,len(_result)):        
            array.append(_result[x][0])
        return array

    def query(self,valor,banco):        
        valor = valor
        con = Conecta().con(banco)
        query = valor
        _cursor = con.cursor()
        _cursor.execute(query)    
        _result = _cursor.fetchall()
        _cursor.close() 


    def exibir(self):
        var =  self.user        
        print(var)
        return var
