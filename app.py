from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello You are in Ram's World!";

@app.route("/education")
def learn():
    return "I am learning web development with Python and Flask"; 

@app.route("/<name>")
def subject(name):
    return f"I am learning {name}";   

@app.route("/square/<int:number>")
def show_square(number):
    return f"Square of {number}  is: " + str(number*number);      

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 3000)
