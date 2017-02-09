IF = "if"
ASSIGNMENT_CHARACTER = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

class Parser(object):
	"""docstring for Parser"""
	def __init__(self,text):
		super(Parser, self).__init__()
		self.index = 0
		self.text = text

	def parse_exp():
		self.index++
		if(self.index != '(')
			return
		while(self.index < len(text)):
			
			self.index++

	def parse_assignment():
		output = ""
		pass

	def check_equality(cmp)
		return self.text[self.index:self.index  + len(cmp)] == cmp

	def parse():
		t = re.sub(r'\s+', '', text)
		self.index = 0
		while(self.index < len(t)):
			if(check_equality(IF)):
				parse_exp()
			self.index++