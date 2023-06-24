def find_pair(a,b,x):
    pairs = []
    set_b = set(b)
    for num in a:
        complement = x -num 
        if complement in set_b:
            pairs.append((num, complement))

    return pairs


A = [1, 2, 4, 5, 7]
B = [5, 6, 3, 4, 8]
X = 9

print(find_pair(A,B,X))