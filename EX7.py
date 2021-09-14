'''
Created on Jun 28, 2019
Counting random numbers
@author: Chokeunhee
'''
import random as rand
dictionary = {}

def countRandomNumber():
    for num in range(10):
        dictionary[str(num)] = 0
    print(dictionary)
    
    with open("data.txt",'w') as f:
        for no in range(100):
            f.write("{}\n".format(rand.randint(0,9)))
       
    with open("data.txt", 'r')as f:
        for line in f:
            item = line[:-1]
            num = dictionary[item]
            dictionary[item] = num + 1
                  
    for key in dictionary.keys():
        print("the number of {} is".format(key),dictionary[key])
    
if __name__ == "__main__":
    countRandomNumber()
            