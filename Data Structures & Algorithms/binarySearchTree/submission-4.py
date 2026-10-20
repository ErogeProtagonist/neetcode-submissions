class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if not self.root:
            self.root = TreeNode(key, val)
            return

        curr = self.root
        while curr:
            if key == curr.key:
                curr.val = val
                return
            elif key < curr.key:
                if not curr.left:
                    curr.left = TreeNode(key, val)
                    return
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = TreeNode(key, val)
                    return
                curr = curr.right
                

    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            if key == curr.key:
                return curr.val
            elif key > curr.key:
                curr = curr.right
            else:
                curr = curr.left
        return -1
                    

    def getMin(self) -> int:
        if not self.root:
            return -1
        curr = self.root
        while curr and curr.left:
            curr = curr.left
        
        return curr.val

    def getMax(self) -> int:
        if not self.root:
            return -1
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val
    
    def remove(self, key: int) -> None:
        def minNode(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr
        def bst(root, key):
            if not root:
                return None
            
            if key > root.key:
                root.right = bst(root.right, key)
            elif key < root.key:
                root.left = bst(root.left, key)
            else:
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                min_node = minNode(root.right)
                root.val = min_node.val
                root.key = min_node.key
                root.right = bst(root.right, min_node.key)
            return root
        self.root = bst(self.root, key)

    def getInorderKeys(self) -> List[int]:
        result = []
        stack = []
        curr = self.root
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            result.append(curr.key)
            curr = curr.right
        
        return result

