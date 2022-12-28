from django.contrib.auth.mixins import UserPassesTestMixin
from ghasedakpack import *


def send_otp_code(phone_number, code):

	sms = ghasedakpack.Ghasedak("vuyDb4/n8/XM44gZHDzGzHMyF8CKqnSGgftvGqUWZUo")
	sms.send({'message': code, 'receptor': phone_number, 'linenumber': 'xxxx', 'senddate': '', 'checkid': ''})


class IsAdminUserMixin(UserPassesTestMixin):
	def test_func(self):
		return self.request.user.is_authenticated and self.request.user.is_admin