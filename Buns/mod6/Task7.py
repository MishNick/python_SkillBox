from typing import Optional
from collections import defaultdict
from queue import Queue

class BinaryTreeNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left: Optional[BinaryTreeNode] = None
        self.right: Optional[BinaryTreeNode] = None

def restore_tree(logs_path: str) -> Optional[BinaryTreeNode]:
    nodes = defaultdict(BinaryTreeNode)
    root = None

    with open(logs_path, 'r') as file:
        for line in file:
            node_num, left_num, right_num = map(int, line.strip().split())
            node = nodes[node_num]

            if root is None:
                root = node

            if left_num != -1:
                node.left = nodes[left_num]
            if right_num != -1:
                node.right = nodes[right_num]

    return root

def walk_tree(root: Optional[BinaryTreeNode]) -> None:
    if root is None:
        return

    visited = set()
    queue = Queue()
    queue.put(root)
    level = 0

    while not queue.empty():
        level_size = queue.qsize()
        print(f'Level: {level}')
        while level_size > 0:
            node = queue.get()
            visited.add(node)
            print(f'Node: {node.value}')
            if node.left and node.left not in visited:
                queue.put(node.left)
            if node.right and node.right not in visited:
                queue.put(node.right)
            level_size -= 1
        level += 1

root = BinaryTreeNode(1)
root.left = node2 = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
node2.left = BinaryTreeNode(4)
node2.right = BinaryTreeNode(5)

with open('logs.txt', 'w') as file:
    walk_tree(root, file)

restored_root = restore_tree('logs.txt')

walk_tree(restored_root)
