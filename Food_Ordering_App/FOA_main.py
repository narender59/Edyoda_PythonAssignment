from FOA_user import User 
from FOA_admin import Admin 
import pandas as pd
import getpass as gt                #For masking the password
import warnings

warnings.filterwarnings("ignore")

member_path = 'E:\Personal\Edyoda\Projects\Python\Food_Ordering_App\login.csv'
food_path = 'E:\Personal\Edyoda\Projects\Python\Food_Ordering_App\Food_items.csv'

def add_member(member_dict):
    df = pd.DataFrame(member_dict)
    df.to_csv(member_path , mode = 'a', index = False, header = False)

class Main:
    
    def execute(self, choice):
        
        if choice == 1:
            print('*'*8,'Hello, User', "*"*8)
            option = int(input('Are you a \n1. Existing User\n2. New User\n'))
            if (option == 1):
                user_email = input('Enter your email id: ')
                
                df = pd.read_csv(member_path)
                flag = (df['Email'] != user_email)
                for i in flag:
                    if i == False:
                        flag1 = False
                        break
                    flag1 = True
                if (flag1):
                    print('*'*8, 'Email Id is not registered with us', '*'*8)
                else:
                    user_password = gt.getpass('Enter your password:  ')
                    idx = df[df['Email'] == user_email].index
                    if df['Password'][idx[0]] == user_password:
                        user_status = True
                        print('Welcome User, Please Choose from the below option:-')
                        inp = int(input('1. Place a New Order\n2. Order History\n3. Update Profile\n4. Exit\n'))
                        while (inp<1 and i>4):
                            print('Please Choose the correct Options:-')
                            inp = int(input('1. Place a New Order\n2. Order History\n3. Update Profile\n4. Exit\n'))
                        else:
                            while user_status:
                                if inp == 1:
                                    print('*'*6, 'Lets Place a new Order', '*'*6)
                                    user_obj.place_new_order(user_email)
                                elif inp == 2:
                                    print('*'*6, 'Previous Orders till now', '*'*6)
                                    user_obj.order_history(user_email)
                                elif inp == 3:
                                    print('*'*6, 'Updating the Profile', '*'*6)
                                    user_obj.update_profile(user_email)
                                elif inp == 4:
                                    print('***********Thank you for connecting with us. Have a nice day.***********')
                                    user_status = False
                                    exit()
                                print('Welcome User, Please Choose from the below option:-')
                                inp = int(input('1. Place a New Order\n2. Order History\n3. Update Profile\n4. Exit\n'))
                                
                     
                    else:
                        print('*****Incorrect Password******')
                

            elif (option == 2):
                user_obj.user_registration()
                

        elif choice == 2:
            print('*'*8,'Hello, Admin', "*"*8)
            option = int(input('Are you a \n1. Existing Admin\n2. New Admin\n'))
            
            if (option == 1):
                admin_email = input('Enter your admin email id: ')
                
                df = pd.read_csv(member_path)
                flag = df['Email'] != admin_email
                flag1 = True
                for i in flag:
                    if i == False:
                        flag1 = False
                        break
                    
                if (flag1):
                    print('*'*8, 'Email Id is not registered with us', '*'*8)
                else:
                    admin_password = gt.getpass('Enter your admin password:  ')
                    idx = df[df['Email'] == admin_email].index
                    if df['Password'][idx[0]] == admin_password:
                        admin_status = True
                        print('Welcome Admin, Please Choose from the below option:-')
                        inp = int(input('1. Add a New food item\n2. Edit food item (using Food id)\n3. View all the food items\n4. Remove a food item (using food id)\n5. Exit\n'))
                        while (inp<1 and i>6):
                            print('Please Choose the correct Option')
                            inp = int(input('1. Add a New food item\n2. Edit food item (using Food id)\n3. View all the food items\n4. Remove a food item (using food id)\n5. Exit\n'))
                        else:
                            while admin_status:
                                if inp == 1:
                                    print('*'*6, 'Lets add food items into the list', '*'*6)
                                    admin_obj.add_food_items()
                                elif inp == 2:
                                    print('*'*6, 'Lets edit food items into the list', '*'*6)
                                    admin_obj.edit_food_items()
                                elif inp == 3:
                                    print('*'*6, 'The food items in the list', '*'*6)
                                    admin_obj.view_food_items()
                                elif inp  == 4:
                                    print('*'*6, 'Lets remove food items from the list', '*'*6)
                                    admin_obj.remove_food_items()
                                elif inp == 5:
                                    print('***********Thank you for connecting with us. Have a nice day.***********')
                                    admin_status = False
                                    exit()
                                print('Welcome Admin, Please Choose from the below option:-')
                                inp = int(input('1. Add a New food item\n2. Edit food item (using Food id)\n3. View all the food items\n4. Remove a food item (using food id)\n5. Exit\n'))
                            
                                    
                    else:
                        print('*****Incorrect Password******')
                

            elif (option == 2):
                master_password = gt.getpass('Enter Master Password to create a New Admin:  ')
                if (master_password == 'Edyoda'):                   #Master Password = Edyoda
                    admin_name = input('Enter your Full Name:  ')
                    admin_phone_no = input('Enter your contact number:  ')
                    admin_email = input('Enter your e-mail id:  ')
                    admin_address = input('Enter your address: ')
                    admin_password = gt.getpass('Create your admin password:  ')
                    admin_re_password = gt.getpass('Enter your admin password again:  ')
                    if (admin_password == admin_re_password):
                        admin_dict = {'Status': ['Admin'],
                                'Name' : [admin_name],
                                'Phone Number' : [admin_phone_no],
                                'Email' : [admin_email],
                                'Address': [admin_address],
                                'Password' : [admin_password]}
                        add_member(admin_dict)
                        print('*******Account Created Successfully.Thank You*********')
                    else:
                        print('Sorry, Password Mismatch. Restart Again')
      
           
        else:
            print('***********Thank you for connecting with us. Have a nice day.***********')
            exit()
        



if __name__ == '__main__':
    
    obj = Main()
    admin_obj = Admin()
    user_obj = User()
    print('*'*8,'Welcome to the Food Plaza', "*"*8)
    while True:
        choice = int(input('I am a \n1. User\n2. Admin\n'))
        obj.execute(choice)