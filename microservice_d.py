from flask import Flask, jsonify, request, send_file
import pandas as pd
import io

app = Flask(__name__)

@app.route('/extract_headers', methods=['GET'])
def extract_headers():
    """
    Receives path of csv file and extracts headers
    """
    try:
        csv_path = request.args.get('path')

        df = pd.read_csv(csv_path)

        headers = df.columns.to_list()

        return jsonify({'headers': headers})
        
    except ValueError:
        return 'error: Invalid input', 400

if __name__ == '__main__':
    app.run(debug=True, port=5004)