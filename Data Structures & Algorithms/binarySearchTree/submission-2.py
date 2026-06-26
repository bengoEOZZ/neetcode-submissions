class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None   # left child
        self.right = None  # right child


class TreeMap:
    def __init__(self):
        self.root = None  # Empty tree starts with no root


    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)


        # If tree is empty, new node becomes the root
        if self.root is None:
            self.root = newNode
            return


        curr = self.root
        while True:
            # Case 1: key is smaller, go left
            if key < curr.key:
                if curr.left is None:
                    curr.left = newNode  # found empty spot, insert here
                    return
                curr = curr.left
            # Case 2: key is larger, go right
            elif key > curr.key:
                if curr.right is None:
                    curr.right = newNode  # found empty spot, insert here
                    return
                curr = curr.right
            # Case 3: duplicate key, just update the value
            else:
                curr.val = val
                return


    def get(self, key: int) -> int:
        curr = self.root
        while curr is not None:
            # Case 1: target is in left subtree
            if key < curr.key:
                curr = curr.left
            # Case 2: target is in right subtree
            elif key > curr.key:
                curr = curr.right
            # Case 3: found it, return value
            else:
                return curr.val
        return -1  # key not found


    def getMin(self) -> int:
        node = self.findMin(self.root)
        return node.val if node else -1  # return -1 if tree is empty


    # returns the node with the minimum key in the subtree
    def findMin(self, node: TreeNode) -> TreeNode:
        # minimum is always the leftmost node
        while node and node.left:
            node = node.left
        return node




    def getMax(self) -> int:
        curr = self.root
        # maximum is always the rightmost node
        while curr and curr.right:
            curr = curr.right
        return curr.val if curr else -1  # return -1 if tree is empty


    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)


    # returns the new root of the subtree after removing the key
    def removeHelper(self, curr: TreeNode, key: int) -> TreeNode:
        if curr is None:
            return None  # key not found, nothing to remove


        # Case 1: target is in right subtree
        if key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        # Case 2: target is in left subtree
        elif key < curr.key:
            curr.left = self.removeHelper(curr.left, key)
        # Case 3: found the node to remove
        else:
            # Case 3a: no left child, replace with right child
            if curr.left is None:
                return curr.right
            # Case 3b: no right child, replace with left child
            elif curr.right is None:
                return curr.left
            # Case 3c: two children, replace with inorder successor
            else:
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeHelper(curr.right, minNode.key)


        return curr


    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result  # keys returned in sorted ascending order


    def inorderTraversal(self, root: TreeNode, result: List[int]) -> None:
        if root is not None:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)

