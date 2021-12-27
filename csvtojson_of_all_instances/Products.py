############################
###csv dosyasında oluşturacağım nesneleri verdim
###dışardan aldığım verilerle nesneler oluşturdum
###bu nesnelerin hepsinin price bilgisinde %20 indirim uyguladım
###nesneleri json olarak output aldım.
############################

import csv
import json
class Product:
    payment_rate=0.8 #class attribute
    productlist=[]  #to hold all my product in one list 
    def __init__(self, name: str, price: float, quantity=0) -> None:
        #Run validations to the received args
        assert price>0, "price should be greater than zero" #some assertions for validation
        assert quantity>=0, "quantity should not be less than zero"
        
        #assigning values to object
        self.name=name
        self.price=price
        self.quantity=quantity
        Product.productlist.append(self)    #add each created instance to product list

    def calculate_total_price(self):
        return self.quantity*self.price

    def apply_discount(self):
        self.price=self.price*self.payment_rate
    
    # def __repr__(self) -> str:
    #     return f"[name:'{self.name}', price: {self.price}, quantity: {self.quantity}]"
    
    def toJSON(self):   #got this code piece from stackoverflow
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)
    
with open('csvtojson_of_all_instances/products.csv') as csv_file:
    csv_reader = list(csv.reader(csv_file, delimiter=','))
    for item in csv_reader[1:]:
        myprod=Product(item[0],int(item[1]),int(item[2]))

for elem in Product.productlist:
    Product.apply_discount(elem)
    


with open("csvtojson_of_all_instances/output.json", "w") as outfile:
    outfile.write(Product.toJSON(Product.productlist))  #converting list of my objects to json format
    
    
    



