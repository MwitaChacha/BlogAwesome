import unittest
from app.models import User, Post, Comment

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'password')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('password'))

class PostModelTest(unittest.TestCase):
        '''
        Test class to test the behavior of the Post class
        '''

        def setUp(self):
            '''
            Set up method that will run before every Test
            '''
            self.new_post = Post(1, 1,' post', 'post','post')

        def test_instance(self):
            '''
            '''
            self.assertTrue(isinstance(self.new_post, Post))

        def test_to_check_instance_variables(self):
            '''
            '''
            self.assertEquals(self.new_post.id, 1)
            self.assertEquals(self.new_post.author, 1)
            self.assertEquals(self.new_post.title, 'pitch')
            self.assertEquals(self.new_post.content, 'pitch')
            
class CommentModelTest(unittest.TestCase):
        '''
        Test class to test the behavior of the Comment class
        '''

        def setUp(self):
            '''
            Set up method that will run before every Test
            '''
            self.new_comment = Comment(1, ' comment')

        def test_instance(self):
            '''
            '''
            self.assertTrue(isinstance(self.new_comment, Comment))

        def test_to_check_instance_variables(self):
            '''
            '''
            self.assertEquals(self.new_post.id, 1)
            self.assertEquals(self.new_post.description, 1)
           
                        


if __name__ == '__main__':
    unittest.main()