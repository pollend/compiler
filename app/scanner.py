from app.token import TokenSymbols
from app.symbol import Symbol

ALPHA = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
NUMERIC = ['0','1','2','3','4','5','6','7','8','9']
SPACE = ['\s','\r',' ','\t', '\n']

class Scanner:
	"""docstring for Scan"""
	def __init__(self, source):
		self.source = source
		self.index = 0
		self.token_collection = []

	def parse(self):
		while self.index < len(self.source) :
			if (self.check_equality("if")):
				self.token_collection.append(Symbol(TokenSymbols.IF_CLAUSE,""))
			elif(self.check_equality("while")):
				self.token_collection.append(Symbol(TokenSymbols.WHILE_CLAUSE,""))
			elif(self.check_equality("||")):	
				self.token_collection.append(Symbol(TokenSymbols.OR_OPERATOR,""))
			elif(self.check_equality("&&")):	
				self.token_collection.append(Symbol(TokenSymbols.AND_OPERATOR,""))
			elif(self.check_equality(";")):
				self.token_collection.append(Symbol(TokenSymbols.SEMI_COLON,""))
			elif(self.check_equality(")")):
				self.token_collection.append(Symbol(TokenSymbols.R_PAREN,""))
			elif(self.check_equality("(")):
				self.token_collection.append(Symbol(TokenSymbols.L_PAREN,""))
			elif(self.check_equality(",")):
				self.token_collection.append(Symbol(TokenSymbols.COMMA,""))
			elif(self.check_equality("{")):
				self.token_collection.append(Symbol(TokenSymbols.L_CURLEY_BRACE,""))
			elif(self.check_equality("}")):
				self.token_collection.append(Symbol(TokenSymbols.R_CURLEY_BRACE,""))
			elif(self.check_equality("==")):
				self.token_collection.append(Symbol(TokenSymbols.DOUBLE_EQUAL,""))
			elif(self.check_equality("<=")):
				self.token_collection.append(Symbol(TokenSymbols.LESS_THEN_EQUAL,""))
			elif(self.check_equality(">=")):
				self.token_collection.append(Symbol(TokenSymbols.GREATER_THEN_EQUAL,""))
			elif(self.check_equality("<")):
				self.token_collection.append(Symbol(TokenSymbols.LESS_THEN,""))
			elif(self.check_equality(">")):
				self.token_collection.append(Symbol(TokenSymbols.GREATER_THEN,""))
			elif(self.check_equality("=")):
				self.token_collection.append(Symbol(TokenSymbols.EQUAL,""))
			elif(self.check_equality("+=")):
				self.token_collection.append(Symbol(TokenSymbols.PLUS_EQUAL,""))
			elif(self.check_equality("-=")):
				self.token_collection.append(Symbol(TokenSymbols.MINUS_EQUAL,""))
			elif(self.check_equality('.')):
				self.token_collection.append(Symbol(TokenSymbols.PERIOD,""))
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
								self.token_collection.append(Symbol(TokenSymbols.NUMBER,numeric))
							else:
								self.token_collection.append(Symbol(TokenSymbols.NUMBER,numeric))
						else:
							self.token_collection.append(Symbol(TokenSymbols.NUMBER,numeric))
					else:
						variable = ""
						while(self.index < len(self.source) ):
							if(self.source[self.index] in ALPHA):
								variable += self.source[self.index]
							else:
								break
							self.index += 1
						self.token_collection.append(Symbol(TokenSymbols.IDENTIFIER,variable))
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

	def __str__(self):
		result = []
		for tk in self.token_collection:
			result.append(str(tk))
		return str(result)
