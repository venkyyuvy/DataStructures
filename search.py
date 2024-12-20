from linked_list import LinkedList, DoubleLinkedList

def bfs_constant_space(graph, start_node):
    solution=f'{start_node}'
    linked_list = LinkedList(head=start_node)
    current_node = start_node
    while True:
        print(f'{current_node=}')
        for neighbor in graph.neighbors(current_node):
            if neighbor.nxt_node is None:
                solution += f"-{neighbor}"
                linked_list.add(neighbor)
        current_node = current_node.nxt_node
        if current_node.name == 'dummy':
            print('reached termination state')
            break
    return solution

def dfs_constant_space(graph, start_node):
    solution=''
    d_ll = DoubleLinkedList(head=start_node)
    current_node = start_node
    while d_ll.head is not None:
        current_node = d_ll.pop()
        print(f'{current_node=}')
        solution += f"{current_node}-"
        for neighbor in graph.neighbors(current_node):
            if neighbor.nxt_node is None:
                d_ll.add(neighbor)
    solution = solution[:-1]
    return solution

def dfs_iterative(graph, start_node):
    solution=''
    current_node = start_node
    pending_stack = [start_node,]
    visited = set()
    while pending_stack:
        current_node = pending_stack.pop()
        visited.add(current_node)
        print(f'{current_node=}')
        solution += f"{current_node}-"
        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                pending_stack.append(neighbor)
                visited.add(neighbor)
    solution = solution[:-1]
    return solution