def max_berries(a):
    n = len(a)
    dp1 = [0] * n
    dp2 = [0] * n

    dp1[0] = a[0]
    dp1[1] = a[1]
    dp2[0] = 0
    dp2[1] = a[1]

    for i in range(2, n):
        dp1[i] = max(dp2[i-1], dp1[i-2]) + a[i]
        dp2[i] = max(dp1[i-1], dp2[i-2]) + a[i]

    return max(dp1[n-1], dp2[n-1])

# Пример использования
a = [1, 2, 3, 4, 5]
max_berries(a)  # Вывод: 9