from app.token import TokenSymbols,EqualityTypes,AssignmentType

ALPHA = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
NUMERIC = ['0','1','2','3','4','5','6','7','8','9']
SPACE = ['\s','\r',' ','\t', '\n']

class Scanner:
	"""docstring for Scan"""
	def __init__(self, source):
		self.source = source
		self.index = 0
		self.token_collection = []

	def push_token(self,key,value):
		self.token_collection.append({"key" : key, "value" : value})

	def push_token_key(self,key):
		self.token_collection.append({"key" : key})

	def parse(self):
		while self.index < len(self.source) :
			if (self.check_equality("if")):
				self.push_token_key(TokenSymbols.IF_CLAUSE)
			elif(self.check_equality("while")):
				self.push_token_key(TokenSymbols.WHILE_CLAUSE)
			elif(self.check_equality("||")):	
				self.push_token(TokenSymbols.LOGICAL_OPERATOR,LogicalTypes.OR_OPERATOR)
			elif(self.check_equality("&&")):	
				self.push_token(TokenSymbols.LOGICAL_OPERATOR,LogicalTypes.AND_OPERATOR)
			elif(self.check_equality(";")):
				self.push_token_key(TokenSymbols.SEMI_COLON)
			elif(self.check_equality(")")):
				self.push_token_key(TokenSymbols.R_PAREN)
			elif(self.check_equality("(")):
				self.push_token_key(TokenSymbols.L_PAREN)
			elif(self.check_equality(",")):
				self.push_token_key(TokenSymbols.COMMA)
			elif(self.check_equality("{")):
				self.push_token_key(TokenSymbols.L_CURLEY_BRACE)
			elif(self.check_equality("}")):
				self.push_token_key(TokenSymbols.R_CURLEY_BRACE)
			elif(self.check_equality("==")):
				self.push_token(TokenSymbols.EQUALITY,EqualityTypes.DOUBLE_EQUAL)
			elif(self.check_equality("<=")):
				self.push_token(TokenSymbols.EQUALITY,EqualityTypes.LESS_THEN_EQUAL)
			elif(self.check_equality(">=")):
				self.push_token(TokenSymbols.EQUALITY,EqualityTypes.GREATER_THEN_EQUAL)
			elif(self.check_equality("<")):
				self.push_token(TokenSymbols.EQUALITY,EqualityTypes.LESS_THEN)
			elif(self.check_equality(">")):
				self.push_token(TokenSymbols.EQUALITY,EqualityTypes.GREATER_THEN)
			elif(self.check_equality("=")):
				self.push_token(TokenSymbols.ASSIGNMENT,AssignmentType.EQUAL)
			elif(self.check_equality("+=")):
				self.push_token(TokenSymbols.ASSIGNMENT,AssignmentType.PLUS_EQUAL)
			elif(self.check_equality("-=")):
				self.push_token(TokenSymbols.ASSIGNMENT,AssignmentType.MINUS_EQUAL)
			elif(self.check_equality('.')):
				self.push_token_key(TokenSymbols.PERIOD)
			else:
				if(not (self.source[self.index] in SPACE)):
					if(self.source[self.index] in NUMERIC):
						numeric = ""
						numeric += self.parse_number()
						if(self.index < len(self.source)):
							if(self.source[self.index] == '.'):
								numeric += "."
								self.index += 1
								numeric += self.parse_number()
								self.push_token(TokenSymbols.NUMBER,numeric)
							else:
								self.push_token(TokenSymbols.NUMBER,numeric)
						else:
							self.push_token(TokenSymbols.NUMBER,numeric)
					else:
						variable = ""
						while(self.index < len(self.source) ):
							if(self.source[self.index] in ALPHA):
								variable += self.source[self.index]
							else:
								break
							self.index += 1
						self.push_token(TokenSymbols.IDENTIFIER,variable)
			self.index += 1

	def parse_number(self):
		numeric = ""
		while(self.index < len(self.source) ):
			if(self.source[self.index] in NUMERIC):
				numeric += self.source[self.index]
			else:
				self.index -= 1
				break
			self.index += 1
		return numeric


	def get_token_collection(self):
		return self.token_collection

	def check_equality(self,cmp):
		if(self.source[self.index:self.index + len(cmp)] == cmp):
			self.index += len(cmp) -1
			return True
		else:
			return False	