from flask import Flask, render_template
import random

app = Flask(__name__)##creates an instance of a flask and instatiates its name

@app.route("/occupations")
def hello_world():
    occL = []
    ans = """<!DOCTYPE html> <html> <head> <title>Occupation Statistics</title></head> <table style="width:100>"""
    for k in occDict:
        ans = ans + """<tr> <th>""" + k + """</th>""" + """<th>""" + str(occDict[k]) + """</th> </tr>"""
        occL.append(k)    
    ans = ans + """</table>"""
    ans = ans + random.choice(occL)
    ans = ans + """</html>"""
    return ans


def buildDict(ocFile): 
    occFile = open(ocFile, 'r')
    occupations = occFile.read()
    occDict = {}
    
    i = 0;
    j = 0;

    while i < len(occupations) :
        j = i;
        while j < len(occupations) :
            if occupations[j] == ",":
                tempKey = occupations[i:j]
                split = j + 1
            if occupations[j] == "\n":
                tempVal = occupations[split:j]
                #print "tempVal: " + tempVal
                try:
                    occDict[tempKey] = float(tempVal)
                except:
                    occDict[tempKey] = tempVal
                i = j;
                break
            j+=1
        i+=1
    return occDict

occDict = buildDict("occupations.csv")







@app.route("/r2")
def hello_world2():
    return "no hablo queso 2"

@app.route("/r3")
def hello_world3():
    return "no hablo queso 3"

coll = [1, 3, 3, 7]

@app.route("/my_first_template")
def tet_template():
    return render_template("foo.html", foo = "SILENCIO", fool=coll)

    
if __name__=="__main__":
        app.debug = True
        app.run()
        
