class fooddetails:
    def __init__(self):
        self.foodcost=0

    def calculate(self,brf,luf,dif,d):
        if brf==1:
            self.foodcost = self.foodcost + 150
        if luf==1:
            self.foodcost = self.foodcost + 500
        if dif==1:
            self.foodcost = self.foodcost + 300
        else:
            print("Wrong Choice..!!")
        self.foodcost=self.foodcost*d
        print("Total Food Bill: ", self.foodcost)
        return self.foodcost


