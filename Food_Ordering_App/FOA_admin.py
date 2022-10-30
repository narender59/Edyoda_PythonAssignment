import pandas as pd


food_path = 'E:\Personal\Edyoda\Projects\Python\Food_Ordering_App\Food_items.csv'

def add_food(food_details_dict):
    df = pd.DataFrame(food_details_dict)
    
    df.to_csv(food_path, mode = 'a', index = False, header = False)

def edit_food(food_id, col_name, col_value):
    
    df = pd.read_csv(food_path)
    df[col_name]= df[col_name].replace([df[col_name][df['Food ID']== food_id]], col_value)
    df.to_csv(food_path, index=False)

class Admin:
    def __init__(self):
        df = pd.read_csv(food_path)
        self.food_id_count = int(df['Food ID'].tail(1))

    def add_food_items(self): #Just increase food id and decrease stock after placing order
        self.food_id_count += 1
        food_name = input('Enter the food item name:  ')
        food_quantity = input(f'Enter the quantity of {food_name}:  ')
        food_price = input(f'Enter the price of {food_name}:  ')
        food_discount = input(f'Enter the discount on {food_name}:  ')
        food_stock = input(f'Enter the stock available of {food_name}:  ')
        food_id = str(self.food_id_count)
        food_item_dict = {'Food ID' : [food_id],
                          'Food Name': [food_name],
                          'Quantity': [food_quantity],
                          'Price': [food_price],
                          'Discount': [food_discount],
                          'Stock': [food_stock]}
        add_food(food_item_dict)
        
            
    def edit_food_items(self): 
        self.view_food_items()
        food_id = int(input('Enter the Food ID  for editing the food items:  '))
        
        df = pd.read_csv(food_path)
        if food_id in list(df['Food ID']):
            print(df[df["Food ID"]== food_id].to_string(index=False))
            print('*'*35)
            print('Modify from the following choice:-')
            print('1. Name\n2.Quantity\n3.Price\n4.Discount\n5.Stock\n6. Exit')
            n = int(input('Enter your choice (1 to 5) which need modification:  '))
            while(n>6 or n<1):
                print('*'*35)
                print('Modifify from the following choice:-')
                print('1. Name\n2.Quantity\n3.Price\n4.Discount\n5.Stock\n6. Exit')
                n = int(input('Enter your choice (1 to 6):  '))
            else:
                if (n==1):
                    food_name = input('Enter new Food name:  ')
                    edit_food(food_id, 'Food Name', food_name)
                elif (n==2):
                    food_quantity = input('Enter new Quantity:  ')
                    edit_food(food_id, 'Quantity', food_quantity)
                elif (n==3):
                    food_price = input('Enter new Food Price:  ')
                    edit_food(food_id, 'Price', food_price)
                elif (n==4):
                    food_discount = input('Enter new Discount:  ')
                    edit_food(food_id, 'Discount', food_discount)
                elif (n==5):
                    self.stock = input('Enter new Stock value:  ')
                    edit_food(food_id, 'Stock', food_stock)
        else:
            print('ALERT!!! Incorrect Food ID')
        

    def view_food_items(self):
        
        df = pd.read_csv(food_path)
        print(df.to_string(index=False))

    def remove_food_items(self): 
        
        df = pd.read_csv(food_path)
        print(df.to_string(index=False))
        food_id = int(input('Enter the Food ID  to delete the food items:  '))
        if food_id in list(df['Food ID']):
            n = int(input('******Are you sure to delete the below food items from the list********\n1. Yes\n2. No\n'))
            if n == 1:
                df = df[df['Food ID'] != food_id]
                df.to_csv(food_path, index = False)
                print(f'Congrats! Food ID {food_id} is removed successfully.')
            else:
                print('************Okay, No Problem*************')
        else:
            print(f'Sorry, No such food items available with the Food ID: {food_id}')
