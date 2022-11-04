from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def home():

    names={'Ram':'USA','Singh':'India'}
    return render_template("index.html",user=names)

if __name__=='__main__':
    app.run(debug=True,host='localhost',port=3000)


