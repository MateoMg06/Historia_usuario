
# Ask if there is another sale

def ask_another_sale():
    answer_ok = False
    while answer_ok == False:
        answer = input("Do you want to register another sale? (y/n): ").strip().lower()

        if answer == "y" or answer == "yes":
            return True
        elif answer == "n" or answer == "no":
            return False
        else:
            print("Write only yes or no")
            answer_ok = False
