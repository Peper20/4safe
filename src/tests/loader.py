import unittest




class MyTestLoader(unittest.TestLoader):
	def __init__(self, client):
		super().__init__()
		self.client = client


	def loadTestsFromTestCase(self, testCaseClass):
		testCaseClass.client = self.client
		return super().loadTestsFromTestCase(testCaseClass)
