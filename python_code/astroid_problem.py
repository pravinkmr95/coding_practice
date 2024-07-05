def asteroidsDestroyed(mass: int, asteroids) -> bool:
    # asteroids.sort()
    # for ast in asteroids:
    #     if ast > mass:
    #         return False
    #     else:
    #         mass += ast
    # return True
    stack = []
    for ast in asteroids:
        if ast > mass:
            stack.append(ast)
        else:
            mass += ast
    print(mass)
    print(stack)
    while stack:
        top = stack.pop()
        if top > mass:
            return False
        else:
            mass += top
    return True


asteroids = [77244,19898,13062,79891,33924,90485,2244]
mass = 14359
print(asteroidsDestroyed(mass, asteroids))