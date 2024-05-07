from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculator():
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']
        
        try:
            num1 = float(num1)
            num2 = float(num2)
            
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 == 0:
                    result = 'Error: Division by zero'
                else:
                    result = num1 / num2
            else:
                result = 'Invalid operation'
        except ValueError:
            result = 'Error: Invalid input'
        
        return render_template('calculator.html', result=result)
    
    return render_template('calculator.html')

if __name__ == '__main__':
    app.run(debug=True)