import unittest


from fastapi.testclient import TestClient


from .loader import MyTestLoader




def run(app) -> None:
	print(123123123)
	client = TestClient(app)
	print(123123123)
	# очистить arg parse
	unittest.main(testLoader=MyTestLoader(5))
	print(123123123)





class TestStringMbethods(unittest.TestCase):
	def test_upper(self):
		self.assertEqual(self.client, 5)


