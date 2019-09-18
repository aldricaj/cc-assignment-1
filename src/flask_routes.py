from flask import Flask

app = Flask(__name__)

@app.route('/')
def login_page():
    return 'hello'

@app.route('/user/<user_id>')
def user_page(user_id):
    return "User: " + str(user_id);

@app.route('/user/<user_id>/document')
def view_documents(user_id):
    return "User: " + str(user_id) + " Documents"

@app.route('/user/<user_id>/document/<document_id>')
def view_document(user_id, document_id):
    return "User: " + str(user_id) + " Document " + str(document_id)

@app.route('/user/<user_id>/document/<document_id>/download')
def download_document(user_id, document_id):
    return "User: " + str(user_id) + " Document " + str(document_id) + " Download"