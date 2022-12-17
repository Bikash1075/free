from admin_user import *
obj=Restaurant()
print('Welcome to Food Ordering App')
print('-'*29)
while True:
    n=int(input('Choose one of the options\n1.Admin\n2.User\n3.Exit\n'))
    if n==1:
        print("Please register your details for admin")
        print('-'*39)
        obj.Register()
        obj.login()
        while True:
            admin=int(input('Enter your preference\n1.Add food items\n2.Edit food items\n3.View all food items\n4.Remove food items\n5.Logout\n'))
            if admin==1:
                obj.add_new_food_items()
                new_item=int(input('Do you want to add more items\n1.Yes\n2.No\n'))
                if new_item==1:
                    obj.add_new_food_items()
                elif new_item==2:
                    pass
                else:
                    print("-----Choose the correct option-----")
            elif admin==2:
                obj.edit_food_items()
            elif admin==3:
                obj.view_all_food_items()
            elif admin==4:
                obj.remove_food_items()
            elif admin==5:
                print('*****Thank you!! Logging out from the admin application*****')
                break
            else:
                print("-----Choose the correct option-----")
    elif n==2:
        print("Please register your details for user")
        print('-'*39)
        obj.Register()
        obj.login()
        while True:
            user=int(input('Enter your preference\n1.Place New Order\n2.Order History\n3.Update Profile\n4.Logout\n'))
            if user==1:
                obj.place_new_order()
                new_order=int(input('Do you want to add more items\n1.Yes\n2.No\n'))
                if new_order==1:
                    obj.place_new_order()
                elif new_order==2:
                    pass
                else:
                    print("-----Choose the correct option-----")
            elif user==2:
                obj.order_history()
            elif user==3:
                obj.update_profile()
            elif user==4:
                print('*****Thank you!! Logging out from the user application*****')
                break
            else:
                print("-----Choose the correct option-----")
    elif n==3:
        print("*****Exiting from the application*****")
        break
    else:
        print("-----Choose the correct option-----")