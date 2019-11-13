
# Sample Input 
# 5
# 100 150
# 60 50 60 70 10

demand = []

n  = int(input())
# P = int(input())
# Q = int(input())
line = input()
lines = line.split()
P = int(lines[0])
Q = int(lines[1])

line = input()
lines = line.split()

demand.append(0)
for i in lines:
    # temp = int(input())
    demand.append(int(i))

cost = 0.0
currStock = 115
daysToReStock = -1

for day in range(1,n+1):
    # check if stock arrives this morning
    if(daysToReStock == 0):
        daysToReStock = -1
        currStock += Q

    #if enough items are available
    if(currStock >= demand[day]):
        currStock -= demand[day]

    else:
        outOfStock = demand[day] - currStock
        currStock = 0
        # add 18 Rs for each out of stock order
        cost += 18 * outOfStock * 1.0

    # if currStock <= P and no orders pending, order items.
    if(currStock <= P and daysToReStock == -1):
        daysToReStock = 3
        cost += 75.0

    # for every stock in inventory, add 0.75 Rs
    cost += currStock * 0.75

    # decrease daysToReStock if > 0
    if(daysToReStock > 0):
        daysToReStock-=1
if(cost-int(cost)<0.01):
    print(int(cost))
else:
    print("{0:0.1f}".format(cost))
