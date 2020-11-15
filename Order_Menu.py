menu = {1: 18.00, 2: 25.00, 3: 35.00}


def take():
    x = int(input("Enter Item No : "))
    y = int(input("Enter Quantity : "))
    if x in range(1, 4) and y in range(1, 100):
        # print(type(menu[x] * y))
        return menu[x] * y
    else:
        return "Invalid Input"


tot = take()

# if isinstance(tot, str) --- raise an exception with "Invalid Input"

# else routing through while for further inputs

# exception case - 1 : If input() other than Y / y --- message "End of order"

# exception case - 2 : If Item.No or Count is not available --- message "Invalid Input"


while True:

    if isinstance(tot, str):
        break
    else:
        k = input("Do you want another Item...  : ")
        if k not in ['Y', 'y']:
            break
        elif k in ['Y', 'y']:
            order = take()
            if isinstance(order, float):
                tot += order
            else:
                break

print("Order Total :", tot)
