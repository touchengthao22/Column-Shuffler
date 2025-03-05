from flask import Flask, jsonify, request, send_file
import pandas as pd
import io

app = Flask(__name__)

@app.route('/export_csv', methods=['GET'])
def export_csv():
    """
    exports to csv
    """

    try:
        csv_path = request.args.get('path')
        file_name = request.args.get('file_name')
        headers = request.args.get('headers')
        
        # convert header to list
        headers = headers.strip("[]")
        headers = [header.strip().strip("'") for header in headers.split(",")]
        print(headers)

        df = pd.read_csv(csv_path)
        df = df[headers]

        json_data = df.to_json(orient="records")

        return jsonify(json_data)
        
    except ValueError:
        return 'error: Invalid input', 400

if __name__ == '__main__':
    app.run(debug=True, port=5003)