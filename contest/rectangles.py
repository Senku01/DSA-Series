def rectanglle(sides):
    count =0
    freq={}
    for side in sides:
        ratio = side[0] / side[1]
        freq[ratio] = freq.get(ratio , 0) +1
    for ratio in freq:
        if freq[ratio] >1:
            count += (freq[ratio] * (freq[ratio] -1)) //2
    return count

sides = [(2, 4), (3, 6), (1, 2), (4, 8), (2, 4)]
result = rectanglle(sides)
print(result)
