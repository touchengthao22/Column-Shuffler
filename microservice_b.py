from flask import Flask, jsonify, request
import random
from datetime import datetime

app = Flask(__name__)

@app.route('/get_date', methods=['GET'])
def get_date():
    """
    returns today's date
    """

    try:
        name = request.args.get('name')
        name_date = f'{name}_{datetime.now().strftime("%m-%d-%Y")}'
        return jsonify({'new_name': name_date})
        
    except ValueError:
        return 'error: Invalid input', 400

if __name__ == '__main__':
    app.run(debug=True, port=5002)