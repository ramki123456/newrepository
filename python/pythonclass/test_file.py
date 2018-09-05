import unittest, requests # urllib,urllib2, http
from data import get_name, get_increment 

# Client will give us "Authentication Details"
# URL(API)
# Functions to call
# Api Key for Maps : AIzaSyCvewXidiRM27WFUZKCC9JT30Xvntde378 

class MyTestCases(unittest.TestCase):
	def test_check_gmail(self):
		data = {'id_username': 'hari', 'id_password': 'kanna212$'}
		url= "http://127.0.0.1:8000/admin/login/?next=/admin/"
		res = requests.get(url, data=data)
		self.assertEquals(res.status_code, 200)
		self.assertNotEquals(res.content, None)


	def test_name(self):
		name = get_name()
		self.assertEquals(len(name), 5, "The length of name should equals to 5")
		self.assertEquals(name.isalnum(), True, "The name should not contains Special chars like ' ' , '$', '!' etc ")

	def increment(self):
		self.assertEquals(get_increment(18000), 26000, "Increment Not correct")