def indexing():
    my_string = "PluckPetalsPushDaisies"
    print(len(my_string))
    
    print(my_string[0])
    
    print(my_string[21])
    
    print(my_string[5]) 
    print(my_string[17])

    print(my_string[-22])
    print(my_string[-1])
    
def concact():
    a = "cat"
    b = "tail"
    a = a + b
    print(a)
    x = "age: " + str(18)
    print(x) # age: 18
     
def main():
    indexing()
    concact()
if __name__ == "__main__":
    main()