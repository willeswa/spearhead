""" This module contains classes for the project """

comments = []
class UserBaseClass:
    """ Defines methods common to all users """
    pass


class Moderator(UserBaseClass):
    """ Defines  """
    pass


class Admin(Moderator):
    pass


class Comments:
    def __init__(self, message, author, timestamp, replying_to):
        self.message = message
        self.author = author
        self.timestamp = timestamp
        self.relying_to = replying_to

    def create_comment(self):
        self.comments.append({
            "comment_id":len(self.comments)
            "message": self.message,
            "author": self.author
            "timestamp": self.timestamp
            "replying_to": self.replying_to
        })

    def edit_comment(self, comment_id):
        for comment in self.comments:
            if comment_id in comment.values():
                comment[message] = self.message

    def delete_comment(self, comment_id):
        for comment in self.comments:
            if comment_id in comment.values():
                del self.comments[comment]:
