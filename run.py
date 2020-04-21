#!/usr/bin/env python3.6
import pyperclip
from credentials import User, Credentials

def create_user(fname, lname, password):
    '''
    Function that create a new user account.
    '''
    new_user = User(fname, lname, password)
    return new_user

def save_user(user):
    '''
    Function that saves a new user created.
    '''
    User.save_user(user)

def verify_user(first_name, password):
    '''
    Function that confirms is the user exist.
    '''
    confirming_user = User.confirm_user(first_name, password)
    return confirming_user

def generate_password(password):
    '''
    Fucntion that automatically generate incase user do not want to create  one.
    '''
    pass_generator= Credentials.password_generator(password)
    return pass_generator


def create_credential(user_name, site_name, account_name, password):
    '''
    Function that creates in new credentials.
    '''
    new_credential = Credentials(user_name, site_name, account_name, password)
    return new_credential


def save_credential(credential):
    '''
    Function that save new created credential.
    '''
    Credentials.save_credential(credential)


def display_credentials(username):
    '''
    Fucntion that display all saved credentials.
    '''
    return Credentials.display_credential(username)


def copy_credential(site_name):
    '''
    Function that copies credential by site_name.
    '''
    return Credentials.copy_credential(site_name)


def find_by_site(site_name):
    '''
    Function that searches site name from the list.
    '''
    return Credentials.find_by_site_name(site_name)

def delete_credential(credential):
    '''
    Function that deletes credential from credential list.
    '''
    credential.delete_credential()

def check_existing_credentials(site_name):
    '''
    Function that check if a credential already exist in credential list.
    '''
    return Credentials.credential_exist(site_name)

    
def main():
    print('\n')

    print("")
    print("Genius, Welcome to Password-Locker.") 
    while True:
        print("-"*120)
        print('\n')
        print("Use these short codes: \n CRA - Create an account \n LI - Log In \n QT - Quite")
        print('\n')
        short_code = input("Enter your choice: ").upper().strip()

        if short_code == "QT":
            break

        elif short_code == "CRA":
            print('\n')
            print("."*120)
            print('\n')
            print("To create a new account:")
            first_name = input("Kindly Enter your first name ").strip()
            last_name = input("Kindly Enter your last name ").strip()
            password = input("Kindly Enter password ").strip()
            save_user(create_user(first_name, last_name, password))
            print("\n")
            print(f"Account for {first_name} {last_name}, password {password} has been successfully created")
        
        elif short_code == "LI":
            print("."*120)
            print('\n')
            print("Enter your valid account details to log in.")
            user_name = input("Kindly Enter your first name ").strip()
            password = str(input("Kindly Enter your password "))
            user_exists = verify_user(user_name, password)
            if user_exists == user_name:
                print('\n')
                print(f"{user_name}, Enter your choise to continue.")
                while True:
                    print("."*120)
                    print("Use these codes: \n CCR - To create a credential \n DAC - To display all your credentials \n FCR - To find a credential \n CP - To copy password \n DEL - To delete a credential \n QT - Quite")
                    print('\n')
                    short_code = input('Enter your choice: ').upper().strip()
                    print("-"*60)
                    if short_code == "QT":
                        print('\n')
                        print(f"{user_name}, Welcome next time")
                        break
                    elif short_code == 'CCR':
                        print('\n')
                        print("Enter your valid credential details:")
                        site_name = input("Enter the site name ").strip()
                        account_name = input("Enter your account username ").strip()

                        while True:
                            print('\n')
                            print("."*120)
                            print("Choose method: \n EP - To enter password \n GP - To generate password \n QT - Quite")
                            password_choice = input("Enter method: ").upper().strip()
                            print("-"*120)
                            if password_choice == "EP":
                                print('\n')
                                password = input("Enter password: ").strip()
                                break
                            elif password_choice == "GP":
                                password = generate_password(password)
                                break
                            elif password_choice == "QT":
                                break
                            else:
                                print("Wrong option.Try again.")
                        save_credential(create_credential(user_name, site_name, account_name,password))
                        print('\n')
                        print(f"Credential created for: \n Site: {site_name} - Account Username: {account_name} - Password: {password}")

                    elif short_code == 'DAC':
                        print('\n')

                        if display_credentials(user_name):
                            print("Your credentials include:")
                            print('\n')
                            for credential in display_credentials(user_name):
                                print(f"Site : {credential.site_name} - Account name: {credential.account_name} - Password: {credential.password}")
                        else:
                            print('\n')
                            print("No saved credential.")
                            print('\n')


                    elif short_code == 'FCR':
                        search_site = input("Enter the site name to search:  \n")
                        if check_existing_credentials(search_site):
                            result = find_by_site(search_site)
                            print(f"Result: Site: {result.site_name} - Account name: {result.account_name} - Password: {result.password}")
                        else:
                            print("Unexisting credential.")
                    
                    elif short_code == "CP":
                        print('\n')
                        chosen_site = input("Enter site name for credential you want to copy: ")
                        copy_credential(chosen_site)
                        print('\n')
                    elif short_code == "DEL":
                        print('\n')
                        print("Enter site of credential to be deleted. ")
                        print('\n')
                        answer = input("Enter Your choice: ")

                        if check_existing_credentials(answer):
                            answer = find_by_site(answer)
                            delete_credential(answer)
                            print("Seleced credentials has beed deleted!")

                        else:
                            ("Unexisting credentila!")
                        
                    else:
                        print("Incorrect option. Try again.")
                
            else:
                print("-"*120)
                print('\n')
                print("Use short codes for selecting options.")


if __name__ == '__main__':
    main()