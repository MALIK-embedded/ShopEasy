product = input("Enter product name:")
price = float(input("Enter price:"))
quantity = int(input("Enter quantity:"))
gst = float(input("Enter GST:"))
subtotal = price * quantity
gst_amount = (subtotal * gst) / 100
final_bill = subtotal + gst_amount
print("=" * 50)
print("              SHOPEASY BILL")
print("=" * 50)
print(f"Product         : {product}")
print(f"Price           : ₹{price:.2f}")
print(f"Quantity        : {quantity}")
print(f"Subtotal        : ₹{subtotal:.2f}")
print(f"GST ({gst}%)      : ₹{gst_amount:.2f}")
print(f"Final Bill      : ₹{final_bill:.2f}" )
print()
if final_bill >= 50000 :
        print("---10% discount applied---")
        print()
        discount_percent = 10
        discount = (final_bill * discount_percent) / 100
        print(f"Discount       : ₹{discount:.2f}")
        pay_bill = final_bill - discount
        print(f"Payable Amount : ₹{pay_bill:.2f}")
else:
        print("---No discount applied---")
        print()
        print(f"Payable Amount : ₹{final_bill:.2f}")

print("=" * 50)