from unittest import TestCase
from unittest.mock import patch
#from app import*
import app
from blog import Blog

class AppTest(TestCase):
    def test_menu_prints_prompt(self):
        with patch('builtins.input') as mocked_input:
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('app.print_blogs', return_value = 'q'):
                app.menu()
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

