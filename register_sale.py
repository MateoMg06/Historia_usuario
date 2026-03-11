
# Ask the user for sale data

def register_sale():
    name = input("Product name: ")

    price_ok = False
    while price_ok == False:
        try:
            price = float(input("Product price: "))
            price_ok = True
        except:
            print("Write a number")

    quantity_ok = False
    while quantity_ok == False:
        try:
            quantity = int(input("Quantity: "))
            quantity_ok = True
        except:
            print("Write a whole number")

    subtotal = price * quantity

    sale = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "subtotal": subtotal,
    }

    return sale
