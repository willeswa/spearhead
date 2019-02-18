""" Tests on the spearhead project """
import unittest
from .users_models import UserBaseClass ,Comments



class TestUserModels(unittest.TestCase):
    """ All user module tests """

    def setUp(self):
        """ Create common variables among all tests """

        self.user = UserBaseClass(123, "bedank6@gmail.com", "siriyangu")
        self.comment = Comments("message", "author", "timestamp", "replying_to")

    def test_user_login(self):
        """ Tests whether the user is logged in """

        self.user.log_in()
        self.assertTrue(self.user.is_logged_in)
        self.assertTrue(self.user.last_logged_in_at)

    def test_user_not_logged_in(self):
        """ Tests the default case of user not logged in """

        self.assertFalse(self.user.is_logged_in)
        self.assertFalse(self.user.last_logged_in_at)

    def test_verify_credentials(self):
        """ Tests verify credentials """

        self.assertTrue(self.user.verify("bedank6@gmail.com", "siriyangu"))

    def test_verify__false_credentials(self):
        """ Tests verify false credentials """

        self.assertTrue(self.user.verify("bedank6@gmail.com", "siriyako"))


    def test_comments(self):
        """ Tests the comments """
        self.assertTrue(self.comment.create_comment())
        self.assertTrue(self.comment.edit_comment("0"))
        self.assertTrue(self.comment.delete_comment("0"))

