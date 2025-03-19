import sqlite3 as lite
import pandas as pd

# Creating connection
con = lite.connect('finan.db')

# INSERT FUNCTIONS -------------------------------------------------------------------

# Insert category
def inserting_category(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Category (name) VALUES (?)"
        cur.execute(query, i)

# Insert revenues
def inserting_revenues(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Revenues (category, added_in, value) VALUES (?,?,?)"
        cur.execute(query, i)

# Insert expenses
def inserting_expenses(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Expenses (category, removed_in, value) VALUES (?,?,?)"
        cur.execute(query, i)

# DELETE FUNCTIONS -------------------------------------------------------------------

# Deleting revenues
def delete_revenues(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Revenues WHERE id=?"
        cur.execute(query, i)

# Deleting expenses
def delete_expenses(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Expenses WHERE id=?"
        cur.execute(query, i)

# VIEW DATA FUNCTIONS -------------------------------------------------------------------

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
    revenues = sum([i[3] for i in view_revenues()])
    expenses = sum([i[3] for i in view_expenses()])
    return [revenues, expenses, revenues - expenses]

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
def percentage_value():
    revenues = sum([i[3] for i in view_revenues()])
    expenses = sum([i[3] for i in view_expenses()])

    if revenues == 0:
        return [0]  # Evita divisão por zero

    return [((revenues - expenses) / revenues) * 100]







    