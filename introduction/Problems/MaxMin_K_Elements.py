#Minimum and Maximum K elements

tup = 5,20,78,3,2,6,8543

K = 3

#1
""" res = []
tup = list(sorted(tup))
for idx, val in enumerate(tup):
    if idx < K or idx > len(tup) - K - 1:
        res.append(val)
tup = tuple(res)
print(tup) """

#2
temp = list(sorted(tup))
#Sort list elements
tup = tuple(temp[:K] + temp[-K:])
#tup = tuple(temp[:K] + temp[len(temp)-K:])

print(tup)