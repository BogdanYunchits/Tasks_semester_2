def calculate_power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        half_power = calculate_power(base, exponent // 2)
        return half_power * half_power
    else:
        return base * calculate_power(base, exponent - 1)

base = 6
exponent = 18
print(calculate_power(base, exponent))
