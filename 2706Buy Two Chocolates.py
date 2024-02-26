def Solution(prices,money):
    return money - sum(sorted(prices)[0:2]) if money - sum(sorted(prices)[0:2])>=0 else money
prices = [1,2,2]
money = 3
print(Solution(prices, money))