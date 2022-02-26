def spy_game(arr):
    first_zero = False
    second_zero = False
    has_seven = False

    for i in arr:
        if i == 0:
            if first_zero:
                second_zero = True
            else:
                first_zero = True
        if i == 7:
            if second_zero:
                has_seven = True
    return has_seven


nums = list(map(int,input().split()))

print(spy_game(nums))
