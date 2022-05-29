import heapq

number_list = [2,5,70,40,35,18,21,90,34]

# print(dir(heapq))
print(heapq.nlargest(2, number_list), ' are the two largest number in he list.')
print(heapq.nsmallest(2, number_list), ' are the two smallest number in he list.')