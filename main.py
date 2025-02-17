from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.ttk import Progressbar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from tkcalendar import Calendar, DateEntry
from datetime import date
from view import values_bar, graph_values, percentage_values, inserting_category, view_category, inserting_revenues, inserting_expenses, table, delete_expenses, delete_revenues


# Colors ----------------------------------------------------------------------------------------------------
co0 = "#2e2d2b" # white
co1 = "#feffff" # black
co2 = "#4fa882" # mint
co3 = "#38576b" # vista blue
co4 = "#403d3d" # auburn
co5 = "#e06636"
co6 = "#038cfc"
co7 = "#3fbfb9"
co8 = "#263238"
co9 = "#e9edf5"

colors = ['#5588bb', '#66bbbb', '#99bb55', '#ee9944', '#444466', '#bb5555']

# Creating window ----------------------------------------------------------------------------------------------------
window = Tk()
window.title()
window.geometry('900x650')
window.configure(background=co9)
window.resizable(width=FALSE, height=FALSE)

style = ttk.Style(window)
style.theme_use("clam")

# Frames ----------------------------------------------------------------------------------------------------
upFrame = Frame(window, width=1043, height=50, bg=co1, relief="flat")
upFrame.grid(row=0, column=0)

midFrame = Frame(window, width=1043, height=361, bg=co1, pady=20, relief="raised")
midFrame.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

downFrame = Frame(window, width=1043, height=300, bg=co1, relief="flat")
downFrame.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)

incomeFrame = Frame(downFrame, width=300, height=250, bg=co1)
incomeFrame.grid(row=0, column=0)

operationsFrame = Frame(downFrame, width=220, height=250, bg=co1)
incomeFrame.grid(row=0, column=1, padx=5)

configFrame = Frame(downFrame, width=220, height=250, bg=co1)
incomeFrame.grid(row=0, column=2, padx=5)

frame_gra_pie = Frame(midFrame, width=580, height=250, bg=co2)
frame_gra_pie.place(x=415, y=5)

# Apps ----------------------------------------------------------------------------------------------------
# Acessing the image
app_img = Image.open('./img/logo.webp')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(upFrame, image=app_img, text=" Finan", width=900, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)

# Defining tree as global
global tree

# Insert category function
def insert_category_2():
    name = entry_category.get()
    insert_list = [name]

    for i in insert_list:
        if i=='':
            messagebox.showerror('Error', 'Fill in all fields')
            return
    # passing list to the insert function present in view
    inserting_category(insert_list)

    messagebox.showinfo('Success', 'The data was entered successfully')

    entry_category.delete(0,'end')

    # Cathcing the category values
    function_categories = view_category()
    category = []

    for i in function_categories:
        category.append(i[1])

    # updating categories list
    combo_expenses_category['values'] = (category)

# insert revenues function
def insert_revenues_2():
    name = 'Revenue'
    date = entry_calendar_revenues.get()
    qty = entry_revenues_value.get()

    insert_list = [name, date, qty]

    for i in insert_list:
        if i=='':
            messagebox.showerror('Error', 'Fill in all fields')
            return
    # calling the insert revenues function present in view
    inserting_revenues(insert_list)

    messagebox.showinfo('Success', 'The data was entered successfully')

    entry_calendar_revenues.delete(0,'end')
    entry_revenues_value.delete(0,'end')

    # updating data
    showIncome()
    percentage()
    graphic_bar()
    summary()
    pie_graph()

# insert expenses function
def insert_revenues_2():
    name = combo_expenses_category.get()
    date = entry_calendar_expenses.get()
    qty = entry_expenses_value.get()

    insert_list = [name, date, qty]

    for i in insert_list:
        if i=='':
            messagebox.showerror('Error', 'Fill in all fields')
            return
    # calling the insert expenses function present in view
    inserting_expenses(insert_list)

    messagebox.showinfo('Success', 'The data was entered successfully')

    combo_expenses_category.delete(0, 'end')
    entry_calendar_expenses.delete(0,'end')
    entry_expenses_value.delete(0,'end')

    # updating data
    showIncome()
    percentage()
    graphic_bar()
    summary()
    pie_graph()

# Delete function
def delete_data():
    try:
        treev_data = tree.focus()
        treev_dictionary = tree.item(treev_data)
        treev_list = treev_dictionary['values']
        value = treev_list[0]
        name = treev_list[1]

        if name == 'Revenues':
            delete_revenues([value])
            messagebox.showinfo('Success', 'The data was successfully delete')

            # updating data
            showIncome()
            percentage()
            graphic_bar()
            summary()
            pie_graph()

        else:
            delete_expenses([value])
            messagebox.showinfo('Success', 'The data was successfully delete')

            # updating data
            showIncome()
            percentage()
            graphic_bar()
            summary()
            pie_graph()
    except IndexError:
        messagebox.showerror('Error', 'Select one of the data from the table')

# Monthly income table
app_table = Label(midFrame, text="Income and expenses table", anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
app_table.place(x=5, y=309)

# Expenses configurations ----------------------------------------------------------------------------------------------------
label_info = Label(downFrame, text='Insert new expenses', height=1, anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co4)
label_info.place(x=370, y=0)

# Category
label_category = Label(downFrame, text='Category', height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
label_category.place(x=370, y=30)

# Selecting categories
category_function = view_category()
category = []

for i in category_function:
    category.append(i[1])

combo_expenses_category = ttk.Combobox(downFrame, width=10, font=('Ivy 10'))
combo_expenses_category['values'] = (category)
combo_expenses_category.place(x=460, y=35)

# Calendar
label_calendar_expenses = Label(downFrame, text='Date', height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
label_calendar_expenses.place(x=370, y=70)
entry_calendar_expenses = DateEntry(downFrame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2022)
entry_calendar_expenses.place(x=460, y=71)

# Value
label_expenses_value = Label(downFrame, text='Total QTY', height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
label_expenses_value.place(x=370, y=100)
entry_expenses_value = Entry(downFrame, width=14, justify='left', relief='solid')
entry_expenses_value.place(x=460, y=101)

# Add Btn expenses
add_expenses_img = Image.open('./img/addBtn.png')
add_expenses_img = add_expenses_img.resize((17,17))
add_expenses_img = ImageTk.PhotoImage(add_expenses_img)
add_expenses_btn = Button(downFrame, command=insert_revenues_2, image=add_expenses_img, text=" Add".upper(), width=80, compound=LEFT, anchor=NW, font=('Ivy 7 bold'), bg=co1, fg=co0, overrelief=RIDGE)
add_expenses_btn.place(x=460, y=131)

# Remove Btn
label_remove = Label(downFrame, text='Remove action', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
label_remove.place(x=370, y=190)

remove_img = Image.open('./img/removeBtn.png')
remove_img = remove_img.resize((17,17))
remove_img = ImageTk.PhotoImage(remove_img)
remove_btn = Button(downFrame, command=delete_data, image=remove_img, text=" Remove".upper(), width=80, compound=LEFT, anchor=NW, font=('Ivy 7 bold'), bg=co1, fg=co0, overrelief=RIDGE)
remove_btn.place(x=470, y=190)

# Revenues configurations ----------------------------------------------------------------------------------------------------
label_info = Label(downFrame, text='Insert new revenues', height=1, anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co4)
label_info.place(x=600, y=0)

# Calendar
label_calendar_revenues = Label(downFrame, text='Date', height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
label_calendar_revenues.place(x=600, y=30)
entry_calendar_revenues = DateEntry(downFrame, width=12, background='darkblue', foreground='white', borderwidth=2, year=2022)
entry_calendar_revenues.place(x=670, y=31)

# Value
label_revenues_value = Label(downFrame, text='Total QTY', height=1, anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
label_revenues_value.place(x=600, y=70)
entry_revenues_value = Entry(downFrame, width=14, justify='left', relief='solid')
entry_revenues_value.place(x=670, y=71)

# Add Btn
add_revenues_img = Image.open('./img/addBtn.png')
add_revenues_img = add_revenues_img.resize((17,17))
add_revenues_img = ImageTk.PhotoImage(add_revenues_img)
add_revenues_btn = Button(downFrame, command=insert_revenues_2, image=add_revenues_img, text=" Add".upper(), width=80, compound=LEFT, anchor=NW, font=('Ivy 7 bold'), bg=co1, fg=co0, overrelief=RIDGE)
add_revenues_btn.place(x=670, y=111)

# New category operations ----------------------------------------------------------------------------------------------------
label_info = Label(downFrame, text='Category', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
label_info.place(x=600, y=160)

entry_category = Entry(downFrame, width=14, justify='left', relief='solid')
entry_category.place(x=670, y=160)

# Add Btn
add_category_img = Image.open('./img/addBtn.png')
add_category_img = add_category_img.resize((17,17))
add_category_img = ImageTk.PhotoImage(add_category_img)
add_category_btn = Button(downFrame, command=insert_category_2, image=add_category_img, text=" Add".upper(), width=80, compound=LEFT, anchor=NW, font=('Ivy 7 bold'), bg=co1, fg=co0, overrelief=RIDGE)
add_category_btn.place(x=670, y=190)

# Functions ----------------------------------------------------------------------------------------------------
def percentage():
    label_name = Label(midFrame, text="Percentage of revenue spent", height=1, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    label_name.place(x=7, y=5)

    style = ttk.Style()
    style.theme_use('default')
    style.configure("black.Horizontal.TProgressBar", background='#daed6b')
    style.configure("TProgressBar", thickness=25)
    
    bar = Progressbar(midFrame, length=180, style='black.Horizontal.TProgressbar')
    bar.place(x=10, y=35)
    bar['value'] = percentage_values()

    value = percentage_values()
    label_percentage = Label(midFrame, text="{:,.2f}%".format(value), anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    label_percentage.place(x=200, y=35)

def graphic_bar():
    categories_list = ['Income', 'Expenses','Balance']
    values_list = values_bar()

    figure = plt.Figure(figsize=(4, 3.45), dpi=60)
    ax = figure.add_subplot(111)

    ax.bar(categories_list, values_list, color=colors, width=0.9)

    c = 0

    for i in ax.patches:
        ax.text(i.get_x()-.001, i.get_height()+.5,
                str("{:,.0f}".format(values_list[c])), fontsize=17, fontstyle='italic', verticalalignment='bottom', color='dimgrey')
        c += 1

    ax.set_xticklabels(categories_list,fontsize=16)

    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False, color='#EEEEEE')
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figure, midFrame)
    canva.get_tk_widget().place(x=10, y=70)

def summary():
    value = values_bar()

    label_line = Label(midFrame, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg='#545454')
    label_line.place(x=309, y=52)
    label_summary = Label(midFrame, text="Total monthly income   ".upper(), anchor=NW, font=('Verdana 12'), bg=co1, fg='#83a9e6')
    label_summary.place(x=309, y=35)
    label_summary = Label(midFrame, text="R$ {:,.2f}".format(value[0]), anchor=NW, font=('Arial 17'), bg=co1, fg='#545454')
    label_summary.place(x=309, y=70)
    
    label_line = Label(midFrame, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg='#545454')
    label_line.place(x=309, y=132)
    label_summary = Label(midFrame, text="Total monthly expenses".upper(), anchor=NW, font=('Verdana 12'), bg=co1, fg='#83a9e6')
    label_summary.place(x=309, y=115)
    label_summary = Label(midFrame, text="R$ {:,.2f}".format(value[1]), anchor=NW, font=('Arial 17'), bg=co1, fg='#545454')
    label_summary.place(x=309, y=150)
    
    label_line = Label(midFrame, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg='#545454')
    label_line.place(x=309, y=207)
    label_summary = Label(midFrame, text="Total cash balance      ".upper(), anchor=NW, font=('Verdana 12'), bg=co1, fg='#83a9e6')
    label_summary.place(x=309, y=190)
    label_summary = Label(midFrame, text="R$ {:,.2f}".format(value[2]), anchor=NW, font=('Arial 17'), bg=co1, fg='#545454')
    label_summary.place(x=309, y=220)

def pie_graph():
    figure = plt.Figure(figsize=(5, 3), dpi=90)
    ax = figure.add_subplot(111)

    values_list = graph_values()[1]
    categories_list = graph_values()[0]

    explode = []
    for i in categories_list:
        explode.append(0.05)

    ax.pie(values_list, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors,shadow=True, startangle=90)
    ax.legend(categories_list, loc="center right", bbox_to_anchor=(1.55, 0.50))

    category_canva = FigureCanvasTkAgg(figure, frame_gra_pie)
    category_canva.get_tk_widget().grid(row=0, column=0)

def showIncome():

    # creating a treeview with dual scrollbars
    table_head = ['#Id','Category','Date','Qty']

    itens_list = table()
    
    global tree

    tree = ttk.Treeview(incomeFrame, selectmode="extended",columns=table_head, show="headings")
    # vertical scrollbar
    vsb = ttk.Scrollbar(incomeFrame, orient="vertical", command=tree.yview)
    # horizontal scrollbar
    hsb = ttk.Scrollbar(incomeFrame, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    hd=["center","center","center", "center"]
    h=[30,100,100,100]
    n=0

    for col in table_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in itens_list:
        tree.insert('', 'end', values=item)

percentage()
graphic_bar()
summary()
pie_graph()
showIncome()

window.mainloop()