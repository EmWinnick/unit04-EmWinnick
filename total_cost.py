def calculate_total_cost(quantity):
    if 1 <= quantity <= 9:
        cost_per_item = 50
    elif 10 <= quantity <= 19:
        cost_per_item = 45
    elif 20 <= quantity <= 29:
        cost_per_item = 38
    else:
        cost_per_item = 32
    total_cost = quantity * cost_per_item
    return total_cost

def main():
    while True:
        quantity = int(input("enter an integer: "))
        if quantity <= 0:
            break
        total_cost = calculate_total_cost(quantity)
        print("Total cost: ", total_cost)
if __name__ == "__main__":
    main()
        