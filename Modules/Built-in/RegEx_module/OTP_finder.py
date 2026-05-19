import re

text = input("Enter message: ")

otp = re.search(r"\d{4,6}", text)

if otp:
    print("OTP Found:", otp.group())
else:
    print("No OTP found")