class check:

    def num(self):
        print("---check number even/odd---")
        num=int(input("\nenter number="))

        if num%2==0:
            print("\nnumber is even!")
        else:
            print("\nnumber is odd!")

c1=check()
c1.num()