class Order:
    def __init__(self , items , price):
        self.items = items
        self.price = price
    
    def __gt__(self , order2):
        return self.price > order2.price
        

order1= Order("Beyblade" , 250)






order2= Order("Beyblade" , 150)





greater = order1>order2

print(greater)