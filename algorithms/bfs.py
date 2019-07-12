
from node import Node
def _bfs(node, target, visited, to_visit):

    # bfs uses queue
    # print('Searches ', node.data)
    if node.data == target:
        return True
    
    if node.data not in visited:
        visited.add(node.data)
        to_visit.extend(node.adjacent)
        # print(to_visit)

    while len(to_visit) > 0:
        node = to_visit[0]
        to_visit = to_visit[1:]
        print(node.data)
        return _bfs(node, target, visited, to_visit)
    
    return False

def _bfs1(node, target, visited, to_visit):

    # bfs uses queue
    # print('Searches ', node.data)
    to_visit.extend([node])
    while len(to_visit) > 0:
        node = to_visit[0]
        print(node.data)
        to_visit = to_visit[1:]

        if node.data == target:
            return True

        if node.data not in visited:
            visited.add(node.data)
            to_visit.extend(node.adjacent)
        else:
            continue
    
    return False

def bfs(node, target):

    to_visit = []
    visited = set()
    return _bfs1(node, target, visited, to_visit)


n5 = Node(5)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)
n11 = Node(11)
n12 = Node(12)
n13 = Node(13)
n14 = Node(14)
n15 = Node(15)

n5.set_adjacent([n7,n8,n9])
n8.set_adjacent([n11,n12,n13])
n12.set_adjacent([n14,n15])

print(bfs(n5, 11))





