class FileManagement:
	def readFromFile(self, name):
		with open(name, 'r') as f:
			data = f.read()
		f.closed
		return data