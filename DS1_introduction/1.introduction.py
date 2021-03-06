'''
    如果 a+b+c=1000，且 a^2+b^2=c^2（a,b,c 为自然数），如何求出所有a、b、c可能的组合?
    a,b,c取值范围0-1000
'''
# import time
# start_time = time.time()
# for a in range(0,1001):
#     for b in range(0,1001):
#         for c in range(0,1001):
#             if a+b+c == 1000 and a**2+b**2 == c**2:
#                 print("a=%d,b=%d,c=%d"%(a,b,c))

# end_time = time.time()
# print("耗时%s"%(end_time-start_time))


#减少循环
# import time  
# start_time = time.time()

# for a in range(0,1001):
#     for b in range(0,1001):
#         c = 1000-a-b
#         if a**2+b**2 == c**2:
#             print("a=%d,b=%d,c=%d"%(a,b,c))

# end_time = time.time()
# print("耗时%s"%(end_time-start_time))






'''
    计算1-5000的和
    高斯算法
    普通算法
'''
# a = (1+5001)*5000/2
# print(a)

def get_sun(n):
    sum= 0
    for i in range(1,n):
        sum = sum+i
    return sum

def get_sum_gs(n):
    sum = n*(n+1)/2
    return sum