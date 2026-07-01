# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        if root==None:
            return ""
        q=deque()
        ans=""
        q.append(root)
        while q:
            temp=q.popleft()
            if temp==None:
                ans=ans+('#,')
            else:
                ans=ans+(str(temp.val)+',')
            
                q.append(temp.left)
                q.append(temp.right)
        print(ans)
        return ans         

    def deserialize(self, data):
        if not data:
            return None
        
        nodes=data.split(',')[:-1]  # str to comma seperated list of char...
        
        
        root=TreeNode(int(nodes[0]))
        q=deque([root])
        i=1
        while q :
            curr=q.popleft()
            if  nodes[i]!='#':
                curr.left=TreeNode(int(nodes[i]))
                q.append(curr.left)
            i+=1
            if  nodes[i]!='#':
                curr.right=TreeNode(int(nodes[i]))
                q.append(curr.right)
            i+=1
        return root
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))