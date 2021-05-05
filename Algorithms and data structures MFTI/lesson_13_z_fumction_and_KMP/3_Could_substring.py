def z_func(s):
    """
    Упражнение №3: Количество разных подстрок
    :param s:
    :return:
    """
    n = len(s)
    z = [0] * n
    k = 0 # текущее количество подстрок строки S
    l = 0
    r = 0
    t = ''
    for j in range(n):
        t += s[j]
        rt = t[::-1]
        for i in range(1, len(rt)):
            while i + z[i] < len(rt) and rt[z[i]] == rt[i + z[i]]:
                    z[i] += 1
        k += len(rt) - max(z)
    return k


print(z_func('aaaaa'))