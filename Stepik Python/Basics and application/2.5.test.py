def mod_cheker(x, mod = 0):
    return lambda y: y % x == mod
mod_3 = mod_cheker(3)

print(mod_3(3))
print(mod_3(4))

mod_3_1 = mod_cheker(3, 1)
print(mod_3_1(4))