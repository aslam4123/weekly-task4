from user import *
from list import *
from admin import *
def register():
    if len(usr)==0:
        id=101
    else:
        id=usr[-1]['id']+1

    email=str(input('enter the email:'))
    f1=0
    for i in usr:
        if i['email']==email:                                                                           
            f1=1                                                                                   
            register()
    if f1==0:
        print('Registration')
        name=str(input('enter the name:'))
        phoneno=int(input('enter the phone no:'))
        password=str(input('enter the password:'))
        usr.append({'name':name,'id':id,'email':email,'phoneno':phoneno,'password':password,'dress':[]})
def login():
    username=input('enter the uname:')
    password=input('enter the password:')
    f=0
    if username=='admin' and password=='admin':
        f=1
    user=''
    for i in usr:
        if username==i['email'] and password==i['password']:
            f=2
            user=i
    return f,user