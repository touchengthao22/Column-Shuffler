# Column Formatter GUI

This project is a Tkinter-based graphical user interface (GUI) application for quickly reshuffling columns in CSV files. It allows users to:

- Refer to microservice description below
- Load a CSV file and view the headers using microservice
- Shuffle the headers using a microservice.
- Add the current date to the file name using microservice
- Export the modified CSV with reshuffled headers using microservice

## Requirements

- Python 3.x
- Tkinter
- Requests
- Pandas

In addition, the application depends on three microservices for functionality. **You must ensure that all the microservices are running before starting the main application**. Each microservice handles a specific task:

1. **Microservice A**: Responsible for reshuffling the column headers.
2. **Microservice B**: Responsible for adding the current date to the file name.
3. **Microservice C**: Responsible for exporting the modified CSV file.
4. **Microservice D**: Responsible for extracting the headers from the CSV file.

### Microservice Endpoints

Ensure that these microservices are up and running on the correct endpoints (usually `http://127.0.0.1:500x`, where `x` is the microservice number). 

- **Microservice A**: [http://127.0.0.1:5001/shuffle](http://127.0.0.1:5001/shuffle)
- **Microservice B**: [http://127.0.0.1:5002/get_date](http://127.0.0.1:5002/get_date)
- **Microservice C**: [http://127.0.0.1:5003/export_csv](http://127.0.0.1:5003/export_csv)
- **Microservice D**: [http://127.0.0.1:5004/extract_headers](http://127.0.0.1:5004/extract_headers)

