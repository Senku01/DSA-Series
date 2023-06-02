# a=int(input())
# b= int(input())
# #TC = O(log phive m(a,b))
# Euclidean Algo to find gcd
# def gcd(a,b):
#     while (a>0 and b >0):
#         if (a>b):
#             a=a % b
#         else:
#             b= b % a
#         if (a==0):
#             return b
#         else:
#             return a
#     def lcm(a,b):
#         return (a * b)//gcd(a,b)
#     gcd_res = gcd(a,b)
#     lcm_res = lcm(a,b)

#     return gcd_res, lcm_res
 
# print(gcd(a,b))

def gcd_lcm(a, b):
    def gcd(x, y):
        while y != 0:
            x, y = y, x % y
        return x

    def lcm(x, y):
        return (x * y) // gcd(x, y)

    gcd_result = gcd(a, b)
    lcm_result = lcm(a, b)

    return gcd_result, lcm_result

# Example usage
num1 = 52
num2 = 10

gcd_result, lcm_result = gcd_lcm(num1, num2)

print("GCD:", gcd_result)
print("LCM:", lcm_result)
