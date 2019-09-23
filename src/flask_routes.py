from flask import Flask, render_template, request, redirect
import repo
import login
import model

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login_page():
    # crappy do-it-all function for login's this should be seperated out
    if request.method == 'POST':
        arguments = request.form.copy()

        if arguments['action_type'] == 'create':
            arguments.update({'password_hash':login.hash_password(arguments['password'])})
            del arguments['password']
            del arguments['action_type']
            user = model.User(**arguments)
            user = repo.create_user(user)
            if user:
                return redirect(f'./user/{str(user.user_id)}')
            else:
                errors = 'User Already Exists'
        
        else:
            user = login.check_user(request.form['username'],
                                request.form['password'])
            if user:
                return redirect(f'./user/{str(user.user_id)}')
            else:
                errors = 'Invalid password'
    return render_template('login.html')

@app.route('/user/<user_id>', methods=['GET', 'POST'])
def user_page(user_id):
    user = repo.get_user_by_id(user_id)
    return render_template('user_view.html', user=user)

@app.route('/user/<user_id>/document', methods=['GET', 'POST'])
def view_documents(user_id):
    return render_template('document_view.html')

@app.route('/user/<user_id>/document/<document_id>', methods=['GET', 'POST'])
def view_document(user_id, document_id):
    return "User: " + str(user_id) + " Document " + str(document_id)

@app.route('/user/<user_id>/document/<document_id>/download')
def download_document(user_id, document_id):
    return "User: " + str(user_id) + " Document " + str(document_id) + " Download"