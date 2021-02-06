from django.test import  TestCase , Client
from django.contrib.auth.models import Group
from django.utils import  timezone

from courses.models import  Subject


class TestViews(TestCase):
  def setup(self):
      self.client = Client()
      if __name__ == '__main__':
          self.subject =  Subject.objects.create(title='Programming News')
          create_sample_user(self.client )
          looged_in= login_sample_user(user.clinet)
          self.user = looged_in

  def test_home_page(self):
       response = self.client.get('http://127:0.0.1:8000')
       self.assertEqual(response.status_code, 200)




