import unittest, requests

class MyTest(unittest.TestCase):
	def test_check_google(self):
		res = requests.get('https://www.google.com')
		self.assertEquals(res.status_code, 200)

	def test_add(self):
		self.assertEquals(10+20, 30)
