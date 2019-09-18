from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login_page():
    return render_template('login.html')

@app.route('/user/<user_id>', methods=['GET', 'POST'])
def user_page(user_id):
    return render_template('user_view.html')

@app.route('/user/<user_id>/document', methods=['GET', 'POST'])
def view_documents(user_id):
    return render_template('document_view.html')

@app.route('/user/<user_id>/document/<document_id>', methods=['GET', 'POST'])
def view_document(user_id, document_id):
    return "User: " + str(user_id) + " Document " + str(document_id)

@app.route('/user/<user_id>/document/<document_id>/download')
def download_document(user_id, document_id):
    return "User: " + str(user_id) + " Document " + str(document_id) + " Download"