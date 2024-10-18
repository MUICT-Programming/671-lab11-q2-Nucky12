# YOUR CODE HERE
def summation(lst1, lst2):
    updated_list = [a + b for a, b in zip(lst1, lst2)]
    return updated_list

def find_min_max(updated_list):
    min_value = min(updated_list)
    max_value = max(updated_list)
    return min_value, max_value

n = int(input())

lst1 = []
for _ in range(n):
    value = int(input())
    lst1.append(value)

lst2 = []
for _ in range(n):
    value = int(input())
    lst2.append(value)
    
updated_list = summation(lst1, lst2)
print(updated_list)
    
min_max = find_min_max(updated_list)
print(min_max)
