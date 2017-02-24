from app.scanner import Scanner

data = ""
with open('test.m', 'r') as content_file:
	data = content_file.read()

scanner = Scanner(data)
scanner.parse()


print(scanner)

token_collection = scanner.get_token_collection()
