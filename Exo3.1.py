def is_prime(x):
    for i in range(2, x-1):
        if x % i == 0:
            return False
    return True
for x in range(1,100):
    print(f"{x}: {is_prime(x)}")