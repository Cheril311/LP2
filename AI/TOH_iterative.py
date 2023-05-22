class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0


def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    stack = Stack()
    done = False

    while not done:
        if n > 0:
            stack.push((n, from_rod, to_rod, aux_rod))
            n -= 1
            from_rod, to_rod, aux_rod = from_rod, aux_rod, to_rod
        else:
            if not stack.is_empty():
                n, from_rod, to_rod, aux_rod = stack.pop()
                print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
                n -= 1
                from_rod, to_rod, aux_rod = aux_rod, to_rod, from_rod
            else:
                done = True
print(TowerOfHanoi(4, '0', '2', '1'))
