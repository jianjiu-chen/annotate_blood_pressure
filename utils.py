import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
import os

import pandas as pd


def input_person():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    user_input = simpledialog.askstring(title="Input", prompt="Whose data are these? pimama or dad")
    root.destroy()  # Destroy the root window after getting the input
    return user_input


def input_today():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    user_input = simpledialog.askstring(title="Input", prompt="What's the date today?")
    root.destroy()  # Destroy the root window after getting the input
    return user_input


def open_image_and_get_input(pic_path, data_dict):
    """
    :param pic_path: should be an element of pic_new_names_fullpath (created in main)
    :param data_dict: defined in main
    :return: nothing, but write inputs to data_dict
    """
    # Open the image
    image = Image.open(pic_path)

    # Resize the image to fit the window
    window_width = 800
    window_height = 600
    image = image.resize((window_width, window_height), resample=Image.BILINEAR)

    # Create the Tkinter window
    window = tk.Tk()
    window.title("Image Viewer")

    # Create a frame to hold the image and input fields
    main_frame = tk.Frame(window)
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Create a canvas to display the image
    canvas = tk.Canvas(main_frame, width=window_width, height=window_height)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Display the image on the canvas
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

    # Create a frame for the input fields
    input_frame = tk.Frame(main_frame)
    input_frame.pack(side=tk.LEFT, padx=20)

    # Create input fields
    sys_bp_label = tk.Label(input_frame, text="Systolic BP:")
    sys_bp_label.grid(row=0, column=0)
    sys_bp_entry = tk.Entry(input_frame)
    sys_bp_entry.grid(row=0, column=1)

    # Focus on the name entry box when the window appears
    sys_bp_entry.focus_set()

    dia_bp_label = tk.Label(input_frame, text="Diastolic BP:")
    dia_bp_label.grid(row=1, column=0)
    dia_bp_entry = tk.Entry(input_frame)
    dia_bp_entry.grid(row=1, column=1)

    hr_label = tk.Label(input_frame, text="Heart rate:")
    hr_label.grid(row=2, column=0)
    hr_entry = tk.Entry(input_frame)
    hr_entry.grid(row=2, column=1)

    # Create a function to handle form submission
    def submit_form(event=None):
        get_user_input(sys_bp_entry, dia_bp_entry, hr_entry, data_dict)
        window.destroy()

    # Bind the Enter key to the submit_form function
    window.bind('<Return>', submit_form)

    # Create a submit button
    submit_button = tk.Button(input_frame, text="Submit", command=submit_form)
    submit_button.grid(row=3, column=0, columnspan=2, pady=10)

    # Start the Tkinter event loop
    window.mainloop()


def get_user_input(sys_bp_entry, dia_bp_entry, hr_entry, data_dict):
    sys_bp_val = sys_bp_entry.get()
    dia_bp_val = dia_bp_entry.get()
    hr_val = hr_entry.get()
    data_dict['sys_bp_val'] = sys_bp_val
    data_dict['dia_bp_val'] = dia_bp_val
    data_dict['hr_val'] = hr_val


def store_input(data_dict, pic_nam):
    """
    :param data_dict: this was written by open_image_and_get_input
    :param pic_nam: filename, not the full path
    :return: nothing, but store input to a csv file
    """
    df = pd.DataFrame(data_dict, index=[pic_nam])
    csv_file_name = '/Users/Chen/project/annotate_blood_pressure/data/data.csv'
    df.to_csv(csv_file_name, mode='a', header=not os.path.exists(csv_file_name))