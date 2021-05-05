def z_func(t:str, p:str):
    """
    Эффективный алгоритм вычисления Z-функции
    :param p: substring
    :param t: string
    :return: count substing in string
    """
    s = p + '#' + t
    n = len(s)
    z = [0] * n
    l = 0
    r = 0
    k = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r-i+1, z[i-l])
        elif i > r:
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
        elif i + z[i] - 1 > r:
            l = i
            r = i = i + z[i] - 1
    for i in range(len(t)):
        if z[i+len(p)+1] == len(p):
            k += 1
    print(k)



z_func('abaababababababab', 'aba')