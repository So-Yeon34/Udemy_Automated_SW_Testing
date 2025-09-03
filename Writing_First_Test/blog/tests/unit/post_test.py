'''
Terminal command
python3 -m unittest tests.unit.post_test → runs via unittest module (handles imports and test discovery)
python3 -m tests.unit.post_test → runs the file directly (may cause import issues)
'''

from unittest import TestCase # "unittest" is a built-in testing framework in Python
from post import Post

class PostTest(TestCase): # TestCase is a class provided by unittest
    def test_create_post(self):
        p = Post('Test', 'Test Content') # create a Post object

        # use the TestCase assertion methods (inherited from TestCase)

        # assertEqual(expected, actual): checks if two values are equal.
        # If 'p.title' is equal to 'Test', the test passes.
        # Otherwise, the test fails and raises an AssertionError.
        self.assertEqual('Test', p.title) # Pass result
        #self.assertEqual('Testx', p.title) #Failure result

        # Verify that the 'content' attribute is correctly assigned.
        # This ensures that the Post constructor stores the content as expected.
        self.assertEqual('Test Content', p.content) 
