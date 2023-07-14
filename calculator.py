import tkinter as tk
import math

# Create GUI
root = tk.Tk()
root.title("Finance Calculator")
root.geometry('700x500')
root.config(bg="#1e7094")

# Create labels and entries for investment calculation
fin_label=tk.Label(root, text=" FINANCIAL CALCULATOR ",bg="black", fg='white',  font=("Arial Black", 18, "bold"))
fin_label.grid(row=0, columnspan=5, pady=20)
inv_label = tk.Label(root, text="Investment Calculator",bg="#1e7094",  font=("Arial Black", 16, "bold"))
inv_label.grid(row=1, column=0, columnspan=2, padx=10, pady=20)

inv_amount_label = tk.Label(root,bg="#1e7094", text="Principle Amount:", font=("Arial", 12))
inv_amount_label.grid(row=2, column=0, padx=10, pady=5, sticky="W")
inv_amount_entry = tk.Entry(root, bg='#333',fg='white', font=("Arial", 12))
inv_amount_entry.grid(row=2,  column=1, padx=10, pady=5)

inv_rate_label = tk.Label(root,bg="#1e7094", text="Interest rate (%):", font=("Arial", 12))
inv_rate_label.grid(row=3, column=0, padx=10, pady=5, sticky="W")
inv_rate_entry = tk.Entry(root,bg='#333',fg='white', font=("Arial", 12))
inv_rate_entry.grid(row=3, column=1, padx=10, pady=5)

inv_time_label = tk.Label(root, bg="#1e7094", text="Years invested:", font=("Arial", 12))
inv_time_label.grid(row=4, column=0, padx=10, pady=5, sticky="W")
inv_time_entry = tk.Entry(root,bg='#333',fg='white', font=("Arial", 12))
inv_time_entry.grid(row=4, column=1, padx=10, pady=5)

inv_interest_label = tk.Label(root,bg="#1e7094", text="Interest type:", font=("Arial", 12))
inv_interest_label.grid(row=5, column=0, padx=10, pady=5, sticky="W")
inv_interest_var = tk.StringVar(value="Simple")
inv_interest_simple = tk.Radiobutton(root,bg="#1e7094", text="Simple", font=("Arial", 12), variable=inv_interest_var, value="Simple")
inv_interest_simple.grid(row=5, column=1, padx=10, pady=5, sticky="W")
inv_interest_compound = tk.Radiobutton(root,bg="#1e7094", text="Compound", font=("Arial", 12), variable=inv_interest_var, value="Compound")
inv_interest_compound.grid(row=5, column=1, padx=10, pady=5, sticky="E")

inv_answer_label = tk.Label(root,bg="#1e7094", text="", font=("Arial", 12, "bold"), fg="#aff44e")
inv_answer_label.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Create labels and entries for bond calculation
bond_label = tk.Label(root, text="Bond Calculator",bg="#1e7094",fg='white',  font=("Arial Black", 16, "bold"))
bond_label.grid(row=1, column=3,  columnspan=2, padx=10, pady=20)

bond_value_label = tk.Label(root,bg="#1e7094",fg='white', text="Present Value:", font=("Arial", 12))
bond_value_label.grid(row=2, column=3, padx=10, pady=5, sticky="W")
bond_value_entry = tk.Entry(root, font=("Arial", 12))
bond_value_entry.grid(row=2, column=4, padx=10, pady=5)

bond_rate_label = tk.Label(root,bg="#1e7094",fg='white', text="Interest rate (%):", font=("Arial", 12))
bond_rate_label.grid(row=3, column=3, padx=10, pady=5, sticky="W")
bond_rate_entry = tk.Entry(root, font=("Arial", 12))
bond_rate_entry.grid(row=3, column=4, padx=10, pady=5)

bond_time_label = tk.Label(root,bg="#1e7094",fg='white', text="Months to Pay:",font=("Arial", 12))
bond_time_label.grid(row=4, column=3, padx=10, pady=5, sticky="W")
bond_time_entry = tk.Entry(root, font=("Arial", 12))
bond_time_entry.grid(row=4, column=4, padx=10, pady=5)

bond_answer_label = tk.Label(root,bg="#1e7094", text="", font=("Arial", 12, "bold"), fg="#aff44e")
bond_answer_label.grid(row=6, column=3, columnspan=2, padx=10, pady=10)

# Create function for investment calculation
def calculate_investment():
    inv_amount = float(inv_amount_entry.get())
    inv_rate = float(inv_rate_entry.get())
    inv_time = int(inv_time_entry.get())
    interest_type = inv_interest_var.get()

    if interest_type == "Simple":
        inv_answer = inv_amount * (1 + (inv_rate / 100) * inv_time)
    elif interest_type == "Compound":
        inv_answer = inv_amount * math.pow((1 + inv_rate / 100), inv_time)

    inv_answer_label.config(text=f"Your investment will be worth R{inv_answer:.2f}.")

# Create function for bond calculation
def calculate_bond():
    present_value = float(bond_value_entry.get())
    interest_rate = float(bond_rate_entry.get())
    months= int(bond_time_entry.get())

    monthly_interest_rate = interest_rate / 12 / 100
    months = (monthly_interest_rate * present_value) / (1 - math.pow((1 + monthly_interest_rate), -months))

    bond_answer_label.config(text=f"Your monthly payment will be R{months:.2f}.")

# Create buttons to calculate investment and bond
inv_button = tk.Button(root,bg='#333',fg='white', text="Calculate Investment", font=("Arial", 12), command=calculate_investment)
inv_button.grid(row=7, column=0,columnspan=2, padx=30, pady=10)

bond_button = tk.Button(root, text="Calculate Bond", font=("Arial", 12), command=calculate_bond)
bond_button.grid(row=7, column=3, columnspan=2, padx=10, pady=10)

root.mainloop()
