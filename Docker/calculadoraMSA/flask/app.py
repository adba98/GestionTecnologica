#sudo docker build -f Docker_resta -t resta .
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/total', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        num1 = request.form['n1']
        num2 = request.form['n2']
        op = request.form['op']

        if op == 'suma':
            sum = float(num1) + float(num2)
            return render_template('index.html', sum=sum)

        elif op == 'resta':
            sum = float(num1) - float(num2)
            return render_template('index.html', sum=sum)

        elif op == 'multi':
            sum = float(num1) * float(num2)
            return render_template('index.html', sum=sum)

        elif op == 'div':
            sum = float(num1) / float(num2)
            return render_template('index.html', sum=sum)
        else:
            return render_template('index.html')


if __name__ == ' __main__':
    app.debug = True
    app.run()