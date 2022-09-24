class roomdetails:
    #Room cost
    def __init__(self):
        self.sum=0
    def roomrent(self,room,AC,number):

        # print ("We have the following rooms for you:-")

        # print ("1.  Super Premium Room---->4000")

        # print ("2.  Super Deluxe Room---->1500")

        # print ("3.  Deluxe Room---->1300")

        # print ("4.  Dormitory---->500")

        # AC= input("Do you want A/C to be on? if not type 'no' else 'yes': ")
        ac_charge= 300

        # n=int(input("For How Many Nights Did You Stay:"))


        if(room==1):
            if AC == "yes":
                self.sum=4000*number
            elif AC == "no":
                self.sum= (4000 - ac_charge)*number

        elif (room==2):

            print ("you have choose Super Deluxe Room")
            if AC == "yes":
                self.sum=1500*number
            elif AC == "no":
                self.sum= (1500- ac_charge)*number

        elif (room==3):

            print ("you have choose Deluxe Room")
            if AC == "yes":
                self.sum=1300*number
            elif AC == "no":
                self.sum = (1300 - ac_charge)*number

        elif (room==4):
            print ("you have choose Dormitory")
            if AC == "yes":
                self.sum=500*number
            elif AC == "no":
                self.sum = (500 - ac_charge)*number

        else:

            print ("please choose a room")

        print ("your chosen room rent is =",self.sum, "\n")
        return self.sum
        
