def counting_sort(lst: list[int]) -> list[int]:
    if not lst:
        return []
    
    max_element = max(lst)
    result_list = []

    counting_list = [0 for i in range(100)]

    for element in lst:
        counting_list[element] += 1

    for i in range(max_element + 1):
        result_list += [i] * counting_list[i]
    
    return counting_list
    
k = int(input())
lst = []

for _ in range(k):
    num, string = input().split()
    lst.append(int(num))

lst = counting_sort(lst)
count = 0
for i in lst:
    count += i
    print(count, end = " ")