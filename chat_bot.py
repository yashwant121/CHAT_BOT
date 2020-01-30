import numpy as np 
import pandas as pd 
from nltk import word_tokenize
import nltk
import mongo_db 

import pprint

user=""
while user!="BYE":
    user = input("Please Enter your Query : ")
    UserQ=[]

    UserQ.append(user)


    def posTag(text):
        tagged_text_list = []
        tagged_text_list.append(nltk.pos_tag(word_tokenize(text)))
        return tagged_text_list

    UserOUT=posTag(user)

    def featureTags(pos_tagged_list):
    
        for i in pos_tagged_list:
            for j in i:
                if(j[1]=='NNS' or j[1]=='NNP' or j[1]=='NNPS' or j[1]=='NN' ):
                    return j[0]

        

    word=featureTags(UserOUT)


    if word =="gainers":
        for t in mongo_db.gainers.find():
            print(t)


    elif word =="loosers":
        for t in mongo_db.loosers.find():
            print(t)           

    else:
        print("please call 9560425119 Yashwant Yadav for further Assistance!!")




