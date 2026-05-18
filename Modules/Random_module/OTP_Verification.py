import random

mobile=input("enter mobile number:")

otp=random.randint(1000,9999)

print("Genrated OTP=",otp)

user_otp=int(input("enter OTP here="))

if user_otp==otp:
    print("Login successfull")
else:
    print("Invalid OTP")