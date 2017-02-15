class Element(Enum):
	PROGRAM = 0
	STATEMENT = 1
	ASSIGNMENT_STATEMENT = 2 # x = 10
	IF_STATEMENT = 4
	BLOCK = 5 # any containg element bettwn {}
	EXPRESSION = 6
	UNIT


class TreeNode:
	"""docstring for TreeNode"""
	def __init__(self,type):
		self.children = []
		self.type = type
	def append_child(node):
		self.children.append(node)
	def is_tree_node(index):
		if(type(self.children[index]) is TreeNode):
			return True
		return False