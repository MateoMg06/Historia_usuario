
def show_summary(sales_list, total_amount):
    print("SUMMARY")

    if sales_list == []:
        print("No sales")
        print("Total", 0)
    else:
        number = 1
        for sale in sales_list:
            print("Sale", number)
            print("Product", sale["name"])
            print("Price", sale["price"])
            print("Quantity", sale["quantity"])
            print("Subtotal", sale["subtotal"])
            number = number + 1

        print("Total", total_amount)
