class items: 
    def __init__(self, food, Pounds_amount):
        self.food = food 
        self.Pounds_amount = Pounds_amount
        self.unitprice = 0
        self.totalprice= 0
       
    def __priceList(self):
        if self.food is "Dry Cured Iberian Ham":
            self.unitprice = 177.80 
        
        elif self.food is "Wagyu Steaks":
            self.unitprice = 450.00
        
        elif self.food is "Matsutake Mushrooms":
            self.unitprice = 272.00

        elif self.food is "Kopi Luwak Coffee":
            self.unitprice = 306.50
    
        elif self.food is "Moose Cheese":
            self.unitprice = 487.20

        elif self.food is "White Truffles":
            self.unitprice = 3600.00
    
        elif self.food is "Blue Fin Tuna":
            self.unitprice = 3603.00

        elif self.food is "Le Bonnotte Potatoes":
            self.unitprice = 270.81
        
        else: 
            print("try again")
        
    def calculateCostVD (self):
        self.totalprice = self.Pounds_amount * self.unitprice
        return self.totalprice
    
    def getfood_name(self):
        return self.food
    
    def getamount_pounds(self):
        return self.Pounds_amount
    
    def getstandardprice(self):
        return self.unitprice    
    
    def getcalculatedprice(self):
        return self.totalprice

    def __str__(self):
        return f"item: {self.food}\nAmount ordered: {self.Pounds_amount:.1f} pounds\n"\
               f"Price per pound: ${self.unitprice:.2f}\n"\
               f"Price of order: ${self.totalprice:.2f}\n"\

