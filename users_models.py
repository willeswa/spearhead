""" This module contains classes for the project """
import random

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
        if self.email == email and self.password == password:
            return True
        return False

    def log_in(self):
        self.is_logged_in = True
        self.last_logged_in_at = datetime.now()

    def log_out(self):
        self.is_logged_in = False



    def __init__(
            self, id, email, password, is_logged_in=False, last_logged_in_at):
        """ Initialise the class """

        self.id = id
        self.email = email
        self.password = password
        self.is_logged_in = is_logged_in
        self.last_logged_in_at = last_logged_in_at

    def verify(self, email, password):
        if self.email == email and self.password == password:
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
    """ Defines  """
    pass


class Admin(Moderator):
    """ Admin Edit and Delete Attributes """
    def __init__(self, id, email, password):
        Moderator.__init__(id, email, password)

    def can_edit(self, comment):
        return True

    def can_delete(self, comment):
        return True


class Comments:
    def __init__(self, message, author, timestamp, replying_to):
        self.message = message
        self.author = author
        self.timestamp = timestamp
        self.relying_to = replying_to
        self.comment_id = len(comments) + 1

    def create_comment(self):
        self.comments.append(self)
        return True

    def edit_comment(self, message):
        for comment in self.comments:
            if comment_id == comment.comment_id:
                self.message = message
                return True

    def delete_comment(self):
        for comment in self.comments:
            if comment_id == comment.values():
                del self.comments[comment]
                return False
