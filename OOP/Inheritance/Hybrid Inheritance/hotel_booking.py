class hotel:

    def customer(self):

        self.name=input("enter customer name=")

class room(hotel):

    def room_detail(self):

        print("\nAC room")
        print("non-AC room")

        choice=int(input("enter choice="))
        day=int(input("enter days="))

        if choice==1:

            self.room_bill=3000*day
            self.room_type="AC room"

        else:

            self.room_bill=1500*day
            self.room_type="non-AC room"

class food(hotel):

    def food_bill(self):
        self.food=int(input("enter food bill="))

class final_bill(room,food):

     def total_bill(self):

        subtotal = self.room_bill + self.food
        gst = subtotal * 0.18
        total = subtotal + gst

        print("\n===== Hotel Bill =====")
        print("Customer Name :", self.name)
        print("Room Type     :", self.room_type)
        print("Room Bill     :", self.room_bill)
        print("Food Bill     :", self.food)
        print("GST Amount    :", gst)
        print("Final Bill    :", total)

b=final_bill()

b.customer()
b.room_detail()
b.food_bill()
b.total_bill()