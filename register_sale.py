
def register_sale():
    name = input("Product name: ")
    price = float(input("Product price: "))
    quantity = int(input("Quantity: "))
    subtotal = price * quantity

    sale = {
        "name": name,
        "price": price,
        "quantity": quantity,
        "subtotal": subtotal,
    }

    return sale
