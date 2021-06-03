
from account import Account_details
from credential import Credential
from termcolor import colored, cprint
import os
import time
import pickle


# Functions that implement the behaviours in account class.

def create_account(username, fname, lname, p_word):
    '''
    Function to create new account
    '''
    new_account = Account_details(username, fname, lname, p_word)
    return new_account


def save_account(account):
    '''
    Function to save account
    '''
    account.save_account()


def delete_account(account):
    '''
    Function to delete an account
    '''
    account.delete_account()


def check_account_exists(username):
    '''
    Function that check if an account with that username already exists and return a Boolean
    '''
    return Account_details.account_exists(username)


def auth_user(username, password):
    '''
    Function to authenicate user during login
    '''
    return Account_details.auth_user(username, password)

    def create_credential(page, username, password):
        
        '''
        Function to create credentials
        '''

    new_credential = Credential(page, username, password)
    return new_credential


def save_credential(credential):
    '''
    Function to save credential
    '''
    credential.save_credential()


def delete_credential(credential):
    '''
    Function to delete credential
    '''
    credential.delete_credential()


def find_cred_by_pagename(pagename):
    """
    Function that finds a credential by pagename and returns the credentials
    """
    return Credential.find_by_pagename(pagename)


def copy_cred_pass(pagename):
    '''
    Function to copy credential password            
    '''
    return Credential.copy_cred_password(pagename)


def check_credential_exists(pagename):
    '''
    Function that check if a credential exists with that pagename and return a Boolean
    '''
    return Credential.credential_exists(pagename)


def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credential.display_credentials()


def generate_password(length):
    '''
    Function that generte a random password
    '''
    return Credential.generate_password(length)


def main():

    login = False  # Set initial login value to false
    sign_name = ''  # Name of user currently logged in
    logged = True

def load_pickles():
        try:
            file_object = open('accounts.pydata', 'rb')
            Account_details.accounts_list = pickle.load(file_object)
            file_object.close()
            print("\nLOADED PICKLES ACCOUNTS")
        except:
            print("\nCLDN'T LOAD PICKLES ACCOUNTS")
            Account_details.accounts_list = []

        try:
            file_objectt = open('credentials.pydata', 'rb')
            Credential.credentials_list = pickle.load(file_objectt)
            file_object.close()
            print("\nLOADED PICKLES CREDENTIALS")
        except:
            print("\nCLDN'T LOAD PICKLES CREDENTIALS")
            Credential.credentials_list = []

def pickle_save():
        try:
            file_object = open('accounts.pydata', 'wb')
            pickle.dump(Account_details.accounts_list, file_object)
            file_object.close()
            print("\nSAVED ACCOUNTS TO PICKLE")

        except Exception as e:
            print(e)
            print("\nCOULDN'T ACCOUNTS SAVE  TO PICKLES.")

        try:
            file_objectt = open('credentials.pydata', 'wb')
            pickle.dump(display_credentials(), file_objectt)
            file_objectt.close()
            print("\nSAVED CREDENTIALS TO PICKLE")

        except Exception as e:
            print(e)
            print("\nCOULDN'T CREDENTIALS SAVE  TO PICKLES.")

def display_title():
    os.system('clear')


while logged:
        display_title()
        load_pickles()

        while login == False:
            cprint("""
        Use the following short codes to manage your password locker account 
            'ln' - Login 
            'xx' - Close app
            """, "blue")
            s_code = input(
                colored('\tWhat would you like to do? >> ', 'cyan')).lower()
            if s_code == 'ln':
                acc_code = input(
                    colored('\tDo you have an account? Y/N >> ', 'cyan')).upper()
                if acc_code == 'Y':
                    cprint(
                        '\tEnter your username and password  to login >>>\n', 'pink')
                    login_user_name = input(
                        colored('\tEnter username >> ', 'cyan'))
                    login_password = input(
                        colored('\tEnter password >> ', 'cyan'))
                    print("\n\t\tSigning in...")
                    time.sleep(1.5)
                    if auth_user(login_user_name, login_password):
                        cprint('\n\t\tLOGIN SUCCESSFUL',
                               'green', attrs=['bold'])
                        sign_name = login_user_name
                        login = True
                    else:
                        cprint('\n\t\tSORRY COULD NOT VERIFY',
                               'red', attrs=['bold'])

                elif acc_code == 'N':
                    cprint(
                        '\tEnter your username,firstname,lastname and password  to register account >>>\n', 'blue')
                    reg_user_name = input(
                        colored('\tEnter username >> ', 'cyan'))
                    reg_f_name = input(
                        colored('\tEnter firstname >> ', 'cyan'))
                    reg_l_name = input(colored('\tEnter lastname >> ', 'cyan'))
                    reg_password = input(
                        colored('\tEnter password >> ', 'cyan'))
                    print("\n\t\tRegistering ...")
                    time.sleep(1.5)
                    if check_account_exists(reg_user_name):
                        cprint(
                            f"\n\t\tACCOUNT WITH, {reg_user_name.upper()} USERNAME ALREADY CREATED", "red", attrs=['bold'])
                    else:
                        new_acc = create_account(
                            reg_user_name, reg_f_name, reg_l_name, reg_password)
                        save_account(new_acc)

                        cprint(
                            "\n\t\tCONGRATULATIONS, YOUR ACCOUNT HAS BEEN CREATED", "green", attrs=['bold'])
                        cprint("\n\tSign into your new account", "blue")
                        sign_username = input(
                            colored('\n\tEnter username >> ', 'cyan'))
                        sign_password = input(
                            colored('\n\tEnter password >> ', 'cyan'))
                        print("\n\t\tSigning in ...")
                        time.sleep(1.5)
                        if auth_user(sign_username, sign_password):
                            cprint("\n\t\tLOGIN SUCCESSFUL",
                                   "green", attrs=['bold'])
                            sign_name = sign_username
                            login = True
                        else:
                            cprint('\n\t\tSORRY COULD NOT VERIFY USER',
                                   'red', attrs=['bold'])
                else:
                    cprint('\n\t\tPLEASE USE THE GIVEN SHORT CODES',
                           'red', attrs=['bold'])
            elif s_code == 'xx':
                cprint(f"""\n\t\tTHANK YOU FOR USING PASSWORD LOCKER
        \t\tBye...
        \t\t\t\t\tClosing App >>>>>
        """, "red", attrs=['bold'])
                pickle_save()
                time.sleep(1.5)
                logged = False
                break
            else:
                cprint('\n\t\tPLEASE USE THE GIVEN SHORT CODES',
                       'red', attrs=['bold'])