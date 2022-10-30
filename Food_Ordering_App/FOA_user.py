import pandas as pd
import getpass as gt                #For masking the password

member_path = 'E:\Personal\Edyoda\Projects\Python\Food_Ordering_App\login.csv'
food_path = 'E:\Personal\Edyoda\Projects\Python\Food_Ordering_App\Food_items.csv'
order_path = 'E:\Personal\Edyoda\Projects\Python\Food_Ordering_App\Order_History.csv'

def add_member(member_dict):
    df = pd.DataFrame(member_dict)
    df.to_csv(member_path , mode = 'a', index = False, header = False)

def add_order(email, order_list):
    for food_id in order_list:
        order_dict = {'Email' : [email],
                     'Food ID' : [food_id]}
        df = pd.DataFrame(order_dict)
        df.to_csv(order_path, mode = 'a+', index = False, header = False)

# def edit_user_data(email, col_name, value):
#     df = pd.read_csv(member_path, index_col = "Email")
#     df.loc[email, col_name] = value
#     df.to_csv(member_path, index = False)
def edit_user_data(email, col_name, col_value):
    
    df = pd.read_csv(member_path)
    df[col_name]= df[col_name].replace([df[col_name][df["Email"]== email]], col_value)
    df.to_csv(member_path, index=False)

class User:
    
    def user_registration(self):
        print('*'*8, 'New User Registration', "*"*8)
        user_name = input('Enter your Full Name:  ')
        user_phone_no = input('Enter your contact number:  ')
        user_email = input('Enter your e-mail id:  ')
        user_address = input('Enter your address: ')
        user_password = gt.getpass('Create your password:  ')
        user_re_password = gt.getpass('Enter your password again:  ')
        if (user_password == user_re_password):
            user_dict = {'Status': ['User'],
                            'Name' : [user_name],
                            'Phone Number' : [user_phone_no],
                            'Email' : [user_email],
                            'Address': [user_address],
                            'Password' : [user_password]}
            add_member(user_dict)
            print('*******Account Created Successfully.Thank You*********')
        else:
            print('******Password Mismatch, Try Again.***********')
        
    def place_new_order(self, user_email):
        print('*'*8, 'Placing New Order', "*"*8)
        df = pd.read_csv(food_path)
        print(df.to_string(index=False))
        new = list(map(int, input('Select your food using Food ID, write numbers separated by commas:  ').split(','))) 
        for i in new:
            idx = (df[df['Food ID'] == i].index)[0]
            print(f'{df["Food Name"][idx]} ({df["Quantity"][idx]}) [INR {df["Price"][idx]}]')
        opt = input('Do you want to place the order (Y/N): ').lower()
        if opt=='y':
            add_order(user_email, new)
            print('********Congrats, Your order is placed***********')
        else:
            print('***********Thank you for connecting with us. Have a nice day.***********')
            exit()


    def order_history(self, user_email):
        print('*'*8, 'Order History', "*"*8)
        df_order_history = pd.read_csv(order_path)
        df_user_order = df_order_history[df_order_history["Email"]== user_email]
        df_food = pd.read_csv(food_path)
              
        print('Your previous orders are:-')
        for i in list(df_user_order["Food ID"]):
            print(f'{df_food[df_food["Food ID"]==i].to_string(index=False)}')
        print('*******That\'s all from your previous order**************')

    def update_profile(self,email):
        print('*'*8, 'User profile Edit', "*"*8)
        print('Which of the following data, you want to edit:')
        edit = int(input('1. Name\n2. Phone Number\n3. Address\n4. Password\n5. Exit\n'))
        while (edit>5 or edit<1):
            print('Choose the correct option')
            edit = int(input('1. Name\n2. Phone Number\n3.Email Id\n4. Address\n5. Password\n6. Exit\n'))
        else:
            df_member = pd.read_csv(member_path)
            idx = (df_member[df_member.Email == email].index)[0]
            if (edit == 1):
                print(f'Name (as per Data): {df_member["Name"][idx]}')
                user_name = input('Enter your new Full Name:  ')
                edit_user_data(email, "Name", user_name)
                print('Congrats! Name has changed successfully. Login Again')
                print('*'*35)
            elif (edit == 2):
                print(f'Contact Number (as per Data): {df_member["Phone"][idx]}')
                user_phone_no = input('Enter your new contact number:  ')
                edit_user_data(email, "Phone Number", user_phone_no)
                print('Congrats! Contact Number has changed successfully. Login Again')
                print('*'*35)
            elif (edit == 3):
                print(f'Address (as per Data): {df_member["Address"][idx]}')
                user_address = input('Enter your new address: ')
                edit_user_data(email, "Address", user_address)
                print('Congrats! Address has changed successfully. Login Again')
                print('*'*35)
            elif (edit == 4):
                print(f'Password (as per Data): {df_member["Password"][idx]}')
                user_password = gt.getpass('Create your password:  ')
                edit_user_data(email, "Password", user_password)
                print('Congrats! Password has changed successfully. Login Again')
                print('*'*35)