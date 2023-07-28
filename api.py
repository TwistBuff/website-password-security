from flask import Flask, render_template, request
from pass_gen import generate, checker


app = Flask(__name__)

@app.route('/')
def index():
    output = generate(16, True, True, True, True)
    length, digits, uppercase, lowercase, symbol = checker(output)
    return render_template('index.html',
                           output = output,
                           
                           length = length,
                           digits = digits, 
                           uppercase = uppercase,
                           lowercase = lowercase,
                           symbol = symbol)

@app.route('/process_form', methods=['POST'])
def process_form():
    passwrd = request.form['password']
    print(passwrd)
    
    if all(list(checker(passwrd))):
        return 'YES!! Your password is good.'
    else :
        return 'WTF!!!! COME UP WITH A GOOD PASSWORD DAMN!!!'


app.run(debug=True, host='0.0.0.0', port=80)