from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    #result={'maths':80,'c':70,'java':60}
    #print(result)
    #name = "abc"
    #list1 = [1,2,3]
    return render_template('home.html')
if __name__=="__main__":
    app.run(debug=True)
