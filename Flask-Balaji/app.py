from flask import Flask, render_template, request,session

app = Flask(__name__)
app.secret_key ='a'
'''def showall():
    sql= "SELECT * from USER"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The Name is : ",  dictionary["NAME"])
        print("The E-mail is : ", dictionary["EMAIL"])
        print("The Contact is : ",  dictionary["CONTACT"])
        print("The Adress is : ",  dictionary["ADDRESS"])
        print("The Role is : ",  dictionary["ROLE"])
        print("The Branch is : ",  dictionary["BRANCH"])
        print("The Password is : ",  dictionary["PASSWORD"])
        dictionary = ibm_db.fetch_both(stmt)
        '''       '''
def getdetails(email,password):
    sql= "select * from USER where email='{}' and password='{}'".format(email,password)
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The Name is : ",  dictionary["NAME"])
        print("The E-mail is : ", dictionary["EMAIL"])
        print("The Contact is : ", dictionary["CONTACT"])
        print("The Address is : ", dictionary["ADDRESS"])
        print("The Role is : ", dictionary["ROLE"])
        print("The Branch is : ", dictionary["BRANCH"])
        print("The Password is : ", dictionary["PASSWORD"])
        dictionary = ibm_db.fetch_both(stmt)'''
        
def insertdb(conn,name,email,gender,contact,date,doctor,location,hospital):
    sql= "INSERT into APP VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(name,email,gender,contact,date,doctor,location,hospital)
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))

def insertdb1(conn,name,email,feedback):
    sql= "INSERT into FEED VALUES('{}','{}','{}')".format(name,email,feedback)
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))

def insertdb2(conn,name,email,gender,contact,date):
    sql= "INSERT into MEDICINE VALUES('{}','{}','{}','{}','{}')".format(name,email,gender,contact,date)
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))
    
import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=1bbf73c5-d84a-4bb0-85b9-ab1a4348f4a4.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;PORT=32286;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=zmk67414;PWD=ChyAigq7rWQliBMi",'','')
print(conn)
print("connection successful...")

@app.route('/')
def index():
    return render_template('Main.html')

@app.route('/service')
def service():
    return render_template('Services.html')


@app.route('/about')
def about():
    return render_template('Aboutus.html')


@app.route('/myprofile')
def myprofile():
    return render_template('Myprofile.html')


@app.route('/feedback')
def feedback():
    return render_template('Feedback.html')


@app.route('/schedule')
def schedule():
    return render_template('Schedule.html')

@app.route('/medicine')
def medicine():
    return render_template('Learn.html')

@app.route('/main')
def main():
    return render_template('Main.html')

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        gender = request.form['gender']
        contact = request.form['mobile']
        date = request.form['date']
        doctor = request.form['doctor']
        location=request.form['location']
        hospital=request.form['hospital']
        #inp=[name,email,contact,address,role,branch,password]
        insertdb(conn,name,email,gender,contact,date,doctor,location,hospital)
        return render_template('Main.html')


@app.route('/feed', methods=['POST','GET'])
def feed():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        feedback = request.form['feedback']
    #inp=[name,email,contact,address,role,branch,password]
        insertdb1(conn,name,email,feedback)
        return render_template('Feedback.html')
    
@app.route('/medi', methods=['POST','GET'])
def medi():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['dosage']
        gender = request.form['frequency']
        contact = request.form['sdate']
        date = request.form['edate']
        
        #inp=[name,email,contact,address,role,branch,password]
        insertdb2(conn,name,email,gender,contact,date)
        return render_template('Main.html')
        

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['pwd']
        sql= "select * from USER where email='{}' and password='{}'".format(email,password)
        stmt = ibm_db.exec_immediate(conn, sql)
        userdetails = ibm_db.fetch_both(stmt)
        print(userdetails)
        if userdetails:
            session['register'] =userdetails["EMAIL"]
            return render_template('userprofile.html',name=userdetails["NAME"],email= userdetails["EMAIL"],contact= userdetails["CONTACT"],address=userdetails["ADDRESS"],role=userdetails["ROLE"],branch=userdetails["BRANCH"])
        else:
            msg = "Incorrect Email id or Password"
            return render_template("login.html", msg=msg)
    return render_template('login.html')


if __name__ =='__main__':
    app.run( debug = True , port=5000 , host='0.0.0.0')
