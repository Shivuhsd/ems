###Custom Functions

#Function to Generate OTP
import random
import string
def GenerateOTP():
    n = 6
    otp = "".join(random.choices(string.ascii_uppercase + string.digits, k=n))
    return otp