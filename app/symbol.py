from app.symbol_type import SymbolType

class Symbol:

	"""docstring for Tree"""
	def __init__(self, symbol, entry_table):
		self.symbol = symbol
		self.entry_table = entry_table 

	def __str__(self):
		if(not self.entry_table):
			return str(self.symbol) 
		else:
			return str(self.symbol)  + "->" + str(self.entry_table)
