cart = {}

GST_RATE = 18

while True:

    print("\n======================================")
    print("       ONLINE SHOPPING CART")
    print("======================================")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. Change Quantity")
    print("4. Display Cart")
    print("5. Apply Discount")
    print("6. Display Final Bill")
    print("7. Exit")
    print("======================================")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("\n---------- ADD PRODUCT ----------")

        product = input("Enter product name: ").strip()

        if product == "":
            print("Product name cannot be empty.")
            continue

        price = float(input("Enter product price: "))
        quantity = int(input("Enter quantity: "))

        if price <= 0:
            print("Price must be greater than 0.")
            continue

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        if product in cart:
            cart[product]["quantity"] += quantity
            print("Product quantity updated.")
        else:
            cart[product] = {
                "price": price,
                "quantity": quantity
            }
            print("Product added successfully.")

    elif choice == "2":

        print("\n---------- REMOVE PRODUCT ----------")

        if not cart:
            print("Shopping cart is empty.")
            continue

        product = input("Enter product name to remove: ").strip()

        if product in cart:
            del cart[product]
            print("Product removed successfully.")
        else:
            print("Product not found in cart.")

    elif choice == "3":

        print("\n---------- CHANGE QUANTITY ----------")

        if not cart:
            print("Shopping cart is empty.")
            continue

        product = input("Enter product name: ").strip()

        if product in cart:

            quantity = int(input("Enter new quantity: "))

            if quantity > 0:
                cart[product]["quantity"] = quantity
                print("Quantity changed successfully.")
            else:
                del cart[product]
                print("Product removed from cart.")

        else:
            print("Product not found in cart.")

    elif choice == "4":

        print("\n---------- SHOPPING CART ----------")

        if not cart:
            print("Shopping cart is empty.")
            continue

        subtotal = 0

        print("-" * 70)
        print(f"{'Product':<20}{'Price':<15}{'Quantity':<15}{'Total':<15}")
        print("-" * 70)

        for product, details in cart.items():

            price = details["price"]
            quantity = details["quantity"]
            total = price * quantity

            subtotal += total

            print(
                f"{product:<20}"
                f"₹{price:<14.2f}"
                f"{quantity:<15}"
                f"₹{total:<14.2f}"
            )

        print("-" * 70)
        print(f"Subtotal: ₹{subtotal:.2f}")

    elif choice == "5":

        print("\n---------- APPLY DISCOUNT ----------")

        if not cart:
            print("Shopping cart is empty.")
            continue

        discount = float(input("Enter discount percentage: "))

        if discount < 0 or discount > 100:
            print("Discount must be between 0 and 100.")
            continue

        subtotal = 0

        for product, details in cart.items():
            subtotal += details["price"] * details["quantity"]

        discount_amount = subtotal * discount / 100
        amount_after_discount = subtotal - discount_amount

        print(f"Subtotal: ₹{subtotal:.2f}")
        print(f"Discount: {discount}%")
        print(f"Discount Amount: ₹{discount_amount:.2f}")
        print(f"Amount After Discount: ₹{amount_after_discount:.2f}")

    elif choice == "6":

        print("\n======================================")
        print("             FINAL BILL")
        print("======================================")

        if not cart:
            print("Shopping cart is empty.")
            continue

        discount = float(input("Enter discount percentage: "))

        if discount < 0 or discount > 100:
            print("Discount must be between 0 and 100.")
            continue

        subtotal = 0

        for product, details in cart.items():

            price = details["price"]
            quantity = details["quantity"]
            total = price * quantity

            subtotal += total

        discount_amount = subtotal * discount / 100

        amount_after_discount = subtotal - discount_amount

        gst = amount_after_discount * GST_RATE / 100

        final_amount = amount_after_discount + gst

        print("-" * 70)
        print(f"{'Product':<20}{'Price':<15}{'Qty':<10}{'Total':<15}")
        print("-" * 70)

        for product, details in cart.items():

            price = details["price"]
            quantity = details["quantity"]
            total = price * quantity

            print(
                f"{product:<20}"
                f"₹{price:<14.2f}"
                f"{quantity:<10}"
                f"₹{total:<14.2f}"
            )

        print("-" * 70)
        print(f"Subtotal              : ₹{subtotal:.2f}")
        print(f"Discount ({discount}%)      : ₹{discount_amount:.2f}")
        print(f"After Discount        : ₹{amount_after_discount:.2f}")
        print(f"GST ({GST_RATE}%)             : ₹{gst:.2f}")
        print("-" * 70)
        print(f"FINAL BILL AMOUNT     : ₹{final_amount:.2f}")
        print("======================================")

    elif choice == "7":

        print("\nThank you for shopping!")
        print("Visit again!")
        break

    else:

        print("\nInvalid choice.")
        print("Please enter a number from 1 to 7.")