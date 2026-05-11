#parent class
class area:
    def  shape(self):
        print("SELECT SHAPE")
        print("1.circle")
        print("2.squre")
        print("3.rectangle")

        self.choice=int(input("enter your choice="))
        
class calculate(area):
    

    def cal_area(self):
         if self.choice==1:
             
            self.r=float(input("enter radius="))
            print("radius of circle=",3.14*self.r*self.r)

         elif self.choice==2:
             
             self.l=int(input("enter length="))
             print("area of squre=",self.l*self.l)

         elif self.choice==3:
             
             self.l=int(input("enter length="))
             self.w=int(input("enter width="))

             print("area of rectangle=",self.l*self.w)
            
         else :
             print("enter valid choice")

print("===FIND SHAPE===")

C=calculate()
C.shape()
C.cal_area()