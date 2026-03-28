from flask import Flask, request, jsonify
from flask_cors import CORS
from database import init_db, connect
import datetime

app = Flask(__name__)
CORS(app)

# Initialize database
init_db()

@app.route('/')
def index():
    return jsonify({
        "status": "online",
        "message": "Expense Tracker API is running",
        "endpoints": ["/api/transactions", "/api/summary"]
    })

@app.route('/api/transactions', methods=['GET'])
def get_transactions():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions ORDER BY date DESC")
    rows = cursor.fetchall()
    conn.close()
    
    transactions = []
    for row in rows:
        transactions.append({
            "id": row[0],
            "title": row[1],
            "amount": row[2],
            "type": row[3],
            "category": row[4],
            "date": row[5],
            "description": row[6]
        })
    return jsonify(transactions)

@app.route('/api/transactions', methods=['POST'])
def add_transaction():
    data = request.json
    title = data.get('title')
    amount = data.get('amount')
    type = data.get('type')
    category = data.get('category')
    date = data.get('date', datetime.date.today().isoformat())
    description = data.get('description', '')
    
    if not all([title, amount, type, category]):
        return jsonify({"error": "Missing required fields"}), 400
        
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO transactions (title, amount, type, category, date, description) VALUES (?, ?, ?, ?, ?, ?)",
        (title, amount, type, category, date, description)
    )
    conn.commit()
    conn.close()
    return jsonify({"message": "Transaction added successfully"}), 201

@app.route('/api/transactions/<int:id>', methods=['DELETE'])
def delete_transaction(id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transactions WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Transaction deleted successfully"})

@app.route('/api/summary', methods=['GET'])
def get_summary():
    conn = connect()
    cursor = conn.cursor()
    
    # Total Income
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='income'")
    total_income = cursor.fetchone()[0] or 0
    
    # Total Expense
    cursor.execute("SELECT SUM(amount) FROM transactions WHERE type='expense'")
    total_expense = cursor.fetchone()[0] or 0
    
    # Category Distribution (for chart)
    cursor.execute("SELECT category, SUM(amount) FROM transactions WHERE type='expense' GROUP BY category")
    categories = [{"category": row[0], "amount": row[1]} for row in cursor.fetchall()]
    
    conn.close()
    
    return jsonify({
        "totalIncome": total_income,
        "totalExpense": total_expense,
        "balance": total_income - total_expense,
        "categories": categories
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
