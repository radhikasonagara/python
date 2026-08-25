import tkinter as tk 
from tkinter import ttk,filedialog,messagebox

root = tk.Tk()
root.title("Employess Registration Form")
root.geometry("600x650")


tk.Label(
    text="First Name:",
    font = ("Arial",12)
).grid(row=0,column=0,padx=10,pady=10,sticky="w")

first_name_entry=tk.Entry(
    width=35,
    font=("Arial",12)
)
first_name_entry.grid(row=0,column=1,padx=10,pady=10)

tk.Label(
    text="Last Name:",
    font = ("Arial",12)
).grid(row=1,column=0,padx=10,pady=10,sticky="w")

last_name_entry=tk.Entry(
    width=35,
    font=("Arial",12)
)
last_name_entry.grid(row=1,column=1,padx=10,pady=10)


tk.Label(
    text="Email:",
    font = ("Arial",12)
).grid(row=2,column=0,padx=10,pady=10,sticky="w")

email_entry=tk.Entry(
    width=35,
    font=("Arial",12)
)
email_entry.grid(row=2,column=1,padx=10,pady=10)

tk.Label(
    text="Phone Number:",
    font = ("Arial",12)
).grid(row=3,column=0,padx=10,pady=10,sticky="w")

phone_entry=tk.Entry(
    width=35,
    font=("Arial",12)
)
phone_entry.grid(row=3,column=1,padx=10,pady=10)

tk.Label(
    text="Department:",
    font = ("Arial",12)
).grid(row=4,column=0,padx=10,pady=10,sticky="w")

department=ttk.Combobox(
    values=["HR","IT","Finance","Marketing"],
    width=35,
    font=("Arial",12)
)
department.grid(row=4,column=1,padx=10,pady=10)

tk.Label(
    text="Designation:",
    font = ("Arial",12)
).grid(row=5,column=0,padx=10,pady=10,sticky="w")

designation=ttk.Combobox(
    values=["Manager","Developer","Accountant"],
    width=35,
    font=("Arial",12)
)
designation.grid(row=5,column=1,padx=10,pady=10)

tk.Label(
    text="Gender:",
    font = ("Arial",12)
).grid(row=6,column=0,padx=10,pady=10,sticky="w")

gender= tk.StringVar()

tk.Radiobutton(
    text="Male",
    variable=gender,
    value="Male"
).grid(row=6,column=1,sticky="w")
tk.Radiobutton(
    text="FeMale",
    variable=gender,
    value="FeMale"
).grid(row=6,column=1,sticky="w",padx=80)

tk.Label(
    text="Date Of Birth:",
    font=("Arial",12)
).grid(row=7,column=0,padx=10,pady=10,sticky="w")
dob_entry=tk.Entry(
    width=35,
    font=("Arial",12)
)
dob_entry.grid(row=7,column=1,padx=10,pady=10,sticky="w")

tk.Label(
    text="Address:",
    font=("Arial",12)
).grid(row=8,column=0,padx=10,pady=10,sticky="w")
add_entry=tk.Entry(
    width=35,
    font=("Arial",12)
    
)
add_entry.grid(row=8,column=1,padx=10,pady=10,sticky="w")


tk.Label(
    text="Password:",
    font=("Arial",12)
).grid(row=9,column=0,padx=10,pady=10,sticky="w")
password_entry=tk.Entry(
    width=35,
    font=("Arial",12),
    show="*"
)
password_entry.grid(row=9,column=1,padx=10,pady=10,sticky="w")

tk.Label(
    text="Confrim Password:",
    font=("Arial",12)
).grid(row=10,column=0,padx=10,pady=10,sticky="w")
confirm_password_entry=tk.Entry(
    width=35,
    font=("Arial",12),
    show="*"
)
confirm_password_entry.grid(row=10,column=1,padx=10,pady=10,sticky="w")

def submit():
    messagebox.showinfo(
        "Success",
        "Employee Registration Successfull!!"
    )

submit_button = tk.Button(
    text="Submit",
    font=("Arial",12,"bold"),
    width=15,
    command=submit
)
submit_button.grid(row=11,column=1,padx=10,pady=20)

root.mainloop()

