#Define the menu of restaurant

menu ={
    'Pizza':100,
    'Pasta': 200,
    'Burger': 100,
    'Salad': 50,
    'Coffee': 80,
    'Chicken Roll': 200
}


#Customer Greeting
print("Welcome to Python Restaurant")
print(" Pizza: Rs.100\n Pasta: Rs.200\n Burger: Rs.100\n Salad: Rs.50\n Coffee: Rs.80\n Chicken Roll Rs.200")


order_total = 0

item_1 = input('Enter the name of your item that you want to order = ')

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your Item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available yet!")


another_order = input("Do You want to add another item? (Yes/No) ")

if another_order == "Yes":
    item2 = input("Enter the name of Second Item = ")
    if item2 in menu:
        order_total += menu[item2]
        print(f"Item {item2} has been added to order")

    else:
        print(f"Ordered Item {item2} is not available!")

print(f"The total amount of items to pay is {order_total}")




