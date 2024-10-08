class Post:
    def __init__(self, id, title, body, subtitle, author, image, time_stamp) -> None:
        self.id = id
        self.title = title
        self.subtitle = subtitle
        self.body = body
        self.author = author
        self.image = image
        self.time_stamp = time_stamp
        