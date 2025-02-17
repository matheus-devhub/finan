# Importing SQLite
import sqlite3 as lite
import pandas as pd

# Creating connection
con = lite.connect('finan.db')

# FUNCTIONS TO INSERT-------------------------------------------------------------------

# Inserting category
def inserting_category(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Category (name) VALUES (?)"
        cur.execute(query, i)

# Inserting revenues
def inserting_revenues(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Revenues (category, added_in, value) VALUES (?,?,?)"
        cur.execute(query, i)

# Inserting expenses
def inserting_expenses(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Expenses (category, removed_in, value) VALUES (?,?,?)"
        cur.execute(query, i)

# FUNCTIONS TO DELETE-------------------------------------------------------------------

# Deleting revenues
def delete_revenues(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Revenues WHERE id=?"
        cur.execute(query, i)

def delete_expenses(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Expenses WHERE id=?"
        cur.execute(query, i)

# FUNCTIONS TO VIEW DATA-------------------------------------------------------------------

# View category
def view_category():
    itens_list = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Category")
        row = cur.fetchall()
        for i in row:
            itens_list.append(i)
            
    return itens_list

# View revenues
def view_revenues():
    itens_list = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Revenues")
        row = cur.fetchall()
        for i in row:
            itens_list.append(i)

    return itens_list

# View expenses
def view_expenses():
    itens_list = []

    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Expenses")
        row = cur.fetchall()
        for i in row:
            itens_list.append(i)

    return itens_list

# Functions for table data
def table():
    expenses = view_expenses()
    revenues = view_revenues()

    table_list = []

    for i in expenses:
        table_list.append(i)
    
    for i in revenues:
        table_list.append(i)
    
    return table_list

# Functions for graph data
def values_bar():
    # Total Revenue
    revenues = view_revenues()
    revenues_list = []

    for i in revenues:
        revenues_list.append(i[3])

    total_revenue = sum(revenues_list)
    
    # Total Expense
    expenses = view_expenses()
    expenses_list = []

    for i in expenses:
        expenses_list.append(i[3])

    total_expense = sum(expenses_list)

    # Total Balance
    total_balance = total_revenue - total_expense

    return [total_revenue, total_expense, total_balance]

# Graph pie function
def graph_values():
    expenses = view_expenses()
    table_list = []
    for i in expenses:
        table_list.append(i)

    dataframe = pd.DataFrame(table_list, columns = ['id', 'category', 'date', 'value'])

    # Get the sum of the durations per month
    dataframe = dataframe.groupby('category')['value'].sum()

    qty_list = dataframe.values.tolist()
    categories_list = []

    for i in dataframe.index:
        categories_list.append(i)

    return([categories_list, qty_list])

# Percentage Function
def percentage_values():
    # Total Revenue
    revenues = view_revenues()
    revenues_list = []

    for i in revenues:
        revenues_list.append(i[3])

    total_revenue = sum(revenues_list)
    
    # Total Expense
    expenses = view_expenses()
    expenses_list = []

    for i in expenses:
        expenses_list.append(i[3])

    total_expense = sum(expenses_list)

    # Total Percentage
    if total_revenue == 0:
        total = 0  # Ou um valor padrão para evitar a divisão por zero
    else:
        total = ((total_revenue - total_expense) / total_revenue) * 100

    return total
