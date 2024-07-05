class SetBitMasking:
    def __init__(self):
        self.set_binary = 0

    def add_value_in_set(self, num):
        self.set_binary = self.set_binary | 1 << (num-1)

    def print_set(self):
        print(bin(self.set_binary)[2:])

    def get_value(self, num):
        if self.set_binary & 1 << (num-1):
            return True
        else:
            return False

    def delete_value(self, num):
        if self.get_value(num):
            num -= 1
            self.set_binary = self.set_binary & ~ (1 << num)
        else:
            print("Number {} is not present in the set".format(num))


if __name__ == "__main__":
    bmo = SetBitMasking()
    bmo.add_value_in_set(5)
    bmo.add_value_in_set(8)
    bmo.add_value_in_set(20)
    bmo.add_value_in_set(5)
    bmo.add_value_in_set(1)
    bmo.add_value_in_set(10)
    print("Print Set ", end='')
    bmo.print_set()
    print("Get 5 ", end=' ')
    print(bmo.get_value(5))
    print("Get 12", end=' ')
    print(bmo.get_value(12))
    print("Delete 20")
    bmo.delete_value(20)
    print("Print Set", end=' ')
    bmo.print_set()
    print("Get 20", end=' ')
    print(bmo.get_value(20))
    print("Delete 4")
    bmo.delete_value(4)
    print("Print Set", end=' ')
    bmo.print_set()
