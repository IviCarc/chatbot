from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    print("GET")
    return render_template('index.html')
    # return render_template("index.html")
    # return ('TEST3')

@app.route("/post", methods = ["POST"])
def agenda():
    print("test2")
    return {'success': True}

if __name__ == '__main__':
    app.run(debug=True, port=80)

# app.run()