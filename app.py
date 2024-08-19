from flask import Flask, request, jsonify
import csv
import io

app = Flask(__name__)

transactions = []

@app.route('/transactions', methods=['POST'])
def upload():
    file = request.files['file']
    if not file:
        return jsonify({"error": "No file detected"}), 400

    # Read the CSV file
    stream = io.StringIO(file.stream.read().decode("UTF8"), newline=None)
    data = csv.reader(stream)

    # Parse the CSV and store the data
    for row in data:
        if len(row) == 4:
            transactions.append({
                "date": row[0],
                "type": row[1],
                "amount": float(row[2]),
                "memo": row[3]
            })
        else:
            continue

    return jsonify({"message": "Transactions uploaded successfully"}), 201


@app.route('/report', methods=['GET'])
def generate():
    gross = 0
    expenses = 0
    for t in transactions:
        print(t)
        if t['type'].strip().lower() == "income":
            gross += t['amount']
        elif t['type'].strip().lower() == "expense":
            expenses += t['amount']
    net = gross - expenses

    report = {
        "gross-revenue": gross,
        "expenses": expenses,
        "net-revenue": net
    }

    return jsonify(report), 200

if __name__ == '__main__':
    app.run(debug=False)
