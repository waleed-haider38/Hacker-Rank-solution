def cutTheSticks(arr):
    result = []
    while arr:   # jab tak list empty na ho
        result.append(len(arr))   # sticks ka count save karo
        min_value = min(arr)      # sabse chhoti stick ki length
        arr = [x - min_value for x in arr if x - min_value > 0]  # minus aur zero hatao
    return result


# Example Run
arr = [5, 4, 4, 2, 2, 8]
print(cutTheSticks(arr))   # Output: [6, 4, 2, 1]
