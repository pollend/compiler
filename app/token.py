from enum import Enum


class TokenSymbols(Enum):
	L_PAREN = 0				# (
	R_PAREN = 1         	# )
	L_CURLEY_BRACE = 2  	# {
	R_CURLEY_BRACE = 3  	# }
	COMMA = 4           	# ,
	IDENTIFIER = 5      	# VARIABLE NAME
	EQUAL = 6 				# =
	PLUS_EQUAL 	= 7			# +=
	MINUS_EQUAL = 8			# -=
	LESS_THEN_EQUAL = 9 	# <=
	GREATER_THEN_EQUAL = 10	# >=
	GREATER_THEN = 12		# >
	LESS_THEN = 13			# <
	DOUBLE_EQUAL = 14		# ==
	IF_CLAUSE = 15 			# if
	WHILE_CLAUSE = 16		# While
	NUMBER = 17				# 10 100
	SEMI_COLON = 18			# ;
	OR_OPERATOR = 19 		# ||
	AND_OPERATOR = 20 		# &&