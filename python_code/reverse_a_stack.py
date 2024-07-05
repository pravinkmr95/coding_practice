class Stack:
    def __init__(self):
        self.st = []

    def push(self, num):
        self.st.append(num)

    def pop(self):
        if self.st:
            top = self.top()
            self.st.pop()
            # print(top)
        else:
            return "Empty stack"

    def top(self):
        if self.st:
            return self.st[-1]
        else:
            return -1

    def size(self):
        return len(self.st)

    def display(self):
        print(self.st)


def insert_num_stack(st, numb):
    if st.size() == 0:
        st.push(numb)
        return
    temp = st.top()
    st.pop()
    insert_num_stack(st, numb)
    st.push(temp)


def reverse_the_stack(st):
    if st.size() == 1:
        return
    temp = st.top()
    st.pop()
    reverse_the_stack(st)
    # print("temp = {}".format(temp))
    insert_num_stack(st, temp)


if __name__ == "__main__":
    st = Stack()
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(2)
    st.push(3)
    # print(st.top())
    st.push(4)
    st.push(5)
    # st.display()
    st.pop()
    st.display()
    st.size()
    # print(st.top())
    reverse_the_stack(st)
    st.display()
