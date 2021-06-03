
from account import Account_details
from credential import Credential
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
    