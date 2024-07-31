import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

# Initialize the global variables
tdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
tdays1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
n = 0
birth_yr = 0

# Define the leap year function
def leap(year, tdays, n, birth_yr, month):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        del tdays[1]
        tdays.insert(1, 29)
        n += tdays[month - 1]
        birth_yr += 366
        return True
    else:
        n += tdays[month - 1]
        birth_yr += 365
        return False

# Define the check function
def check(year, month, day):
    if len(str(year)) == 4 and len(str(month)) <= 2 and len(str(day)) <= 2:
        if (month <= 12 and month > 0) and (day <= 31 and day > 0):
            if leap(year, tdays, n, birth_yr, month):
                if day <= tdays[month - 1]:
                    return False
                else:
                    return f"Month {month} of year {year} had {tdays[month - 1]} days"
            else:
                if day <= tdays[month - 1]:
                    return False
                else:
                    return f"Month {month} of year {year} had {tdays[month - 1]} days"
        else:
            return "Date must be less than or equal to 31 and greater than 0. Month must be less than or equal to 12 and greater than 0."
    else:
        return "Please enter date in correct format."

# Define the calculate function
def calculate():
    try:
        birth_date = date_of_birth.get_date()
        present_date = present_date_entry.get_date()

        global tdays, birth_yr
        n = 0
        birth_yr = 0
        tdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        year, month, day = birth_date.year, birth_date.month, birth_date.day
        year1, month1, day1 = present_date.year, present_date.month, present_date.day

        # Validate birth date
        if check(year, month, day) == False:
            day_month = tdays[month - 1] - day

            leap(year, tdays, n, birth_yr, month)
            days_birth_yr=0
            for i in range(month,12):
                days_birth_yr += tdays[i]

            totaldaysLeft_birth = days_birth_yr + day_month

            days_yr=0
            for i in range(0,month1-1):
                days_yr += tdays1[i]

            leap(year1, tdays1, n, birth_yr, month1)
            totaldaysLived = days_yr + day1

            total = 0
            y_c = 1

            if year < year1:
                while year + 1 != year1:
                    y_c += 1
                    if leap(year + 1, tdays, n, birth_yr, month):
                        total += 366
                    else:
                        total += 365
                    year += 1
                result = f"TOTAL DAYS SURVIVED(year): {total + totaldaysLeft_birth + totaldaysLived + 1}\nYears lived: {y_c}\n"
            elif year > year1:
                result = "Date of birth must be earlier than present date"
            elif year == year1:
                totaldaysLived = 0
                if month == month1:
                    result = f"TOTAL DAYS SURVIVED!!@@(end included): {day1 - day + 1}\nYears lived: {year1 - year}\n"
                elif month > month1:
                    result = "Date of birth must be earlier than present date"
                else:
                    totaldaysLived = sum(tdays[month:month1 - 1])
                    result = f"TOTAL DAYS SURVIVED(same)(end included): {totaldaysLived + (tdays[month - 1] - (day - 1)) + day1}"
        else:
            result = check(year, month, day)
        
        result_label.config(text=result)
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Date Calculator")
root.geometry("600x400")
root.configure(bg="#f0f0f0")

# Define fonts and styles
title_font = ('Arial', 18, 'bold')
label_font = ('Arial', 12)
button_font = ('Arial', 12, 'bold')

# Create and place widgets
title_label = tk.Label(root, text="Date Calculator", font=title_font, bg="#f0f0f0")
title_label.pack(pady=10)

frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(pady=10)

tk.Label(frame, text="Date of Birth:", font=label_font, bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=5)
date_of_birth = DateEntry(frame, width=12, background='darkblue', foreground='white', borderwidth=2)
date_of_birth.grid(row=0, column=1, padx=10, pady=5)

tk.Label(frame, text="Present Date:", font=label_font, bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=5)
present_date_entry = DateEntry(frame, width=12, background='darkblue', foreground='white', borderwidth=2)
present_date_entry.grid(row=1, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate", font=button_font, command=calculate, bg="green", fg="white")
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="", font=label_font, bg="#f0f0f0", wraplength=500)
result_label.pack(pady=10)

root.mainloop()
