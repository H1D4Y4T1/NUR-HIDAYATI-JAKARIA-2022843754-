import tkinter as tk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

def insert_data():
    cus_first_name = first_name_entry.get()
    cus_last_name = last_name_entry.get()
    cus_title = title_combobox.get()
    cus_gender = gender_combobox.get()
    cus_birth_day = dayField.get()
    cus_birth_month = monthField.get()
    cus_birth_year = yearField.get()
    cus_age = age_year_entry.get()

    # Connect to your MySQL database
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="stationery membership registration"
    )

    # Create a cursor object to execute SQL queries
    mycursor = mydb.cursor()

    # SQL query to insert data into the table
    insert_query = "INSERT INTO customer (Cus_First_Name, Cus_Last_Name, Cus_Title, Cus_Gender, Cus_Birth_Day, Cus_Birth_Month, Cus_Birth_Year, Cus_Age) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"

    # Execute the query with the data
    mycursor.execute(insert_query, (cus_first_name, cus_last_name, cus_title, cus_gender, cus_birth_day, cus_birth_month, cus_birth_year, cus_age))

    # Commit the changes to the database
    mydb.commit()

    mycursor.close()
    mydb.close()

    messagebox.showinfo("Success", "Data inserted successfully!")

# function for checking error
def checkError() :

	# if any of the entry field is empty
	# then show an error message and clear 
	# all the entries
	if (dayField.get() == "" or monthField.get() == ""
		or yearField.get() == "") :

		# show the error message
		messagebox.showerror("Input Error")
		
		return -1


# function to calculate Age 
def calculate_age() :

	# check for error
	value = checkError()

	# if error is occur then return
	if value == -1 :
		return
	
	else :
		
		# take a value from the respective entry boxes get method returns current text as string
		birth_day = int(dayField.get())
		birth_month = int(monthField.get())
		birth_year = int(yearField.get())

		given_day = int(current_day.get())
		given_month = int(current_month.get())
		given_year = int(current_year.get())

		# if birth date is greater then given birth_month then do not count this month and add 30 to the date so as to subtract the date and get the remaining days 
		month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		
		if (birth_day > given_day):
			given_month = given_month - 1
			given_day = given_day + month[birth_month-1] 
					
					
		# if birth month exceeds given month, then do not count this year and add 12 to the month so that we can subtract and find out the difference 
		if (birth_month > given_month):
			given_year = given_year - 1
			given_month = given_month + 12
					
		# calculate day, month, year 
		calculated_day = given_day - birth_day; 
		calculated_month = given_month - birth_month; 
		calculated_year = given_year - birth_year;

		# calculated day, month, year write back to the respective entry boxes

		# insert method inserting the value in the text entry box.
	
		age_year_entry.insert(10, str(calculated_year))


		# if birth date is greater then given birth_month then donot count this month and add 30 to the date so as to subtract the date and get the remaining days 
		month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		
		if (birth_day > given_day):
			given_month = given_month - 1
			given_day = given_day + month[birth_month-1] 
					
					
		# if birth month exceeds given month, then do not count this year and add 12 to the month so that we can subtract and find out the difference 
		if (birth_month > given_month):
			given_year = given_year - 1
			given_month = given_month + 12
					
		# calculate day, month, year 
		calculated_day = given_day - birth_day; 
		calculated_month = given_month - birth_month; 
		calculated_year = given_year - birth_year;

		# calculated day, month, year write back to the respective entry boxes

		# insert method inserting the value in the text entry box.
		
		age_year_entry.insert(10, str(calculated_year))

root = tk.Tk()
root.title("Stationery Membership Registration")
root.geometry("800x600")

# Customer Details
customer_frame = tk.LabelFrame(root, text= "Customer Details", font= ('Times New Roman',16, 'bold'))
customer_frame.grid(row=0, column=0, padx=20, pady=20)

first_name_label = tk.Label(customer_frame, text="First Name", font=('Times New Roman',14))
first_name_label.grid(row=0, column=0)
first_name_entry = tk.Entry(customer_frame, font=('Times New Roman',14))
first_name_entry.grid(row=1, column=0)

last_name_label = tk.Label(customer_frame, text="Last Name", font=('Times New Roman',14))
last_name_label.grid(row=0, column=1)
last_name_entry = tk.Entry(customer_frame, font=('Times New Roman',14))
last_name_entry.grid(row=1, column=1)

title_label = tk.Label(customer_frame, text="Title", font=('Times New Roman',14))
title_label.grid(row=2, column=0)
title_combobox = ttk.Combobox(customer_frame, values=["Mr.", "Ms.", "Mrs."], font=('Times New Roman',14))
title_combobox.grid(row=3, column=0)

gender_label = tk.Label(customer_frame, text="Gender", font=('Times New Roman',14))
gender_label.grid(row=2, column=1)
gender_combobox = ttk.Combobox(customer_frame, values=["Female", "Male"], font=('Times New Roman',14))
gender_combobox.grid(row=3, column=1)

for widget in customer_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Date of Birth details
birth_date_frame = tk.LabelFrame(root)
birth_date_frame.grid(row=1, column=0, ipadx=20, ipady=20)

birth_date_label = tk.Label(birth_date_frame, text= "Date of Birth", font=('Times New Roman',14, 'bold'))
birth_date_label.grid(row=1, column=0)

# Date of birth
birth_date = tk.Label(birth_date_frame, text="Day", font=('Times New Roman',14, 'bold'))
birth_date.grid(row = 2, column = 0)
birth_month = tk.Label(birth_date_frame, text="Month", font=('Times New Roman',14, 'bold'))
birth_month.grid(row = 3, column = 0)
birth_year = tk.Label(birth_date_frame, text="Year", font=('Times New Roman',14, 'bold'))
birth_year.grid(row = 4, column = 0)

# Create a text entry box for filling or typing the information(dob). 
dayField = tk.Entry(birth_date_frame)
dayField.grid(row = 2, column = 1)
monthField = tk.Entry(birth_date_frame)
monthField.grid(row = 3, column = 1)
yearField = tk.Entry(birth_date_frame)
yearField.grid(row = 4, column = 1)	

# Current Year
curr_day = tk.Label(birth_date_frame, text= "Current Day", font=('Times New Roman',14, 'bold'))
curr_day.grid(row=2, column=3)
curr_month = tk.Label(birth_date_frame, text= "Current Month", font=('Times New Roman',14, 'bold'))
curr_month.grid(row=3, column=3)
curr_year = tk.Label(birth_date_frame, text= "Current Year", font=('Times New Roman',14, 'bold'))
curr_year.grid(row=4, column=3)

# Create a text entry box for filling or typing the information(current year). 
current_day = tk.Entry(birth_date_frame)
current_day.grid(row = 2, column = 4)
current_month = tk.Entry(birth_date_frame)
current_month.grid(row = 3, column = 4)
current_year = tk.Entry(birth_date_frame)
current_year.grid(row = 4, column = 4)	

# Age results
resultantAge = tk.Button(birth_date_frame, text = "Age", command = calculate_age, padx=25, pady=5)
resultantAge.grid(row=5, column=2, sticky= "news")

age_year = tk.Label(birth_date_frame, text= "Year", font=('Times New Roman',14))
age_year.grid(row=6, column=2, sticky= "news")
age_year_entry = tk.Entry(birth_date_frame)
age_year_entry.grid(row=7, column=2, sticky= "news")

for widget in birth_date_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Button
button = tk.Button(root, text= "Enter data", command= insert_data)
button.grid(row=3, column=0, sticky= "news", padx=20, pady=10)

root.mainloop()