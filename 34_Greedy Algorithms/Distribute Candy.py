"""
N children are standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum number of candies you must give?
"""

#A = [1, 5, 2, 1]
A= [3,4,1,5,2,1,7,2]

def min_candies(ratings):
    n = len(ratings)
    candies = [1]*n
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1]+1
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i],candies[i+1]+1)
    return sum(candies)

print(f'total candies distributed = {min_candies(A)}')