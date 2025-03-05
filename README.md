Column Formatter GUI
This project is a Tkinter-based graphical user interface (GUI) application for quickly reshuffling columns in CSV files. It allows users to:

Load a CSV file and view the headers.
Shuffle the headers using a microservice.
Add the current date to the file name.
Export the modified CSV with reshuffled headers.
Requirements
Python 3.x
Tkinter
Requests
Pandas
In addition, the application depends on three microservices for functionality. You must ensure that all the microservices are running before starting the main application. Each microservice handles a specific task:

Microservice A: Responsible for reshuffling the column headers.
Microservice B: Responsible for adding the current date to the file name.
Microservice C: Responsible for exporting the modified CSV file.
Microservice D: Responsible for extracting the headers from the CSV file.
Ensure that these microservices are up and running on the correct endpoints (usually http://127.0.0.1:500x, where x is the microservice number).

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/column-formatter.git
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Make sure to start all the necessary microservices before launching the GUI.

Usage
Run the main application script:

bash
Copy
Edit
python app.py
The GUI window will appear with the following features:

File Name Entry: Enter the name of the CSV file.
Load CSV File: Press the button to load the CSV and display the headers.
Reshuffle Headers: Press to shuffle the headers using Microservice A.
Add Date to File Name: Add the current date to the file name.
Export CSV: Save the CSV file with reshuffled headers.
Start Over: Reset the application to start with a new file.
Microservices
Each microservice serves a specific role in processing the CSV files:

Microservice A: Responsible for reshuffling the headers of the CSV file.
Microservice B: Adds the current date to the file name.
Microservice C: Exports the newly reshuffled CSV file.
Microservice D: Extracts the headers from the CSV file.
Make sure the microservices are running at the following endpoints:

Microservice A: http://127.0.0.1:5001/shuffle
Microservice B: http://127.0.0.1:5002/get_date
Microservice C: http://127.0.0.1:5003/export_csv
Microservice D: http://127.0.0.1:5004/extract_headers
Troubleshooting
If you encounter an error indicating that a request failed, ensure that all microservices are running before proceeding with the application.
Check the status messages for guidance on any issues that may arise during the processing steps.