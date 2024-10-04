usr=[]
mwr=[]
while True:
    print('''
    1.register
    2.login
    3.exit''')
    choice=int(input('enter the choice:'))
    if choice==1:
        register()
    elif choice==2:
        f,user=login()
        if f==1:
            while True:
                print('''
                1.add dress
                2.view dress
                3.update dress
                4.delete dress
                5.view user
                6.logout''')
                sub_choice=int(input('enter the choice:'))
                if sub_choice==1:
                    add_dress()
                elif sub_choice==2:
                    view_dress()
                elif sub_choice==3:
                    update_dress()
                elif sub_choice==4:
                    delete_dress()
                elif sub_choice==5:
                    view_user()
                elif sub_choice==6:
                    break

        elif f==2:
            while True:
                print('''
                1.view profile
                2.view dress
                3.update profile
                4.buy dress
                5.dress in hand
                6.logout''')
                sub_choice=int(input('enter the choice:'))
                if sub_choice==1:
                    view_profile(user)
                elif sub_choice==2:
                    view_dress()
                elif sub_choice==3:
                    update_profile(user)
                elif sub_choice==4:
                    buy_dress(user)
                elif sub_choice==5:
                    dress_in_hand(user)
                elif sub_choice==7:
                    break
        else:
            print('invalid username or password')
    elif choice==3:
        break
    else:
        print('invalid choice')