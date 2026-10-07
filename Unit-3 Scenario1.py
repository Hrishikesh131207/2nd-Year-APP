import csv
import re

FILE_NAME = "customers.csv"

def load_customers():
    customers = []

    try:
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                customers.append(row)

    except FileNotFoundError:
        print(f"Error: {FILE_NAME} not found.")

    return customers


def display_customers(customers):
    if not customers:
        print("No customer records found.")
        return

    print("\n--- All Customer Details ---")

    for customer in customers:
        print(f"Account Number : {customer['Account Number']}")
        print(f"Name           : {customer['Name']}")
        print(f"Address        : {customer['Address']}")
        print(f"Phone          : {customer['Phone']}")
        print(f"Balance        : {customer['Balance']}")
        print("-" * 35)


def validate_account_number(account_number):
    pattern = r"^\d{10}$"
    return re.fullmatch(pattern, account_number) is not None


def search_customer(customers):
    account_number = input("Enter Account Number: ").strip()

    if not validate_account_number(account_number):
        print("Invalid account number!")
        print("Account number must contain exactly 10 digits.")
        return

    for customer in customers:
        if customer["Account Number"] == account_number:
            print("\n--- Customer Found ---")
            print(f"Account Number : {customer['Account Number']}")
            print(f"Name           : {customer['Name']}")
            print(f"Address        : {customer['Address']}")
            print(f"Phone          : {customer['Phone']}")
            print(f"Balance        : {customer['Balance']}")
            return

    print("Customer with this account number was not found.")


def main():
    customers = load_customers()

    while True:
        print("\n===== Bank Customer Record System =====")
        print("1. Display All Customer Details")
        print("2. Search Customer by Account Number")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_customers(customers)

        elif choice == "2":
            search_customer(customers)

        elif choice == "3":
            print("Thank you for using the Bank Customer Record System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
