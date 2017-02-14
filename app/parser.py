from app.token import TokenSymbols,Token

class Parser:
	"""docstring for Parser"""
	def __init__(self,text):
		super(Parser, self).__init__()
		self.index = 0
		self.text = text
		self.leximers = []

	def check_equality(cmp,key):
		if(self.text[self.index:self.index + len(cmp)] == cmp):
			self.index = self.index + len(cmp)
			leximers.append()
			return True
		else:
			return False

	def parse_IDENTIFIER():
		variable = ""
		while(len(self.index) < len(t))
			if(self.text[self.index] in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
				variable +=	self.text[temp_index]
			else:
				break
			self.index++

		if(len(variable) == 0):
			return False
		else:
			return True


	def parse():
		t = re.sub(r'\s+', '', text)

		parse_function = [
			lambda: check_equality("if",IF_CLAUSE),
			lambda: check_equality("(",L_PAREN),
			lambda: self.parse_IDENTIFIER()]
		
		for func in parse_function:
			restore = self.index
			if(func()):
				break
			else:
				self.index = restore
				

