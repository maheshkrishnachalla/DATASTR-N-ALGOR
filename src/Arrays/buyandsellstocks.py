"""
Stock Buy and Sell - Max one Transaction Allowed
Input: prices[] = {7, 10, 1, 3, 6, 9, 2}
Output: 8
Explanation: Buy for price 1 and sell for price 9.

Input: prices[] = {7, 6, 4, 3, 1}
Output: 0
Explanation: Since the array is sorted in decreasing order, 0 profit can be made without making any transaction.

Input: prices[] = {1, 3, 6, 9, 11}
Output: 10
Explanation: Since the array is sorted in increasing order,
we can make maximum profit by buying at price[0] and selling at price[n-1]
"""


def buyandsellstocks(arr):
    max_sum  = 0
    n = len(arr)
    i = 0
    p1 = arr[0]
    while i < n-1:
        p2 = arr[i+1]
        if p2 < p1:
            p1 = p2
        if max_sum < (p2 - p1):
            max_sum = p2 -p1
        i = i+1
    return max_sum


def maxProfit(prices):
    minSoFar = prices[0]
    res = 0

    # Update the minimum value seen so far
    # if we see smaller
    for i in range(1, len(prices)):
        minSoFar = min(minSoFar, prices[i])

        # Update result if we get more profit
        res = max(res, prices[i] - minSoFar)

    return res



arr = [7, 10, 1, 3, 6, 9, 2]
#arr = [7, 6, 4, 3, 1]
#arr = [1, 3, 6, 9, 11]
result  =buyandsellstocks(arr=arr)
result2 = maxProfit(prices=arr)
print(result)
print(result2)


