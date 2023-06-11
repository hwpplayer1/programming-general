def isprime(val):
    if val % 2 == 0:
        return val == 2
    for i in range(3, val, 2):
        if val % i == 0:
            return False
    return True

result = [i for i in range(2, 1000) if isprime(i)]
print(result)
