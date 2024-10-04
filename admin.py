def add_dress():
    if len(mwr)==0:
        id=10
    else:
        id=mwr[-1]['id']+1

    f2=0
    for i in mwr:
        if i['id']==id:                                                                           
            f2=1                                                                                   
            add_dress()
    if f2==0:
        print('Dress details')
        name=str(input('enter the dress:'))
        stock=int(input('enter the stock:'))
        size=str(input('enter the size:'))
        price=int(input('enter the price:'))
        mwr.append({'name':name,'id':id,'stock':stock,'size':size,'price':price})                                   
def view_dress():                                                                                        
    for i in mwr:
        print(i)
def update_dress():
    id=int(input('enter the id:'))
    f2=0
    for i in mwr:
        if i['id']==id:                                                                           
            f2=1                                                                                   
        stock=int(input('enter the stock:'))
        price=int(input('enter the price:'))
        i['stock']=stock
        i['price']=price
    if f2==0:
        print('invalid')
def delete_dress():
    id=int(input('enter the id:'))
    f2=0
    for i in mwr:
        if i['id']==id:                                                                           
            f2=1
            mwr.remove(i)                                                                                   
    if f2==0:
        print('invalid')
def view_user():
    for i in usr:
        print('USER')
        print('name:',i['name'])
        print('id:',i['id'])
        print('email:',i['email'])
        print('phoneno:',i['phoneno'])
