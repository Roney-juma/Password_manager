import random
import string
import pyperclip


class Credential:
    """
    Class that generates an instance of a Credential
    """

    def __init__(self, page_name, user_name, password):
        '''
        __init__ method that helps us define properties for our objects.
        Args:
            page_name:Name of page or account you want to save credentials for
            user_name:Username of page you want to save
            pass_word:Password of page you want to save
        '''
        self.page_name = page_name
        self.user_name = user_name
        self.password = password

    list_account = []  # Empty credentials list

    