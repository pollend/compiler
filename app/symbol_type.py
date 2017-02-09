from enum import Enum

class SymbolType(Enum):
	NONE = 0
	STATEMENT = 1
	ASSIGNMENT_EXPRESSION = 2

class AssignmentOperators(Enum):
	EQUAL = "="
	PLUS_EQUAL = "+="
	SUBTRACT_EQUAL = "-="
