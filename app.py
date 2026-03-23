from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None

    if request.method == 'POST':
        name = request.form['name']
        attendance = list(map(int, request.form['attendance'].split(',')))

        percentage = sum(attendance) / len(attendance) * 100

        if percentage >= 75:
            category = "Good"
        elif percentage >= 50:
            category = "Average"
        else:
            category = "Low"

        result = (name, percentage, category)

    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
