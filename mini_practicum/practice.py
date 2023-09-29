import random

GLOBAL1 = 100
GLOBAL2 = -100

def absolute_difference(a, b):
    difference = a - b
    return str(abs(difference))
    
def main():
    a = random.randrange(GLOBAL2, GLOBAL1)
    b = random.randrange(GLOBAL2, GLOBAL1)
    #a = int(input("insert integer: "))
    #b = int(input("insert another integer: "))
    print("a=",a, "b=",b, "absolute difference=",absolute_difference(a, b))
if __name__ == "__main__":
    main()
    