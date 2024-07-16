# Import libraries
from flask import Flask, redirect, request, render_template, url_for

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
# implement Read before other functions to redirect the ppage with all transactions every time a new transaction is created, updated, or deleted.
@app.route("/")
def get_transactions():
    return render_template("transactions.html", transactions=transactions)

# Create operation
# GET - display the transaction form to the user
# POST - handle the creation of a new user
@app.route("/add", methods=["GET", "POST"])
def add_transaction():
    if request.method == "POST":
        # create a new transaction object
        transation = {
            'id': len(transactions)+1,
            'date': request.form['date'],
            'amount': float(request.form['amount'])
        }
        transactions.append(transaction)
        return redirect(url_for("get_transaction"))
    # if the request is GET, render the form template
    return render_template("form.html")

# Update operation
# GET - display the current transaction data
# POST - update the data sent by user
@app.route("/edit/<int:transaction_id>", methods=["GET", "POST"])
def edit_transaction(transaction_id):
    if request.method == "POST":
        date = request.form["date"]
        amount = float(request.form["amount"])
        # find the transaction with the matching ID and update its values
        for transaction in transactions:
            if transaction["id"] == transaction_id:
                transaction["date"] = date
                transaction["amount"] = amount
                break
        # redirect to the transactions list page after updating the transaction
        return redirect(url_for("get_transactions"))
    # if request is GET, find the transaction with matching ID and render the edit form
    for transaction in transactions:
        if transaction["id"] == transaction_id:
            # render the edit form and pass the transaction to be edited
            return render_template("edit.html", transaction=transaction)
    # if the transaction ID is not found, handle this case
    return {"message": "Transaction not found"}, 404

# Delete operation
# delete existing transactions
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    for transaction in transactions:
        if transaction["id"] == transaction_id:
            transactions.remove(transaction)
            break
    return redirect(url_for("get_transaction"))

# check if the current script is the main program
if __name__ == "__main__":
    # Run the Flask app with debug enabled to view detailed error messages in the browser
    app.run(debug=True)

    