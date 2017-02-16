from app.token import  TokenSymbols,EqualityTypes,AssignmentType
from app.tree_node import TreeNode,Element

class Parser:
	"""docstring for Parser"""
	def __init__(self,token_collection):
		self.token_collection = token_collection
		self.index = 0

	def expected_token(self,node,token):
		if(self.index < len(self.token_collection)):
			print("EOF Expected Token:" + token)
		if(self.token_collection[self.index]["key"] == token)
			node.append_child(self.token_collection[self.index])
		else:
			print("Expected Token:" + token)
		
		
	def expected_token_value(self,node,token,value):
		if(self.index < len(self.token_collection)):
			print("EOF Expected Token:" + token)
		if(self.token_collection[self.index]["key"] == token and self.token_collection[self.index]["value"] == value)
			node.append_child(self.token_collection[self.index])
		else:
			print("Expected Token:" + token + "-" + value)

	def current_token(self):
		return self.token_collection[self.index]["key"]

	def next_token(self):
		self.index += 1
		if(self.index < len(self.token_collection)):
			return True
		return False

	def has_next_token():
		if((self.index +1) < len(self.token_collection)):
			return True
		return False

# -----------------------------------------------------------------------

	def parse_BLOCK(self):
		block = TreeNode(Element.BLOCK)	
		
		while(True):
			if(self.current_token() == TokenSymbols.IF_CLAUSE):
				pass
			elif(self.current_token() == TokenSymbols.WHILE_CLAUSE):
				pass
			elif(self.current_token() == TokenSymbols.IDENTIFIER):
	
	def parse_EXPRESSION(self,node):
		if(self.current_token() == TokenSymbols.)

	def parse_UNIT(self, node):

		pass

	def parse_LOGICAL_EXPRESSION(self, node):
		pass

	def parse_IF_STATEMENT(self,parent):

		if_statement = TreeNode(Element.IF_STATEMENT)
		self.expected_token(if_statement,TokenSymbols.IF_CLAUSE)
		
		self.next_token()
		self.expected_token(if_statement,TokenSymbols.L_PAREN)
		
		self.next_token()
		self.parse_LOGICAL_EXPRESSION(if_statement)
		
		self.next_token()
		self.expected_token(if_statement,TokenSymbols.R_PAREN)
		parent.append_child()

		

		pass

	def parse_STATEMENT(self,parent):
		if(self.current_token() == TokenSymbols.IF_CLAUSE):
			statement = TreeNode(Element.IF_STATEMENT)
			statement.append_child()
			parent.append_child()


	def build():
		program = TreeNode(Element.PROGRAM)
		while(has_next_token()):
			program.append_child(self.parse_STATEMENT(program))
		