def net_amount(transaction_log):
    transactions = transaction_log.split()

    net_amount = 0

    for i in range(0, len(transactions), 2):
        transaction_type = transactions[i]
        transaction_amount = int(transactions[i+1])

        if transaction_type == "D":
            net_amount += transaction_amount
        elif transaction_type == "W":
            net_amount -= transaction_amount

    return net_amount

def main():
    transaction_log = input("Enter the transaction log: ")

    result = net_amount(transaction_log)

    print(result)

if __name__ == "__main__":
    main()

