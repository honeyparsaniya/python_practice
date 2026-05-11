class Hospital:

    def hospital_info(self):

        self.h_name=input("enter hospital name=")
        self.c_name=input("enter city name=")

        print("\n---------HOSPITAL INFORMATION---------")
        print("Hospital name=",self.h_name)
        print("City         =",self.c_name)

class Doctor(Hospital):

    def Doctor_info(self):

        print("\nEnter doctor detail.")

        self.name=input("enter doctor name=")
        self.spel=input("enter doctor specialization=")
        self.d_fee=input("enter doctor fee=")

        print("\n---------Doctor Detail---------")
        print("Doctor Name   =",self.name)
        print("specialization=",self.spel)
        print("Doctor Fee    =",self.d_fee)

class patient(Hospital):

    def Patient_info(self):

        print("\nenter Patient detail")

        self.name=input("enter patient naem=")
        self.age=int(input("enter patient age="))
        self.disease=input("enter patient disease=")

        print("\n---------Patient Detail----------")
        print("Patient Name  :", self.name)
        print("Age           :", self.age)
        print("Disease       :", self.disease)

d=Doctor()

print("=====Doctor section=====")

d.hospital_info()
d.Doctor_info()

p=patient()

print("=====Patient section=====")

p.hospital_info()
p.Patient_info()