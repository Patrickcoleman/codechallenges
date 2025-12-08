import random


hops_taken = []
destination = 2

for i in range(10**8):
    distance = 0
    hops = 0
    while distance < destination:
        distance += random.random()
        hops += 1
    hops_taken.append(hops)

total_hops = sum(hops_taken)

#print(hops_taken)
print(total_hops/len(hops_taken))


#### Yeah this is above my mathematical paygrage