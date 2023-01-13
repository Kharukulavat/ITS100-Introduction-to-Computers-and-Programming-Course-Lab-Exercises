#ITS100 Lecture3 Libraries Lab3.7
import random as r
a = str(r.randint(8,9))
b = str(r.randint(6,7))
c = str(r.randint(4,5))
d =str(r.randint(2,3))
e =str(r.randint(0,1))
OTP = a+b+c+d+e
print("Your OTP is %s. This password will be expired within 5 minutes."%OTP)