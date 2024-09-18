cart = []
def add_item (item, quantity):
    cart.append((item, quantity))

def print_cart():
    print("Cart Contents:")
    for item, quantity in cart:
        print(f"{item}: {quantity}")

def update_quantity(item, new_quantity):
    for i in range(len(cart)):
        if cart[i][0] == item:
            cart[i] = (item, new_quantity)
            print(f"Updated quantity of {item} to {new_quantity}")
            return
    print(f"{item} is not in the cart")


def remove_item(item):
    for i in range(len(cart)):
        if cart[i][0] == item:
            cart.pop(i)
            print(f"removed {item} from the cart")
            return
    print(f"{item} not in the cart")



# Add items to the cart
add_item("Apple", 2)
print_cart()
add_item("Banana", 3)
print_cart()
add_item("Orange", 1)
print_cart()

# Remove an item from the cart
remove_item("Banana")
print_cart()

# Update the quantity of an item in the cart
update_quantity("Apple", 4)
print_cart()