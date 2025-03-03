from flask import Flask, jsonify, request
import random

app = Flask(__name__)

@app.route('/shuffle', methods=['GET'])
def get_shuffled_array():
    try:
        length_str = request.args.get('length')
        if length_str is None:
            return jsonify({'error': 'Missing required parameter: length'}), 400
        
        length = int(length_str)
        numbers = list(range(length))
        random.shuffle(numbers)
        return jsonify({'shuffled_numbers': numbers})
    except ValueError:
        return jsonify({'error': 'Invalid input: length must be an integer.'}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5001)