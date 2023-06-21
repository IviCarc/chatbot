from flask import Flask

app=Flask(__name__) 

@app.route('/')
def index():
    return "TEST 3"

@app.route("/post", methods = ["POST"])
def agenda():
    print("test2")
    return {'success': True}
if __name__ == '__main__':
    app.run(debug=True, port=5000)