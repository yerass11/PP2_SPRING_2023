"""
   * 
  * *    
 *   *   
*     * 
 *   *   
  * *     
   *     

"""
n = 7
l = 3
r = 3
while True:
    if l > 0:
        for i in range(n+1):
            for j in range(n+1):
                if (j == l or j == r):
                    print('*', end = "")
                else:
                    print(" ", end = "")
                l -= 1
                r += 1
    
    else:
        for i in range(n+1):
            for j in range(n+1):
                if (j == l or j == r):
                    print('*', end = "")
                else:
                    print(" ", end = "")
                l += 1
                r -= 1
                if (l == 4):
                    break


# n = 7
# def rhombus(n):
#     for i in range(n + 1):
#         for j in range(2 * n - 1):
#             if j >= n - i and j <= n + i:
#                 print("*", end="")
#             else:
#                 print(" ", end="")
#         print()
# rhombus(n)

# n = int(input())
# k = n / 2
# for i in range(k+1):
#     for j in range(0, n-i):
#         print(end=" ")
#     for j in range(0, i):
#         print('*', end = " ")
#     print()

# n=int(input())
# k = n//2
# for i in range(k+1):
#     if i == 0:
#         print(" "*(k-i), '*', sep='', end='\n')
#     else:
#         j = list(range(1,n-1,2))[i-1]
#         print(" "*(k-i), '*', " "*j, '*', sep='', end='\n')
# for i in range(k-1,-1,-1):
#     if i > 0:
#         j = list(range(n-k+(n-9)//2,-1,-2))[k-i-1]
#         print(" "*(k-i), '*', " "*j, '*', sep='', end='\n')
#     else:
#         print(" "*(k-i), '*', sep='', end='\n')