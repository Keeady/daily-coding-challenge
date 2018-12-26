from Tree import Inorder
from library import node

five = node.Node(5)
four = node.Node(4)
two = node.Node(2, four, five)
three = node.Node(3)
one = node.Node(1, two, three)

result = Inorder.inorder(one)
assert [4,2,5,1,3] == result

