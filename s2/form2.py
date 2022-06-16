from flask import Flask,render_template,request
from flask_mysqldb import MySQL
app=Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_PORT']=3307
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='1234'
app.config['MYSQL_DB']='flask'
mysql=MySQL(app)
@app.route('/')
def home():
   return render_template("index.html")
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO a VALUES(%s,%s)''',(name,age))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"
@app.route("/output/")
def output():
    cursor = mysql.connection.cursor()
    output= cursor.execute('SELECT * FROM a')
    data = cursor.fetchall()
    return render_template("output.html", data = data) 
if __name__=="__main__":
    app.run(debug=True,host="localhost",port="2000")