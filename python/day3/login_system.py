print("=" * 50)
print("               WELCOME TO SHOPEASY")
print("=" * 50)
username = "Malik"
passkey = "Malik@123"
name = input("Enter Username : ")
password = input("Enter password : ")
if name == username and password == passkey :
    print()
    print("Login Successful!")
    print(f"Welcome Back, {name}")
elif name != username and password == passkey :
    print()
    print("Invalid Username.")
elif name == username and password != passkey :
    print()
    print("Incorrect Password.")
else :
    print()
    print("Invalid Username or Password.")
print("=" * 50)