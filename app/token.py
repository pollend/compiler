class TokenSymbols(Enum):
	L_PAREN = 0
	R_PAREN = 1
	L_CURLEY_BRACE = 2
	R_CURLEY_BRACE = 3
	COMMA = 4
	IDENTIFIER = 6
	EQUAL_SIGN = 7
	LESS_THEN = 8
	LESS_THEN_EQUAL = 9
	GREATER_THEN = 11
	GREATER_THEN_EQUAL = 10
	DOUBLE_EQUAL = 11
	IF_CLAUSE = 12
	WHILE_CLAUSE = 13
	NUMBER = 14


class Token():
	"""docstring for Leximers"""
	def __init__(self, key,value):
		super(Leximers, self).__init__()
		self.key = key
		self.value = value
	
	def __init__(self, key):
		super(Leximers, self).__init__()
		self.key = key
	
	def get_key(self)
		return self.key
	def get_value(self)
		return value

		

