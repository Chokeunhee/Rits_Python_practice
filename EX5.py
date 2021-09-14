'''
Created on Jun 14, 2019
Exercise of strings
@author: Chokeunhee
'''

data = "Information System Science and Engineering"

def main():
    print(data.replace("System","Systems"))
    ver1 = data[0:11]
    print(ver1)
    ver2 = data[19:26]
    print(ver2)
    print("{0} of {1}".format(ver1,ver2))
    
if __name__ == "__main__":
    main()
    
