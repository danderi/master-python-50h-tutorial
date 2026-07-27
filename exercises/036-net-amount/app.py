# Your code here
def net_amount(log):
    amount = 0
    transactions = log.split()
    
    for i in range(0, len(transactions), 2):
        print(i)
        action = transactions[i]
        value = int(transactions[i + 1])

        if action == "D":
            amount += value
        elif action == "W":
            amount -= value

    return amount
print(net_amount("D 300 D 300 W 200 D 100"))  # Output: 150