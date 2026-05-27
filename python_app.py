from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ""

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        message = f"Hello your name and age: {name}, {age}"

    return f'''
    <html>
    <head>
        <title>Name and Age Form</title>
    </head>
    <body>
        <h2>Enter Your Details</h2>

        <form method="POST">
            <table border="1" cellpadding="10">
                <tr>
                    <th>Name</th>
                    <th>Age</th>
                </tr>
                <tr>
                    <td><input type="text" name="name" required></td>
                    <td><input type="number" name="age" required></td>
                </tr>
            </table>

            <br>
            <input type="submit" value="Submit">
        </form>

        <h3>{message}</h3>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
