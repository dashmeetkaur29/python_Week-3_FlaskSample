from flask import Flask, request, render_template

app = Flask(__name__)

# http://127.0.0.1:5000/
@app.route('/')
def hello_world():
    return '<h1> Hello World </h1>'


# Using Jinja2 template
# http://127.0.0.1:5000/welcome
@app.route('/welcome')
def welcome():
    return render_template('hello.html') #Using render function from flask


# Using Jinja2 template for PATH parameter
# http://127.0.0.1:5000/welcome/Dashmeet
@app.route('/welcome/<name>')
def welcome_name(name):
    return render_template('welcome.html', name=name)  # Passing Parameter to template


# http://127.0.0.1:5000/name
@app.route('/name')
def my_name():
    return '<h1> Dashmeet </h1> Kaur'

#app.add_url_rule('/','name',my_name)


# GET request is default
# http://127.0.0.1:5000/sum?a=100&b=20
@app.route('/sum', methods=['GET'])
def add_number():
    a = request.args.get('a')
    b = request.args.get('b')
    c = int(a) + int(b)
    return 'SUM =' + str(c)


# http://127.0.0.1:5000/user-data
@app.route('/user-data', methods=['GET', 'POST'])
def user_data():
    if request.method == 'POST':
        first_name = request.form.get('fName')
        last_name = request.form.get('lName')
        result = '''
                <h1> First Name : {0}<h1>
                <h1> Last Name : {1}<h1>
        '''
        return result.format(first_name,last_name)
    return '<h2>No get method is allowed only POST method is allowed!<h2>'



# http://127.0.0.1:5000/user
@app.route('/user')
def user_form():
    return render_template('userForm.html')


if __name__ == '__main__':
    app.run()
