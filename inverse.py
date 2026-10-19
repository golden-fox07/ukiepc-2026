import math

n = int(input())
#k = math.gcd(6,12)
#print(k)
# k = 2

# def Eq_a(n, k):
#     a = k + n
#     return a

# def Eq_b(1,n):
#     b = n + (n^2 // k)
#     return b


# print(Eq_a(n, k))
# print(Eq_b(n, k))

# k = prime factor
# while True:

# prime number 
# k=math.gcd(n)
# print(k)


def find_pairs(n):
    pairs=[]
    for a in range(n+1,2*n+1):
        if (a*n)%(a-n)==0:
            b=(a*n)//(a-n)
            pairs.append((a,b))
    # print(pairs)
    return pairs

pairs = find_pairs(n)

def min_sum(find_pairs):
    sums = []
    # print(find_pairs[0][0])
    for i in range(len(find_pairs)):
        a = find_pairs[i][0]
        b = find_pairs[i][1]
        if a != b:
            sums.append(a+b)

    # Find min
    min_sum = sums[0]
    for i in range(len(sums)):
        if sums[i] < min_sum:
            min_sum = sums[i]

    # print(min_sum)

    for i in range(len(find_pairs)):
        a = find_pairs[i][0]
        b = find_pairs[i][1]
        if a+b == min_sum:
            print(a, b)

min_sum(pairs)


# print(min(find_pairs(n)))


   


