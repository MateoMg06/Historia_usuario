
# Boolean values

yes = True
no = False


# Ask if there is another sale

def ask_another_sale():
    answer = input("Do you want to register another sale? (y/n): ").strip().lower()

    if answer == "y" or answer == "yes":
        return yes

    return no
