from time import timezone
from django.utils import timezone

from django.test import TestCase
from courses.models import  Course , Subject
from users.models import  Account

class TestModels(TestCase):
     def setUp(self) :
         self.subject = Subject.objects.create(title='Programming news')
         self.owner = Account.objects.create(email= 'teast@gmail.com',
                                 password= 'test',
                                 fullname= 'Test')
         self.course = Course.objects.create(title = ' books',
                              owner = self.owner,
                              subject = self.subject,
                              overview='this is a sample overview',
                              created = timezone.now()
         )
     def test_course_creation(self):
        course = self.course
        self.assertTrue(isinstance( course, Course))
        self.assertEqual(course.slug ,  'books')

     def test_subject_creation(self):
         subject = self.subject
         self.assertTrue(isinstance(subject, Subject))
         self.assertIsInstance(self.subject.title, str)
         self.assertEqual( subject.slug, 'programming-news')

