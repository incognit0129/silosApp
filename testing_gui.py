import tkinter as tk
import random

import math
import customtkinter as ctk


import json










#functions
#change color if lower level

# Create the window
window = ctk.CTk()
window.title("Progress Bars")
window._set_appearance_mode('dark')
window.geometry("1000x1000")

#Create the progress bars
progress_bar1 = tk.Canvas(window, width=100, height=300, bg="white")
progress_bar1.grid(row=1, column=1, padx=100, pady=50)

progress_bar2 = tk.Canvas(window, width=100, height=300, bg="white")
progress_bar2.grid(row=1, column=2, padx=100, pady=50)

progress_bar3 = tk.Canvas(window, width=100, height=300, bg="white")
progress_bar3.grid(row=1, column=3, padx=100, pady=50)

# Create the labels
label1 = tk.Label(window, text="Silo 1", font=('raleway',15, 'bold'), relief='raised')
label1.grid(row=0, column=1)

label2 = tk.Label(window, text="Silo 2", font=('raleway', 15, 'bold'), relief='raised')
label2.grid(row=0, column=2)

label3 = tk.Label(window, text="Silo 3", font=('raleway', 15, 'bold'), relief='raised')
label3.grid(row=0, column=3)




#value  mA labels

silo_1_current = tk.Label(window, text="ma", font=('raleway',15, 'bold'), relief='raised')
silo_1_current.grid(row=2, column=1, padx=25, pady=0)

silo_2_current = tk.Label(window, text="ma", font=('raleway', 15, 'bold'), relief='raised')
silo_2_current.grid(row=2, column=2, padx=25, pady=0)


silo_3_current = tk.Label(window, text="ma", font=('raleway', 15, 'bold'), relief='raised')
silo_3_current.grid(row=2, column=3, padx=25, pady=0)


#value lbs labels

silo_1_lbs = tk.Label(window, text="lbs", font=('raleway',15, 'bold'), relief='raised')
silo_1_lbs.grid(row=4, column=1, padx=25, pady=0)

silo_2_lbs = tk.Label(window, text="lbs", font=('raleway',15, 'bold'), relief='raised')
silo_2_lbs.grid(row=4, column=2, padx=25, pady=0)

silo_3_lbs = tk.Label(window, text="lbs", font=('raleway',15, 'bold'), relief='raised')
silo_3_lbs.grid(row=4, column=3, padx=25, pady=0)

#ft labels
silo_1_ft = tk.Label(window, text="ft", font=('raleway',15, 'bold'), relief='raised')
silo_1_ft.grid(row=5, column=1, padx=25, pady=0)

silo_2_ft = tk.Label(window, text="ft", font=('raleway',15, 'bold'), relief='raised')
silo_2_ft.grid(row=5, column=2, padx=25, pady=0)


silo_3_ft = tk.Label(window, text="ft", font=('raleway',15, 'bold'), relief='raised')
silo_3_ft.grid(row=5, column=3, padx=25, pady=0)


#Category 
silo_calc_values = tk.Label(window, text="Linear Values", font=('raleway',20, 'bold'), relief='raised')
silo_calc_values.grid(row=3, column=0, padx=25, pady=15)

silo_Mass = tk.Label(window, text="Mass", font=('raleway',15, 'bold'), relief='raised')
silo_Mass.grid(row=4, column=0, padx=25, pady=15)


silo_height = tk.Label(window, text="Height", font=('raleway',15, 'bold'), relief='raised')
silo_height.grid(row=5, column=0, padx=25, pady=15)


#functions
#change color if lower level
def change_color_bar3(value3):
        if value3 <=33:
            progress_bar3.create_rectangle(0, 300-value3*3, 100, 300, fill="red")
        elif value3 <=66:
            progress_bar3.create_rectangle(0, 300-value3*3, 100, 300, fill="yellow")

def change_color_bar2(value2):
        if value2 <=33:
            progress_bar2.create_rectangle(0, 300-value2*3, 100, 300, fill="red")
        elif value2 <=66:
            progress_bar2.create_rectangle(0, 300-value2*3, 100, 300, fill="yellow")
            
def change_color_bar1(value1):
        if value1 <=33:
            progress_bar1.create_rectangle(0, 300-value1*3, 100, 300, fill="red")
        elif value1 <=66:
            progress_bar1.create_rectangle(0, 300-value1*3, 100, 300, fill="yellow")
            
# def change_color_bar1(value1):
#    progress_bar2.create_rectangle(0, 300-value1*3, 100, 300, fill="red")



def silo_values(silo1, silo2, silo3):
    
    values = {
        "Silo1": str(silo1),
        "Silo2": str(silo2),
        "Silo3": str(silo3)
    }
    return values

def update_json_file(values):
    with open('data.json', 'w') as f:
        json.dump(values, f)



# Update the progress bars with a random value every second
def update_progress_bars():
    # Generate random values
    value1 = random.randint(0,100)
    value2 = random.randint(0,100)
    value3 = random.randint(0,100)
    
    values = silo_values(value1, value2, value3)
    
    update_json_file(values)
    
    
    
    #Update progress bars
    progress_bar1.delete("all")
    progress_bar1.create_rectangle(0, 300-value1*3, 100, 300, fill="green")
    silo_1_current.config(text=f"{value1} %")
    
    progress_bar2.delete("all")
    progress_bar2.create_rectangle(0, 300-value2*3, 100, 300, fill="green")
    silo_2_current.config(text=f"{value2} %")
    
    progress_bar3.delete("all")
    progress_bar3.create_rectangle(0, 300-value3*3, 100, 300, fill="green")
    silo_3_current.config(text=f"{value3} %")
    
    
    #update labels silo 1 
    silo_1_lbs.config(text =f"{round(((12-4)/16)*84000, 2)} lbs")
    silo_1_ft.config(text =f"{round(((12-4)/16)*24, 2)} ft")
    
        #update labels silo 2 
    silo_2_lbs.config(text =f"{round(((12-4)/16)*91747, 2)} lbs")
    silo_2_ft.config(text =f"{round(((12-4)/16)*24, 2)} ft")
    
    
    #update labels silo 3 
    silo_3_lbs.config(text =f"{round(((12-4)/16)*125200, 2)} lbs")
    silo_3_ft.config(text =f"{round(((12-4)/16)*24, 2)} ft")
    
    change_color_bar3(value3)
    change_color_bar2(value2)
    change_color_bar1(value1)
        
    # Schedule the next update
    window.after(5000, update_progress_bars)

# Start the update loop
update_progress_bars()

# Start the event loop
window.mainloop()
