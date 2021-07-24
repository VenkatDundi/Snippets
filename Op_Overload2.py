class Order():
    def __init__(self, cart, customer) -> None:
        self.cart = list(cart)
        self.customer = customer

    def __len__(self):
        return len([i for i in self.cart if i[0] == 'P'])               # Should only return an "Integer" as it refers len()
    
    def __str__(self) -> str:
        return " * ".join([i for i in self.cart if i[0] == 'P'])        # Should only return a "String" as it refers str()

ob1 = Order(('Pomogranate', 'Pineapple', 'Peach', 'Watermelon'), 'Emily')

print(len(ob1))

print(str(ob1))