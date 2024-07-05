def print_steps(n, source, helper, destination):
    if n == 0:
        return
    print_steps(n-1, source, destination, helper)
    print("Move disk from {} to {}".format(source, destination))
    print_steps(n-1, helper, source, destination)


if __name__ == "__main__":
    num = int(input())
    print_steps(num, 'S', 'H', 'D')