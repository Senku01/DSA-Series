def gather(n,arr):
    # min_cost = float('inf')
    # for k in range(n):
    #     total =0 
    #     for i in range(n):
    #         distance = abs(i-k)
    #         total += arr[i] * distance
    #     min_cost = min(min_cost ,total)
    # return min_cost
    total_cost = sum(arr)  # Calculate the initial total cost
    
    left_sum = 0  # Initialize the left partial sum
    right_sum = total_cost  # Initialize the right partial sum
    
    min_cost = float('inf')  # Initialize the minimum cost with a large value
    
    for k in range(n):
        if k > 0:
            left_sum += arr[k-1]
            right_sum -= arr[k-1]
        
        cost = left_sum * k + right_sum * (n - k - 1)
        min_cost = min(min_cost, cost)
    
    return min_cost
n= 5
arr=[1, 5, 4, 2, 10]
print(gather(n, arr))