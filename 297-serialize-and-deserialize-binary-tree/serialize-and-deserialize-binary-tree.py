# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return 'null'
        queue = deque([root])
        result = []
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append('null')
        
        return ','.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == 'null':
            return None
        data_list = data.split(',')
        root = TreeNode(int(data_list[0]))
        queue = deque([root])
        index = 1
        while queue:
            current_node = queue.popleft()
            if data_list[index] != 'null':
                left_child = TreeNode(int(data_list[index]))
                current_node.left = left_child
                queue.append(left_child)
            index += 1
            if data_list[index] != 'null':
                right_child = TreeNode(int(data_list[index]))
                current_node.right = right_child
                queue.append(right_child)
            index += 1
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))