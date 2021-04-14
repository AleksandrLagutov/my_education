def z_func(s):
    """
    Эффективный алгоритм вычисления Z-функции
    :param s:
    :return:
    """
    n = len(s)
    z = [0] * n
    l = 0
    r = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r-i+1, z[i-l])
        elif i > r:
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
        elif i + z[i] - 1 > r:
            l = i
            r = i = i + z[i] - 1


print(z_func('aaaabaa'))