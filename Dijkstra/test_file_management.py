import unittest
from FileManagement import FileManagement


class TestFileManagement(unittest.TestCase):
	
	def setUp(self):
		self.fm = FileManagement()
		print("fikszczur test file management")

	def testReadFromFile(self):
		retStr = self.fm.readFromFile("test.txt")
		self.assertEqual("""1 2 3\n4 5 6""", retStr)

if __name__ == '__main__':
	unittest.main()