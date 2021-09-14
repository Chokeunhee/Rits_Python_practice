'''
Created on Jun 21, 2019
Display the fruits that can be eaten
@author: Chokeunhee
'''
dictionary = {"apple":"RINGO", "orange":"MIKAN", "grape":"BUDO"}
priceJ = {"RINGO":40, "MIKAN":20, "BUDO":30}
tray = ("grape", "orange", "apple", "orange", "apple", "grape", "apple")
priceE = {}
budget = 200

keys =dictionary.keys()
for k in keys:
    value = dictionary[k]
    price = priceJ[value]
    priceE[k] = price
print(priceE)

total = 0
i = 0
print("The length of list is", len(tray))
while i < len(tray) and total + priceE[tray[i]]  < budget :
    total += price
    print("I have", tray[i])
    i += 1
print("total price is", total)
