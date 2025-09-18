from unittest import TestCase
from unittest.mock import patch
#from app import*
import app
from blog import Blog
from post import Post


class AppTest(TestCase):
    def test_menu_prints_prompt(self):
        with patch('builtins.input') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        # Patch the print_blogs() function inside app.py
        with patch('app.print_blogs') as mocked_print_blogs:

            # Patch input() so that when menu() asks for user input,
            # it immediately returns 'q' (quit), avoiding an infinite loop
            with patch('builtins.input', return_value = 'q'):

                # Call the menu() function
                app.menu()

                # Verify that print_blogs() was called at least once
                mocked_print_blogs.assert_called_with()
            '''
            If app.menu() is called directly in the test, it waits for user input.
            Because of that, the function never finishes and the assert is never executed
            which makes the test hang or timeout.
            
            app.menu()
            mocked_print_blogs.assert_called()
            '''

    def test_print_blogs(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 posts)')


    def test_ask_create_blog(self):
        # Patch the built-in input() function so it doesn't wait for real user input
        with patch('builtins.input') as mocked_input:
            # Simulate two user inputs: first for the blog title, second for the author
            mocked_input.side_effect = ('Test', 'Test Author')

            # Call the function under test (from app.py)
            app.ask_create_blog()

            # Verify that the blog dictionary has a new entry with the title 'Test'
            # and that its value is not None (a Blog object was created)
            self.assertIsNotNone(app.blogs['Test'])

    def test_ask_read_blog(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
        with patch('builtins.input', return_value = 'Test'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()

                mocked_print_posts.assert_called_with(blog)

    def test_print_posts(self):
        blog = Blog('Test', 'Test Author')
        blog.create_blog('Test Post', 'Test Content')
        app.blogs = {'Test': blog}

        with patch('app.print_posts') as mocked_print_post:
            app.print_posts(blog)

            mocked_print_post.assert_called_with(blog.posts[0])

    def test_print_post(self):
        post = Post('Post title', 'Post content')
        expected_print = '''
    --- Post title ---
    Post content
    '''
        with patch('builtins.print') as mocked_print:
            app.print_post(post)
            mocked_print.assert_called_with(expected_print)
