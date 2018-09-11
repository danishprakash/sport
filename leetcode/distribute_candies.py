def distributeCandies(candies):
    return min(len(candies)/2, len(set(candies)))
ls = [int(x) for x in input().split()]
print(distributeCandies(ls))
