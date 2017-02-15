from enum import Enum


class TokenSymbols(Enum):
	L_PAREN = 0			# )
	R_PAREN = 1         # (
	L_CURLEY_BRACE = 2  # {
	R_CURLEY_BRACE = 3  # }
	COMMA = 4           # ,
	IDENTIFIER = 5      # variable name
	ASSIGNMENT = 6 		# = += -= 
	EQUALITY = 7 		# <= < > >= ==
	IF_CLAUSE = 8  		# if
	WHILE_CLAUSE = 9	# While
	NUMBER = 10		# 10 100
	SEMI_COLON = 12		# ;
	

class EqualityTypes(Enum):
	LESS_THEN_EQUAL = 0
	GREATER_THEN_EQUAL = 1
	LESS_THEN = 2
	GREATER_THEN = 3
	DOUBLE_EQUAL = 4


class AssignmentType(Enum):
	EQUAL = 0
	PLUS_EQUAL = 1  
	MINUS_EQUAL = 2

