# You may serialize the following tree:
#
#     1
#    / \
#   2   3
#      / \
#     4   5
#
# as "[1,2,3,null,null,4,5]"
import collections
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Helper:

    def serialize(self, root):
        def preorder(node, res):
            if not node:
                res.append('#')
                return
            res.append(str(node.val))
            preorder(node.left, res)
            preorder(node.right, res)

        res = []
        preorder(root, res)
        #try to serilize it with preorder, add # if node is none
        #[1, 2, #, #, 3, 4, #, #, 5, #, #]
        return ' '.join(res)

    def deserialize(self, data):
        def buildtree():
            if not dq: return
            val = dq.popleft()
            if val == '#': return
            node = TreeNode(int(val))
            node.left = buildtree()
            node.right = buildtree()
            return node
        dq = collections.deque(data.split(' '))
        return buildtree()


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

helper = Helper()
data = helper.serialize(root)
print(data)
root = helper.deserialize(data)
print(root.val)
print(root.left.val)
print(root.right.val)
print(root.right.left.val)
print(root.right.right.val)