import csv
from datetime import datetime
import matplotlib.pyplot as plt
categories=["Food","Transport","Bills","Shopping","Entertainment","Misc"]
def parse_date(date_str):
    return datetime.strptime(date_str,"%Y-%m-%d")
def parse_amount(amt):
    amount=float(amt)
    if amount<0:
        raise ValueError("Amount should not be negative")
    return round(amount,2)
def add_expense():
    print("\n--- Add New Expense ---")
    while True:
        date_in=input("enter date in (YYYY-MM-DD):").strip()
        try:
            date=parse_date(date_in)
            break
        except Exception as e:
            print("Invalid date. PLease use YYYY-MM-DD format.")
    while True:
        amount_in=input("enter amount:").strip()
        try:
            amount=parse_amount(amount_in)
            break
        except Exception:
            print("Invalid amount. Please enter amount like 440 or 50.00")
    print("\nChoose cataegory")
    for i, cat in enumerate(categories, start=1 ):
        print(f"{i}.{cat}")
    while True:
        try:
            choice=int(input("enter category number:"))
            if 1 <= choice <= len(categories):
                category = categories[choice - 1]
                break
            else:
                print("Choose a valid number from the list.")
        except Exception:
            print("Enter a number (e.g., 1)")
    notes = input("Notes (optional): ").strip()
    with open("expenses.csv","a",newline="") as file:
        writer=csv.writer(file)
        writer.writerow([date.strftime("%Y-%m-%d"),amount,category,notes])
    print("\nExpense added successfully!\n")
def view_expense():
    try:
        with open("expenses.csv","r",newline='') as file:
            reader=csv.reader(file)
            rows=list(reader)
    except:
        print("file does not exist")
        return
    if not rows or len(rows)<=1:
        print("no records found")
        return
    print("-"*20,"EXPENSE RECORD","-"*20)
    print("-"*50)
    print("DATE     AMOUNT     CATEGORY     NOTES")
    print("-"*50)
    for i,row in enumerate(rows[1:],start=1):
        date, amount, category, notes = row
        print(f"{date}   {amount}   {category}   {notes}")
    print("-"*50)
def summary():
    try:
        with open("expenses.csv","r",newline="") as file:
            reader=csv.reader(file)
            rows=list(reader)
    except:
        print("file not found")
        return
    if not rows or len(rows)<=1:
        print("no expenses found")
        return
    category_totals={"Food":0,"Transport":0,"Bills":0,"Shopping":0,"Entertainment":0,"Misc":0}
    total_expense=0
    for row in rows[1:]:
        date,amount,category,notes=row
        flt_amount=float(amount)
        total_expense+=flt_amount
        category_totals[category]+=flt_amount
    print("-"*20,"SUMMARY","-"*20)
    print("Total spent:",total_expense)
    print("Category-wise expenditure:")
    for category in category_totals:
        print(category,category_totals[category])
def monthly_summary():
    month=int(input("enter month(1-12):"))
    year=int(input("enter year(YYYY):"))
    try:
        with open("expenses.csv","r",newline="") as file:
            reader=csv.reader(file)
            rows=list(reader)
    except:
        print("file not found")
        return
    if not rows or len(rows)<=1:
        print("no expenses found")
        return
    monthly_totals={"Food":0,"Transport":0,"Bills":0,"Shopping":0,"Entertainment":0,"Misc":0}
    monthly_expense = 0
    count = 0
    for row in rows[1:]:
        date,amount,category,notes=row
        dt=datetime.strptime(date,"%Y-%m-%d")
        if dt.month==month and dt.year==year:
            amt=float(amount)
            monthly_expense+=amt
            monthly_totals[category]+=amt
            count+=1
    if count == 0:
        print("no expenses found for this month")
        return

    print("-"*20,"MONTHLY SUMMARY","-"*20)
    print("Total expenditure in",month,"of",year,"was:",monthly_expense)
    print("Category-wise expenditure was:")
    for category in monthly_totals:
        print(category,monthly_totals[category])
def show_charts():
    try:
        with open("expenses.csv", "r", newline="") as file:
            reader = csv.reader(file)
            rows = list(reader)
    except:
        print("file not found")
        return

    if not rows or len(rows) <= 1:
        print("no expenses to display charts")
        return
    category_totals = {"Food": 0, "Transport": 0, "Bills": 0,
                       "Shopping": 0, "Entertainment": 0, "Misc": 0}

    for row in rows[1:]:
        date, amount, category, notes = row
        category_totals[category] += float(amount)
    labels = list(category_totals.keys())
    values = list(category_totals.values())
    plt.figure(figsize=(8,5))
    plt.bar(labels, values)
    plt.title("Total Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount Spent")
    plt.tight_layout()
    plt.show()
    plt.figure(figsize=(7,7))
    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.title("Expense Distribution")
    plt.tight_layout()
    plt.show()
add_expense()
view_expense()
summary()
monthly_summary()
show_charts()









      
        





