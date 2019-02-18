from datetime import datetime
from random import randint
""" This module contains classes for the project """


class UserBaseClass:
    """ Defines methods common to all users """

    def __init__(
            self, email, password, last_logged_in_at=None,
            is_logged_in=False):
        """ Initialise the class """

        self.id = randint(0, 100)
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

    def can_delete(self):
        return False


class Moderator(UserBaseClass):
    """ Defines  """
    pass


class Admin(Moderator):
    pass


class Comments:
    pass
