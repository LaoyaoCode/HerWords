# coding=utf-8

import string
import sqlite3
import time

SQLFileName = "MineLVerSaid.db"

class SQLController:

    def __init__(self):

        #连接数据库
        connect = sqlite3.connect(SQLFileName)
        connect.text_factory = str

        #如果不存在则创建表
        c = connect.cursor()
        c.execute(
            '''CREATE TABLE IF NOT EXISTS HerWords
               (
                ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                Words           TEXT    NOT NULL,
                Time            VARCHAR(50)     NOT NULL
                );''')

        connect.commit()

        self.__Connect = connect
        print("SQLite Data Create Success + " + SQLFileName)

    #添加数据到数据库中,test success
    def AddWords(self, model):
        if(not isinstance(model,WordsModel)):
            raise Exception('只能保存文字模型')

        c = self.__Connect.cursor()
        c.execute(model.GetSaveSQLWords())
        self.__Connect.commit()

    def ReadAllWords(self):

        c = self.__Connect.cursor()
        c.execute("SELECT Words,Time FROM HerWords;")
        Tables = c.fetchall()

        return Tables

    #关闭数据库连接
    def Close(self):
        self.__Connect.close()

class WordsModel:

    def __init__(self, words):
        self.Words = words
        self.Time = time.strftime('%Y-%m-%d$%H:%M:%S', time.localtime(time.time()))

    def GetTimeAndDate(self):
        time = self.Time
        time = time.split('$')
        return time[0], time[1]

    def GetSaveSQLWords(self):
        return '''INSERT INTO HerWords(Words,Time) ''' + ''' VALUES(''' + '\''+self.Words + '\',\'' + self.Time + '\');'
