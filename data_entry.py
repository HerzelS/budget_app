from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}
SUB_CATEGORIES = {"f_1": "food", "u_1":"utilities"}

def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("Invalid date format. Please enter the date in dd-mm-yy format")
        return get_date(prompt, allow_default) # recurssive function

def get_amount():
    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount() # rucurse function

def get_category():
    category = input("Enter the category ('I' for Income or 'E'  for expense.): ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]

    print("Invalid category. Please enter 'I' for Income or 'E' for Expense")
    return get_category()

def get_description():
    return input("Enter a description: ")


def get_sub_category():
    sub_category = input("Enter sub category: ").lower()
    if sub_category in SUB_CATEGORIES:
        return[sub_category.value()]
    
    print("Invalid response. Try again")
    get_sub_category()


def get_allocation():
    pass

def get_month():
    d = get_date("please enter date: ", allow_default=True)


for key, sub_category in SUB_CATEGORIES.items():
        print(sub_category)
