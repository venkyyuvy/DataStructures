# reversing a stack without additional space

def insert_at_bottom(stack, element):
    if not stack:
        stack.append(element)
        return stack
    top = stack.pop()
    stack = insert_at_bottom(stack, element)
    stack.append(top)
    return stack

def reverse(stack):
    if not stack:
        return stack
    top = stack.pop()
    reverse(stack)
    stack = insert_at_bottom(stack, top)
    return stack

def test_insert_at_bottom():
    return insert_at_bottom(list(range(5)), 40)

print(test_insert_at_bottom())

def test_reverse():
    stack = list(range(20))
    print(reverse(stack))

test_reverse()
