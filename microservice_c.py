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

        output = io.StringIO()
        df.to_csv(output, index=False)
        output.seek(0)

        return send_file(
            io.BytesIO(output.getvalue().encode()),
            mimetype='text/csv',
            as_attachment=True,
            download_name=file_name + '.csv'
        )
        
    except ValueError:
        return 'error: Invalid input', 400

if __name__ == '__main__':
    app.run(debug=True, port=5003)