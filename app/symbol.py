from app.symbol_type import SymbolType

class Symbol:

	"""docstring for Tree"""
	def __init__(self, symbol, entry_table):
		super(Symbol, self).__init__()
		# an entry descries the mapping for the object
		self.symbol = symbol
		self.entry_table = entry_table 

