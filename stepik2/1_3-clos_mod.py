def closest_mod_5(x):
    while True:
        if x % 5 == 0:
            return x
        x += 1
    return "I don't know :("

print(closest_mod_5(int(input())))