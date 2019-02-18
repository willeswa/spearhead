from datetime import datetime
""" This module contains classes for the project """

comments = []
class UserBaseClass:
    """ Defines methods common to all users """
    
    def __init__(
            self, id, email, password, is_logged_in=False, last_logged_in_at):
        """ Initialise the class """

        self.id = id
        self.email = email
        self.password = password
        self.is_logged_in = is_logged_in
        self.last_logged_in_at = last_logged_in_at

    def verify(self, email, password):
        if self.email == email and self.password = password:
            return True
        return False

    def log_in(self):
        self.is_logged_in = True
        self.last_logged_in_at = datetime.now()

    def log_out(self):
        self.is_logged_in = False

    def can_edit(self, comment):
        return comment.author == self.id

    def can_delete():
        return False


class Moderator(UserBaseClass):
    """ Moderator Edit and Delete Attributes """
    def __init__(self, id, email, password):
        UserBaseClass.__init__(id, email, password)

    def can_delete(self, comment):
        return True


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
