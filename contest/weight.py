def blocks(w):
    # counter = 0
    # while w >0:
    #     if w > 4:
    #         w -=4
    #     else:
    #         w -= w
    #     counter +=1
    # return counter
    # large = 4
    # comb = w // large
    # if w % large !=0:
    #     comb += 1 
    # return com
    count = 0 
    while w > 0:
        w &= (w -1)
        count +=1
    return count

print(blocks(12))