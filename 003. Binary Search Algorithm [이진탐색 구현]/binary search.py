def binary_search(element, some_list):
    
    while True:
        mid = (len(some_list)-1) // 2
        if some_list[mid] == element:
            return mid
        elif some_list[mid] > element:
            some_list = some_list[0:(mid-1)]
        elif some_list[mid] < element:
            some_list = some_list[(mid+1):(len(some_list)-1)]



print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))
