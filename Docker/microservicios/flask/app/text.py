from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('app.html')
@app.route('/resp', methods=['POST'])
def resp():
    if request.method == 'POST':
		num1 = request.form['n1']
		num2 = request.form['n2']
		oper = request.form['operacion']
        if oper == "+":
			sum = float(num1) + float(num2)
			return render_template('app.html', sum = sum)
		elif oper == '-' :
			sum = float(num1) - float(num2)
			return render_template('app.html', sum = sum)
		elif oper == '*':
			sum = float(num1) * float(num2)
			return render_template('app.html', sum = sum)
		elif oper == '/':
			sum = float(num1) / float(num2)
			return render_template('app.html', sum = sum)
		else:
			return render_template('app.html') 
    
    return oper

if __name__ == "__main__":
    app.run(debug=True)