from .models import UserProfile, BankAccount, Transaction 
import random
# Following lists are for data seeding 

FIRST_NAMES = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda",
            "William", "Elizabeth", "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica",
            "Thomas", "Sarah", "Christopher", "Karen", "Daniel", "Nancy", "Matthew", "Lisa",
            "Anthony", "Betty", "Mark", "Margaret", "Donald", "Sandra", "Steven", "Ashley",
            "Paul", "Kimberly", "Andrew", "Emily", "Joshua", "Donna", "Kenneth", "Michelle"
            ]

LAST_NAMES = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis",
            "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas",
            "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson", "White",
            "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker", "Young",
            "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores"
            ]

ACCOUNT_TYPES = ["Savings", "Checking", "Business", "Investment"]

TRANSACTION_TYPES = ["Deposit", "Withdrawal", "Transfer"]

DOMAINS = ["gmail.com", "yahoo.com", "outlook.com"]

TRANSACTION_DESCRIPTION = [ "ATM Withdrawal", "Direct Deposit", "Online Purchase", "Bill Payment",
            "Cash Deposit", "Wire Transfer", "Check Deposit", "Salary Payment",
            "Refund", "Subscription Payment", "Grocery Shopping", "Gas Station"
            ]

"""
Following functions are to generate random model objects
"""
#Creating name, email, phone no and password
def GenereateRandomUser(admin_chance):
    
    first_name = FIRST_NAMES[random.randrange(0, len(FIRST_NAMES))]
    last_name = LAST_NAMES[random.randrange(0,len(LAST_NAMES))]
    full_name = f'{first_name} {last_name}'

    email_name = f'{first_name.lower}.{last_name.lower}{random.randrange(1,999)}'
    domain = DOMAINS[random.randrange(0, len(DOMAINS))]
    email = f'{email_name}${domain}'


    phone_number = '04' + str(random.randrange(0,9)) + '-' + str(random.randrange(100,999)) + '-' + str(random.randrange(1000, 9999))
    
    password = GenerateRandomPassword()

    isAdmin = True if random.random() < admin_chance else False

    return UserProfile(name=full_name, email=email, )
    


# Function to create random models 
def SeedDatabase(number_of_users = 50, accounts_per_user = 2, transactions_per_account = 10, admin_chance = 0.1):
    print("Starting database seeding")