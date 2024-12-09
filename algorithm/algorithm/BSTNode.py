class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.key = value
        self.left = None
        self.right = None

# 순환 구조
def search_bst(node ,key):
    if node == None:
        return None
    elif key == node.value:
        return node
    elif key < node.value:
        return search_bst(node.left, key)
    else:
        return search_bst(node.right, key)
    
#반복 구조
def search_bst_loop(node, key):
    while node is not None:
        if key == node.value:
            return node
        elif key < node.value:
            node = node.left
        else:
            node = node.right
    return -1

def insert_node(root, target):
    if root == None:
        return target
    if target.key == root.key:
        return root
    
    if target.key < root.key:
        root.left = insert_node(root.left, target)
    else:
        root.right = insert_node(root.right, target)
    
    return root

def remove_node(root, key):
    if root is None:
        return root  # 삭제할 키가 트리에 없음

    # 탐색: 삭제할 키를 찾는다
    if key < root.key:
        root.left = remove_node(root.left, key)
    elif key > root.key:
        root.right = remove_node(root.right, key)
    else:
        # 삭제할 노드를 찾음
        if root.left is None:  # 오른쪽 자식만 있거나 리프 노드
            return root.right
        elif root.right is None:  # 왼쪽 자식만 있음
            return root.left

        # 두 자식이 있는 경우: 후계자 노드를 찾음
        min_larger_node = find_min(root.right)
        root.key = min_larger_node.key
        root.value = min_larger_node.value
        # 후계자 노드를 삭제
        root.right = remove_node(root.right, min_larger_node.key)

    return root

def find_min(node):
    while node.left is not None:
        node = node.left
    return node
