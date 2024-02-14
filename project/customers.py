import os
import re

class SophisticatedArray:
    def __init__(self, array):
        self.array = array

    def deny_access(self):
        size = len(self.array)
        start_index = int(size * 0.1)
        denied_access = self.array[:start_index]
        self.array[:start_index] = ['DENIED_ACCESS'] * start_index
        return denied_access

    def __str__(self):
        return str(self.array)

def file_exists(file_path):
    return os.path.exists(file_path)

def create_file(file_path):
    with open(file_path, 'w') as file:
        pass

def read_usernames_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

def process_users_even_rows(user_array):
    return [user for i, user in enumerate(user_array) if i % 2 == 1]

def is_valid_email(email):
    # Basic email validation using regular expression
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def get_gmail_addresses(email_addresses):
    return [email for email in email_addresses if email.endswith('@gmail.com')]

def match_name_email(all_user, gmail_addresses):
    usernames_emails_set = {}
    for name, letter in zip(all_user, gmail_addresses):
        if name.lower() in letter.lower():
            usernames_emails_set[name] = letter
    return usernames_emails_set



def convert_and_count_A(name):
    # Adding a comma as a separator
    converted_name = ','.join(str(ord(char)) for char in name)
    print(f'converted_name {converted_name}')

    # Splitting the values using the comma separator
    converted_back = ''.join(chr(int(converted_char)) for converted_char in converted_name.split(','))
    print(f'converted_back {converted_back}')

    return converted_back.upper().count('A')

def capitalize_variable_names(variable_names):
    return [name.upper() for name in variable_names]

def calculate_payment(team_members):
    payment = 0
    for i, member in enumerate(team_members, 1):
        if i % 8 == 0:
            payment += 200
        elif i > (len(team_members) // 8) * 8:
            payment += 50
    return payment

# a. Check if the file exists, if not, create one
file_path = 'data/users.txt'
if not file_exists(file_path):
    create_file(r'C:\Users\user1\pythonProject\pythonProject1\project\New.txt')

# b. Read usernames into a generator
usernames_generator = read_usernames_generator(r'C:\Users\user1\pythonProject\pythonProject1\project\UsersName.txt')
user_array = list(usernames_generator)
all_user =list(read_usernames_generator(r'C:\Users\user1\pythonProject\pythonProject1\project\UsersName.txt'))
sophisticated_array = SophisticatedArray(user_array)
denied_usernames = sophisticated_array.deny_access()

# d. Implement function for users in even rows
even_rows_users = process_users_even_rows(user_array)
even_rows_users = SophisticatedArray(even_rows_users)
even_rows_users.deny_access()

# e. Read and validate email addresses
email_addresses = read_usernames_generator(r'C:\Users\user1\pythonProject\pythonProject1\project\UsersEmail.txt')
valid_email_addresses = [email for email in email_addresses if is_valid_email(email)]

# f. Function to return Gmail email addresses
gmail_addresses = get_gmail_addresses(valid_email_addresses)

# g. Match usernames and email addresses
name_email = match_name_email(all_user,valid_email_addresses)
print(name_email)
# h. Function to check user's name and count occurrences of letter 'A'
user_name = 'Devorah'
count_A = convert_and_count_A(user_name)
print(f'countA in {user_name} is in upper {user_name.upper()}: {count_A}')

# i. Capitalize variable names
variable_names = usernames_generator
capitalized_names = capitalize_variable_names(variable_names)

# j. Calculate payment for team members
team_members = list(range(1, 101))  # Assuming 100 team members
payment_amount = calculate_payment(team_members)

# Print results for demonstration
print("Even Rows Users:", even_rows_users)
print("Valid Email Addresses:", valid_email_addresses)
print("Gmail Addresses:", gmail_addresses)
print("Count of 'A' in User Name:", count_A)
print("Capitalized Variable Names:", capitalized_names)
print("Payment Amount:", payment_amount)