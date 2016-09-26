from flask import Flask, render_template
app3 = Flask(__name__)##creates an instance of a flask and instatiates its name

@app3.route("/")

def hello_world():
    return "No hablo queso-v3"

coll = [1, 3, 3, 7]

@app3.route("/my_first_template")
def tet_template():
    return render_template("foo.html", foo = "SILENCIO", fool=coll)

    
if __name__=="__main__":
        app3.debug = True
        app3.run()
        
