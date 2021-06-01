class Account_details:
    '''
    class for the instance of the account
    '''

    list_accounts=[] #list that contains my accounts
    def __init__(self,first_name,last_name,user_name,password):
        self.first_name=first_name
        self.last_name=last_name
        self.user_name=user_name
        self.password=password
        '''
        __init__ method that helps us define properties for our objects.

        Args:
        user_name:Account user login user name
        first_name: Account user login first name.
        last_name : Account user login last name.
        pass_word:Account user login password

        '''
    def save_account(self):
         Account_details.list_accounts.append(self)

    @classmethod
    def auth_user(cls,username,password):
        '''
        auth_user returns true if login details are correct
        '''
        for account in cls.list_accounts:
            if account.user_name==username and account.password==password:
                return True
        return False

    @classmethod
    def account_exists(cls,username):
        '''
        Method that checks if an account already exists.
        Args:
            username: username to search if account already exists
        Returns :
            Boolean: True or false depending if the account exists
        '''
        for account in cls.accounts_list:
            if account.user_name==username:
                return True

        return False     

