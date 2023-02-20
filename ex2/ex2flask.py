from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def ex2():
    return '''
    <p><strong> Home </strong> </p>
    <p>Enter an integer to find out if it is even or odd:</p>
        <form method="get" action="/result">
            <input type="text" name="number" required>
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/result')
def result():
    try:
        num = int(request.args.get('number'))
        if num % 2 == 0:
            result = 'even'
        else:
            result = 'odd'
    except ValueError:
        string = request.args.get('number')
        return f'{string} is not an integer! <a href="/">Go Home</a>'
    return f'{num} is {result}. <a href="/">Go Home</a>'

if __name__ == '__main__':
    app.run()