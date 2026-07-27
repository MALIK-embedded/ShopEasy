products = ["Laptop" , "Phone" , "Keyboard" , "Mouse"]
cart = []
print("=" * 50)
print("               Welcome to SHOPEASY")
print("=" * 50)
print()
print("Available products :")
print()
print(f"1.{products[0]}")
print(f"2.{products[1]}")
print(f"3.{products[2]}")
print(f"4.{products[3]}")
print()
product = int(input("Enter the product :"))
if product <= 0 or product > len(products) :
    print("Invalid product Number!")
else :
    print(f"✓ {products[product-1]} added to cart!")
    selected_product = products[product-1]
    cart.append(selected_product)
    print()
    opinion = input("Do you want to continue shopping (Yes/No) :")
    print()
    while opinion == "Yes" :
        print("Available products :")
        print()
        print(f"1.{products[0]}")
        print(f"2.{products[1]}")
        print(f"3.{products[2]}")
        print(f"4.{products[3]}")
        print()
        product = int(input("Enter the product :"))
        if product <= 0 or product > len(products) :
            print("Invalid product Number!")
            print()
            opinion = input("Do you want to continue shopping (Yes/No) :")
        else :
            print(f"✓ {products[product-1]} added to cart!")
            print()
            selected_product = products[product-1]
            cart.append(selected_product)
            opinion = input("Do you want to continue shopping (Yes/No) :")
print("=" * 50)
print("Shopping cart :")
print()
cart_item = 1
while cart_item <= len(cart) :
    print(f"{cart_item}.{cart[cart_item-1]}")
    cart_item = cart_item+1
print()
Total_items = len(cart)
print(f"Total Items : {Total_items}")
print("=" * 50)
            
            