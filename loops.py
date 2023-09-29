def count_down(number):
    sum = 0
    while number >= 0:
        sum = sum + number
        print(number)
        number -= 1
    print("sum:", sum)

def count_up(number1):
    current = 0
    sum = 0
    while current <= number1:
        sum <= current
        print(current)
        current += 1
    print("sum1", sum)
   
def sum_of_odds():
    count = 0
    while True:
        num = int(input("input a number: "))
        if num == 0:
            break
        elif num % 2 == 0:
            continue
        sum = sum + num
        return sum
        
def print_range(a_range):
    index = 0
    while index < len(a_range):
        print(a_range[index], end=" ")
    index = 1
    print()

def print_range_4(a_range):
    index = 0
    for number in a_range:
        print(number, end=" ")
    index = 1
    print() 

def main():
    count_down(5)
    count_up(4)
    print_range(range(0, 11))
    print_range(range(0, 21, 2))
    print_range(range(5, 16, 2))
    print_range(range(10, -1, -1))

    print_range_4(range(0, 11))
    print_range_4(range(0, 21, 2))
    print_range_4(range(5, 16, 2))
    print_range_4(range(10, -1, -1))
if __name__ == "__main__":
    main()

