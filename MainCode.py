# coding=utf-8

import itchat
import time
from itchat.content import *
from SQLControler import SQLController
from SQLControler import WordsModel

#保存她的文字
def SaveWordsToTxt(words):
    file = open("HerWords.txt", 'a+', encoding='utf-8')
    file.write(words + '\r\n')
    file.close()

@itchat.msg_register(TEXT)
def others_send_me_message(msg):

    #是她发给我的消息
    if(Friend['UserName'] == msg['FromUserName']):
        #保存数据到文件中
        SaveWordsToTxt(msg['Content'])
        print('She Send Me : ' + msg['Content'])
        model = WordsModel(msg['Content'])
        Controller.AddWords((model))


Controller = SQLController()
for word in Controller.ReadAllWords():
    print(word)

#自动登录
itchat.auto_login(hotReload=True)
print('登陆成功')
#获取好友列表
Friend = itchat.search_friends(name='何姗')[0]
print("获得她的信息 : " + Friend['NickName'])
itchat.run(True)


