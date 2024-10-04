def view_profile(user):
    print(user)
def update_profile(user):
    name=str(input('enter the name:'))
    phoneno=int(input('enter the phone no:'))
    user['name']=name
    user['phoneno']=phoneno
def buy_dress(user):
    id=int(input('enter the id:'))
    f=0
    for i in mwr:
        if i['id']==id:
            f=1
            i['stock']-=1
            user['dress'].append(id)
            print('dress added')
    if f==0:
        print('invalid id')
def dress_in_hand(user):
    print(user['dress'])