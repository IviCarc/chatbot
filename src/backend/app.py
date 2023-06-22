from flask import Flask, render_template

app=Flask(__name__) 

@app.route('/')
def index():
    print("HOLA")
    return "TEST 3"
    # return render_template('index.html')

@app.route("/post", methods = ["POST"])
def agenda():
    print("test2")
    return {'success': True}
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)