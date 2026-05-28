food = input("Enter the food:")
quantity=int(input("Quantity of the food:"))
if food == "pizza":
    print("pizza is available\n")
    price= 250
    print("pizza price is",price)
    print("quantity of the pizza is \n",quantity)
    delivary=input("is delivary is available (yes or no):")
    if delivary == "yes":
        print("The delivary is available\n")
    else:
        print("The delivary is unavailable")
    print("------------------")
    print("Total amount: ",price*quantity)
    print("------------------")
elif food == "burgar":
    print("Burgar is available\n")
    price=300
    print("Burgar price is",price)
    print("quantity of the Burgar is ",quantity)
    delivary=input("is delivary is available (yes or no):")
    if delivary == "yes":
        print("The delivary is available\n")
    else:
        print("The delivary is unavailable\n")
    print("------------------")
    print("Total amount: ",price*quantity)
    print("------------------")
elif food == "shawarma":
    print("Shawarma is available\n")
    price= 150
    print("Shawarma price is",price)
    print("quantity of the Shawarma is ",quantity)
    delivary=input("is delivary is available (yes or no):")
    if delivary == "yes":
        print("The delivary is available\n")
    else:
        print("The delivary is unavailable\n") 
    print("------------------")
    print("Total amount: ",price*quantity)
    print("------------------")
else:
    print("Sorry the food is unavailable!!!")
