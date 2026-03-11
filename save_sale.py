
# Save the sale and update the total

def save_sale(sales_list, sale, total_amount):
    sales_list.append(sale)
    total_amount = total_amount + sale["subtotal"]
    return total_amount
