import requests

def get_shuffled_numbers(length):
    url = f"http://127.0.0.1:5001/shuffle?length={length}"
    response = requests.get(url)
    return response.json()["shuffled_numbers"]

# Example usage
length = 10
shuffled_numbers = get_shuffled_numbers(length)
print("Shuffled Numbers:", shuffled_numbers)
