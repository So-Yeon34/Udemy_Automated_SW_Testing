from video_code.app import MENU_PROMPT

MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, "q" to quit: '
blogs=dict() #dictionary or {} (but, avoid to confuse set, using dict())

def menu():
    print_blogs() #Show the user the available blogs
    selection = input(MENU_PROMPT) #Let the user make a choice
'''
Do something with that choice
Eventually exit
'''


def print_blogs():
    # Print the available blogs
    for key, blog in blogs.items(): #(blog_name, Blog), (blog_name, Blog)
        print('- {}'.format(blog))