products = ["Laptop", "Phone", "Keyboard", "Mouse"]
cart = []
def show_products() :
    print("Available Products :")
    print()
    for index, product in enumerate(products, start=1):
         print(f"{index}. {product}")
    print()
def add_product() :
    product_no = int(input("Enter product : "))
    print()
    if product_no <= 0 or product_no > len(products):
         print("Invalid product selected!")
    else:
        print(f"{products[product_no - 1]} successfully added to cart")
        print()

        item = products[product_no - 1]
        cart.append(item)
def show_cart() :
    if len(cart) == 0 :
        print("Your cart is empty!")
        print()
    else:    
        print("=" * 50)
        print("             Shopping Cart") 
        print("=" * 50)
        print()
        for index,item in enumerate(cart , start = 1 ) : 
            print(f"{index}. {item}")
        print()   
        print("=" * 50)
        print(f"Total items : {len(cart)}")
        print()
        print("=" * 50)
        print()
def remove_item() :
    print()
    print("=" * 50)
    print("Shopping cart :")
    print("=" * 50)
    for index,item in enumerate(cart , start = 1) :
        print(f"{index}. {item}")
    print()
    remove_item_no = int(input("Enter item number to remove :"))
    print()
    if remove_item_no <= 0 or remove_item_no >  len(cart) :
        print("select a valid item")
    else :
        remove_item = cart[remove_item_no-1]
        print(f"{remove_item} removed from the cart")
        print()
        cart.remove(remove_item)
print("=" * 50)
print("                  SHOPEASY")
print("=" * 50)
print()

options = ["View Products", "View Cart", "Remove from cart" , "Exit"]

while True:

    for index, option in enumerate(options, start=1):
        print(f"{index}. {option}")

    print()
    choice = int(input("Enter your choice : "))
    print()

    if choice == 1:
        show_products()
        add_product()
        choose = input("Do you want to continue shopping (Yes/No) : ")
        print()

        while choose == "Yes":
            show_products()
            add_product()
            choose = input("Do you want to continue shopping (Yes/No) : ")
            print()
    elif choice == 2 :
        show_cart()
    elif choice == 3 :
        remove_item()
    elif choice == 4 :    
        print("Thank you for shopping!")    
        print("=" * 50)
        break