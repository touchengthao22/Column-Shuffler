import tkinter
import os
from tkinter import filedialog
from pathlib import Path
import pandas as pd
import requests


class Tk:
    """
    Main GUI class
    """

    def __init__(self):
        # set up GUI window
        self.window = tkinter.Tk()
        self.window.title('Column Formatter')
        self.window.geometry('750x500')

        self.frame = tkinter.Frame(self.window)
        self.frame.pack()

        self.path = ""

        # Main frame to store all labels so that that app will be responsive
        self.input_frame = tkinter.LabelFrame(self.frame, text='Quickly Reorganized Columns Within Minutes')
        self.input_frame.grid(row=0, column=0)

        # Create entry
        file_name_text = tkinter.Label(self.input_frame, text='1) Enter file name below: (REQUIRED)', pady=5)
        file_name_text.grid(row=0, column=0)
        self.file_name = tkinter.Entry(self.input_frame, width=30)
        self.file_name.grid(row=1, column=0)
        self.file_name.config(justify='center')

        # ---------------------List box------------------------------------ #
        self.listbox = tkinter.Listbox(self.input_frame, selectmode=tkinter.MULTIPLE)
        self.listbox.grid(row=2, column=0, pady=5)

        self.input_area = tkinter.Label(self.input_frame, text='2) Press "Upload" button below to select csv to load headers', pady=10)
        self.input_area.grid(row=3, column=0)

        # ---------------------Button------------------------------------ #
        self.button = tkinter.Button(self.input_frame, text="Load CSV File", width=15, command= self.process_headers)
        self.button.grid(row=4, column=0)

        self.shuffle_button = tkinter.Button(self.input_frame, text='Reshuffle headers', width=15, state="disabled", command=self.shuffle_header)
        self.shuffle_button.grid(row=6, column=0, pady=10)

        self.add_date_button = tkinter.Button(self.input_frame, text='Add date to file name', width=15, command=self.add_date)
        self.add_date_button.grid(row=1, column=1, pady=10)

        # ---------------------Status Message------------------------------------ #
        self.message = tkinter.Label(self.input_frame, text="", pady=10)
        self.message.grid(row=7, column=0)

    def process_headers(self):
        """
        method to allow users to select path where csv file is located
        """
        self.path = filedialog.askopenfilename()

        if not self.path:
            pass

        # Check if name entry field is empty
        elif len(self.file_name.get()) == 0:
            message = 'Missing: file name'
            self.get_status(message, 'red')

        elif self.path and self.check_csv_extension(self.path):
            self.get_status('Please wait while your data is being processed! \n'
                            'You will see a list of column header names above once completed', 'brown')

            # Disable entry field and upload button once we start processing data
            self.file_name.config(state='disabled')
            self.button.config(state='disabled')

            headers = self.get_header_list(self.path)
            self.place_header(headers)

            # Display message when we are done processing data
            self.get_status('CSV file header(s) has successfully loaded!', 'green')

        else:
            message = ('The file you have selected is not the correct file! \n '
                       'Make sure you are using a .csv file.\n'
                       'Please try again!')
            self.get_status(message, 'red')

    def get_header_list(self, path):
        """
        returns list of headers
        """
        df = pd.read_csv(path)
        df_headers = df.columns.tolist()
        return df_headers

    def place_header(self, my_list):
        """
        places header into listbox
        """

        for col in my_list:
            self.listbox.insert(tkinter.END, col)
        
        self.shuffle_button.config(state="normal")
    
    def shuffle_header(self):
        """
        shuffles header with microservice and place headers back into listbox
        """
        header_list = self.get_header_list(self.path)
        length_of_header = len(header_list)

        try:
            url = f"http://127.0.0.1:5001/shuffle?length={length_of_header}"
            response = requests.get(url)

            if response.status_code == 200:
                try:
                    self.shuffle_button.config(state="disabled")
                    shuffled_numbers = response.json().get("shuffled_numbers")
                    if shuffled_numbers is not None:
                        self.clear_listbox()
                        
                        for index, value in enumerate(shuffled_numbers):
                            shuffled_numbers[index] = header_list[shuffled_numbers[index]]

                        self.place_header(shuffled_numbers)
                        self.shuffle_button.config(state="normal")
                        self.get_status("Successfully reshuffled!", "green")
                    else:
                        print("Key 'shuffled_numbers' not found in the response.")

                except ValueError as e:
                    print(f"Error parsing JSON: {e}")
            else:
                self.get_status(f"Request failed with status code {response.status_code}", "red")
        
        except:
            self.get_status("Request failed. Make sure your microservice is running", "red")

    def add_date(self):
        """
        Takes name from file name input and adds today's today to it
        """
        file_name = self.file_name.get()
    
        try:
            url = f"http://127.0.0.1:5001/get_date?name={file_name}"
            response = requests.get(url)

            new_name_date = response.json().get("new_name")

            self.file_name.delete(0, tkinter.END)
            self.file_name.insert(0, new_name_date)
            self.get_status("Date has been successfully added to file name", "green")
        
        except:
            self.get_status("Request failed. Make sure your Microservice B is running", "red")


    def clear_listbox(self):
        """
        empties listbox
        """
        self.listbox.delete(0, tkinter.END)

    def get_status(self, message, color='black'):
        """
        Returns status message on window
        """

        self.message.config(text=message, fg=color, font='bold')

    def check_csv_extension(self, file_path):
        """
        Check file path if it is a csv file
        """
        return Path(file_path).suffix.lower() == '.csv'

    def start(self):
        """
        Start application
        """
        self.window.mainloop()


if __name__ == "__main__":
    app = Tk()
    app.start()
