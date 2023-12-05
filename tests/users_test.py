import unittest
import users
from test_util import init_test, MockupRequest
from werkzeug.security import check_password_hash, generate_password_hash

class UserTest(unittest.TestCase):
	def setUp(self):
		self.app, self.db = init_test()	

	def test_register(self):
		with self.app.app_context(), self.app.test_request_context():
			self.assertTrue(users.register(self.db, "test_user1", generate_password_hash("password1")))
