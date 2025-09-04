class Post:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def __repr__(self):
        pass

    # dictionary
    def json(self):
        return {
            'title' : self.title,
            'content' : self.content,
        }

