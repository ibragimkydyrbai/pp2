def unique_elements(li: []) -> []:
    new_list = []

    for i in li:
        if i not in new_list:
            new_list.append(i)
    return new_list


li = list(map(int, input().split()))
print(unique_elements(li))
