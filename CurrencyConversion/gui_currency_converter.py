import tkinter as tk
from tkinter import ttk
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
API_KEY = os.getenv('API_KEY')
BASE_URL = 'https://api.exchangerate-api.com/v4/latest/'

# Currency dictionary
d = {
    "Country": "Currency Code",
    "Indian Rupee": "INR",
    "US Dollars": "USD",
    "British Pounds": "GBP",
    "Euros": "EUR",
    "Canadian Dollar": "CAD",
    "Chinese Yuan": "CNY",
    "Russian Ruble": "RUB"
}

def fetch_conversion_rate(base_currency, target_currency):
    try:
        response = requests.get(BASE_URL + base_currency)
        data = response.json()
        return data['rates'][target_currency]
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def convert_currency():
    base_currency = d[c1_var.get()]
    target_currency = d[c2_var.get()]

    rate = fetch_conversion_rate(base_currency, target_currency)
    if rate is None:
        result_label.config(text="Error fetching conversion rate.")
        return

    amount = float(amount_var.get())
    result = amount * rate
    result_label.config(text=f"{amount} {base_currency} = {result:.2f} {target_currency}")

# Create main window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("500x600")  # Increased height

# Create frames
frame1 = tk.Frame(root, padx=10, pady=10, bg='lightblue')
frame1.pack(padx=20, pady=10, fill='x')

frame2 = tk.Frame(root, padx=10, pady=10, bg='lightgreen')
frame2.pack(padx=20, pady=10, fill='x')

frame3 = tk.Frame(root, padx=10, pady=10, bg='lightyellow')
frame3.pack(padx=20, pady=10, fill='x')

# Create currency selection dropdowns
c1_var = tk.StringVar(value="Indian Rupee")
c2_var = tk.StringVar(value="US Dollars")

c1_label = tk.Label(frame1, text="Select currency to convert from:", bg='lightblue', font=('Arial', 16))
c1_label.pack()

c1_menu = ttk.Combobox(frame1, textvariable=c1_var, values=[k for k in d.keys() if k != "Country"], font=('Arial', 14))
c1_menu.pack()

c2_label = tk.Label(frame2, text="Select currency to convert to:", bg='lightgreen', font=('Arial', 16))
c2_label.pack()

c2_menu = ttk.Combobox(frame2, textvariable=c2_var, values=[k for k in d.keys() if k != "Country"], font=('Arial', 14))
c2_menu.pack()

# Amount input
amount_var = tk.StringVar(value="1")
amount_label = tk.Label(frame3, text="Enter amount to be converted:", bg='lightyellow', font=('Arial', 16))
amount_label.pack()

amount_entry = tk.Entry(frame3, textvariable=amount_var, font=('Arial', 16), width=15)
amount_entry.pack(pady=10)

# Convert button
convert_button = tk.Button(frame3, text="Convert", command=convert_currency, font=('Arial', 16))
convert_button.pack(pady=20)

# Result label
result_label = tk.Label(frame3, text="", bg='lightyellow', font=('Arial', 18, 'bold'))
result_label.pack()

# Run the application
root.mainloop()
