"""
1)if ValueError occure it means your ip is not valid.
2)NO SUBNETS and SPECIAL IPs Could be validated using this script!!!
MADE BY UMAR SOHAIL
"""

ip = str(input("enter IP address: "))

spliter = ip.split(".")
if not len(spliter) == 4: 
    raise ValueError
    

ip_address = ""

for i in spliter:
     con = int(i)
     if con > 255:
         raise ValueError
     else:
         string = str(con)
         ip_address += "%s."%(string)

print("this " + ip_address + "is valid")

         


