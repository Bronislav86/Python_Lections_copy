# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     print(summa)


# sum_numbers(5)

# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa

# a = sum_numbers(5)

# print(a)


# def sum_numbers(n, y="hello"):
#     print(y)
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa


# a = sum_numbers(5, "qwerty")
# print(a)


# def sum_nstr(*args):
#     res = ''
#     for i in args:
#         res+= i
#     return res

# print(sum_nstr('q', 'e', '1'))
# print(sum_nstr('q', 'e', '1', 'r', 'f'))
# print(sum_nstr('1', '8', '9'))

# ----------------------------------МОДУЛЬНОСТЬ-----------------------------
# import modul1
# print(modul1.max1(5, 9))

# # ИЛИ

# # from modul1 import max1

# # print(max1(10, 9))

# # ------------------------------
# import modul1 as m1

# print(m1.max1(10, 9))

# ----------------------------------РКУРСИЯ------------------------------------


# def fib(n):
#     print(n)
#     if n in [1, 2]:  # ЭТО БАЗИС!!!!
#         return 1
#     return fib(n - 1) + fib(n - 2)


# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)

# ---------------------БЫСТРАЯ СОРТИРОВКА------------------------------


# def quic_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quic_sort(less) + [pivot] + quic_sort(greater)


# print(quic_sort([10, 5, 2]))

# ------------------------------СОРТИРОВКА СЛИЯНИЕМ------------------------


# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1
            
#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1
            
#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1

# lis_1 = [1, 5, 8, 9 ,7 ,2 ,6]
# merge_sort(lis_1)
# print(lis_1)

# def concatenatio(*params):