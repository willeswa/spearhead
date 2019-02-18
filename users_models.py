""" This module contains classes for the project """


class UserBaseClass:
    """ Defines methods common to all users """
    pass


class Moderator(UserBaseClass):
    """ Moderator Edit and Delete Attributes """
    def __init__(self, id, email, password):
        UserBaseClass.__init__(id, email, password)

    def can_delete(self, comment):
        return True


class Admin(Moderator):
    pass


class Comments:
    pass
