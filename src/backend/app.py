from flask import Flask, render_template

app=Flask(__name__) 

@app.route('/')
def index():
    return "TEST 3"
    # return render_template('index.html')

@app.route("/post", methods = ["POST"])
def agenda():
    print("test2")
    return {'success': True}
if __name__ == '__main__':
    app.run(debug=True, port=5000)