import tkinter as tk
from tkinter import simpledialog
from tkinter import Canvas
import datetime
import pytz
import os

import pandas as pd


#######################
# get person and date
#######################
def input_person():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    user_input = simpledialog.askstring(title="Input", prompt="Whose data are these? pimama or dad")
    root.destroy()  # Destroy the root window after getting the input
    return user_input


person = input_person()
assert person in ('pimama', 'dad'), 'The input should be either "pimama" or "dad".'

today = datetime.datetime.now(pytz.timezone('Asia/Hong_Kong')).date().strftime('%Y%m%d')

#######################
# rename all jpg files
#######################
download_dir = '/Users/Chen/Downloads'
pic_old_names = [i for i in os.listdir(download_dir) if '.jpg' in i]

for i, pic_i in enumerate(pic_old_names):
    old_filename = os.path.join(download_dir, pic_i)
    new_filename = os.path.join(download_dir, f"{person}_{today}_{i+1}.jpg")
    os.rename(old_filename, new_filename)

pic_new_names = [i for i in os.listdir(download_dir) if '.jpg' in i]

#######################
# ask user to input BR readings
#######################
window = tk.Tk()
window.title("Please enter the readings.")

canvas = Canvas(window, width=400, height=400)
canvas.pack()

def input_bp(filename_i):
    """
    Do 3 things: 1) open a picture, 2) ask user to input data, 3) save data to a csv file
    :param filename_i: should one element in pic_new_names (a list)
    :return: Nothing
    """
    # Open the JPG file based on the user ID
    image_path = f"path/to/your/image_{filename_i}.jpg"
    if os.path.exists(image_path):
        photo = tk.PhotoImage(file=image_path)
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    else:
        print(f"Image file for user {filename_i} not found.")

    sys_bp_val = sys_bp_entry.get()
    dia_bp_val = dia_bp_entry.get()
    hr_val = hr_entry.get()
    assert isinstance(sys_bp_val, int) and sys_bp_val > 0, "Systolic BP should be positive integer!"
    assert isinstance(dia_bp_val, int) and dia_bp_val > 0, "Diastolic BP should be positive integer!"
    assert isinstance(hr_val, int) and hr_val > 0, "Heart rate should be positive integer!"
    df = pd.DataFrame({'sys_bp_val': sys_bp_val,
                       'dia_bp_val': dia_bp_val,
                       'hr_val': hr_val}, index=filename_i)
    window.destroy()


# Create input fields and a button
sys_bp_label = tk.Label(window, text="Systolic BP:")
sys_bp_entry = tk.Entry(window)
dia_bp_label = tk.Label(window, text="Diastolic BP:")
dia_bp_entry = tk.Entry(window)
hr_label = tk.Label(window, text="Heart rate:")
hr_entry = tk.Entry(window)
submit_button = tk.Button(window, text="Submit", command=lambda input_bp)

# Arrange the widgets in the window
sys_bp_label.grid(row=0, column=0)
sys_bp_entry.grid(row=0, column=1)
dia_bp_label.grid(row=1, column=0)
dia_bp_entry.grid(row=1, column=1)
hr_label.grid(row=2, column=0)
hr_entry.grid(row=2, column=1)
submit_button.grid(row=3, column=0, columnspan=2)

canvas = Canvas(window, width=400, height=400)
canvas.pack()
