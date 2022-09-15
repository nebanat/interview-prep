# possible change: 1p, 2p, 5p, 10p, 20p, 50p, 1pound, 2pound

# for the set coins above what is the minimum number of coins to make 24p
# 24p -> 20p + 2p + 2p = 3 coins
# 1.63 = 1pound + 50p + 10p + 2p + 1p = 5 coins

# algorithm walkthrough
# 1. sort the coins in descending order
# 2. start with the largest coin
# 3. if the coin is less than the target amount, subtract the coin from the target amount
    # 
# 4. if the coin is greater than the target amount, move to the next coin
# 5. repeat until the target amount is 0

def make_change(target_amount):
    denominations = [200, 100, 50, 20, 10, 5, 2, 1]
    values = []
    coin_count = 0

    for coin in denominations:
        while target_amount >= coin:
            target_amount -= coin
            values.append(coin)
            coin_count += 1
    return coin_count, values


if __name__ == '__main__':
    print(make_change(163))
    print(make_change(24))