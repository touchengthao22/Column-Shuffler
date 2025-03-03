# CS361-assignment8

## How to run

1. Clone repository and navigate to project folder
2. Install dependencies by running `pip install flask`
3. Run microservice by running "python3 microservice.py"

## Communication Contract

### Requesting Data

To request data from the microservice, make an HTTP GET request to:
http://127.0.0.1:5001/shuffle?length={length}

Example call using Python 'requests':

url = f"http://127.0.0.1:5001/shuffle?length={length}"

response = requests.get(url)

### Receiving Data
The microservice responds with a list of shuffled integers in JSON format

Example call:
``` 
    return response.json()["shuffled_numbers"]

shuffled_numbers = get_shuffled_numbers(10)
print("Shuffled Numbers:", shuffled_numbers)
```

Response:

<img width="643" alt="Screenshot 2025-02-24 at 5 43 58 PM" src="https://github.com/user-attachments/assets/66da0af6-2877-4a0b-a81c-f0aeb1970dff" />

### UML:

<img width="758" alt="Screenshot 2025-02-24 at 10 06 20 PM" src="https://github.com/user-attachments/assets/96692579-ed3d-45ef-8398-071df6d694ee" />
