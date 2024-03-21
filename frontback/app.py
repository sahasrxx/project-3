from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/',methods=['GET'])
def homepage():
    return 'you are in homePage'

@app.route('/index',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/index2',methods=['GET'])
def login():
    return render_template('index2.html')

@app.route('/login-form',methods=['POST'])
def login_form_data():
    num1= request.form['a']
    num2= request.form['b']
    return {'response':int(num1)+int(num2)}

#MATHS
#-------------------------------------------
'''ADDITION'''
@app.route('/add',methods=['GET'])
def addition():
    return render_template('add.html')

@app.route('/addition-form',methods=['POST'])
def addition_form_data():
    num1= request.form['a']
    num2= request.form['b']
    return [int(num1)+int(num2)]



'''subtraction'''
@app.route('/sub',methods=['GET'])
def subtraction():
    return render_template('sub.html')

@app.route('/subtraction-form',methods=['POST'])
def subtraction_form_data():
    num1= request.form['a']
    num2= request.form['b']
    return [abs(int(num1)-int(num2))]



'''MULTIPLICATION'''
@app.route('/mul',methods=['GET'])
def multiplication():
    return render_template('multi.html')

@app.route('/multiplication-form',methods=['POST'])
def multiplication_form_data():
    num1= request.form['a']
    num2= request.form['b']
    return [(int(num1)*int(num2))]



'''DIVISION'''
@app.route('/div',methods=['GET'])
def division():
    return render_template('div.html')

@app.route('/division-form',methods=['POST'])
def division_form_data():
    num1= request.form['a']
    num2= request.form['b']
    return [(int(num1)/int(num2))]