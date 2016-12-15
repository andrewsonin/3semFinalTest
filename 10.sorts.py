from random import randint, choice, shuffle


def bogo_sort():
    A = list(range(1, 5))
    shuffle(A)
    while A != sorted(A):
        shuffle(A)
    print(A)
bogo_sort()
'''O(n*n!)'''

'''Квадратичные сортировки'''
def insertion_sort(A):
    for i in range(1, len(A)):
        tmp = A[i]
        k = i-1
        while k >= 0 and A[k] > tmp:
            A[k+1] = A[k]
            k -= 1
        A[k+1] = tmp
    return A
A = [4, 5, 6, 3, 4, 4]
print(insertion_sort(A))
'''Вставка элемента в отсортированный подмассив [:i]'''


def choice_sort(A):
    for i in range(len(A)-1):
        for k in range(i+1, len(A)):
            if A[k] < A[i]:
                A[i], A[k] = A[k], A[i]
    return A
print(choice_sort([0, 1, 2, 3, 2]))
'''Поиск минимума в подмассиве [i:]'''


def bubble_sort(A):
    for k in range(1, len(A)):
        for i in range(len(A) - k):
            if A[i] > A[i+1]:
                A[i+1], A[i] = A[i], A[i+1]
    return A
'''Поиск максимума в подмассиве [:i-k]'''


def fool_sort(A):
    i, N = 0, len(A)
    while i < N - 1:
        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
            i = 0
        else:
            i += 1
    return A
print(fool_sort([555, 33, 223, 3, 0, 1, 2, 3, 2]))
'''Перестановка элементов с возвращением к началу при каждой перестановке. Таким образом каждый элемент будет
сортироваться за O(N**2), все -- за O(N**3).'''
'''Кубическая'''


def count_sort(A):
    Q = [0 for i in range(max(A)+1)]
    for x in A:
        Q[x] += 1
    pos = 0
    for i in range(len(Q)):
        for j in range(Q[i]):
            A[pos] = i
            pos += 1
    return A
# A = list(randint(0, 333) for i in range(0, 10))
# print(A)
# print(count_sort(A))
'''O(M+N)'''


def radix_sort(A):
    for i in range(len(str(max(A)))):
        B = [[] for k in range(10)]
        for x in A:
            digit = (x//10**i) % 10
            B[digit].append(x)
        A = B[0]+B[1]+B[2]+B[3]+B[4]+B[5]+B[6]+B[7]+B[8]+B[9]
    return A
A = list(randint(0, 333) for i in range(0, 10))
# print(A)
# print(radix_sort(A))
'''O(MN)'''


def hoar_sort(A):
    if len(A) <= 1:
        return A
    barrier = choice(A)
    L, M, R = [], [], []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    return hoar_sort(L) + M + hoar_sort(R)
A = list(randint(0, 333) for i in range(0, 10))
# print(A)
# print(hoar_sort(A))
'''O(N**2)'''


def merge_sort(A):
    if len(A) <= 1:
        return A
    left = merge_sort(A[:len(A)//2])
    right = merge_sort(A[len(A)//2:])
    return merge(left, right)


def merge(L, R):
    A = [None] * (len(L) + len(R))
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    A[k:] = L[i:] + R[j:]
    return A

# A = list(randint(0, 333) for i in range(0, 10))
# print(A)
# print(merge_sort(A))