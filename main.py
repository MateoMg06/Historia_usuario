from initialize import initialize_sales_list
from register_sale import register_sale
from save_sale import save_sale
from another_sale import ask_another_sale
from show_summary import show_summary


def main():
    sales_list = initialize_sales_list()
    total_amount = 0

    yes = True
    while yes:
        sale = register_sale()
        total_amount = save_sale(sales_list, sale, total_amount)
        yes = ask_another_sale()

    show_summary(sales_list, total_amount)


main()
