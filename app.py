from flask import Flask, render_template, request,session

app = Flask(__name__)
app.secret_key ='a'
def showall():
    sql= "SELECT * from APPOINTMENT"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The DEPARTMENT is : ",  dictionary["DEPARTMENT"])
        print("The DOCTOR is : ", dictionary["DOCTOR"])
        print("The DATE is : ",  dictionary["DATE"])
        print("The TIME is : ",  dictionary["TIME"])
        print("The FULLNAME is : ",  dictionary["FULLNAME"])
        print("The PHONE NUMBER is : ",  dictionary["PHONE NUMBER"])
        print("The EMAIL is : ",  dictionary["EMAIL"])
        print("The WHATSAP NUMBER is : ",dictionary["WHATSAP NUMBER"])
        print("The PROBLEM is:", dictionary["PROBLEM"])
        dictionary = ibm_db.fetch_both(stmt)
        
def getdetails(email,password):
    sql= "select * from USER where email='{}' and password='{}'".format(email,password)
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        print("The DEPARTMENT is : ",  dictionary["DEPARTMENT"])
        print("The DOCTOR is : ", dictionary["DOCTOR"])
        print("The DATE is : ", dictionary["DATE"])
        print("The TIME is : ", dictionary["TIME"])
        print("The FULLNAME is : ", dictionary["FULLNAME"])
        print("The PHONE NUMBER is : ", dictionary["PHONE NUMBER"])
        print("The EMAIL is : ", dictionary["EMAIL"])
        print(" The WHATSAP NUMBER is : ", dictionary["WHATSAP NUMBER"])
        print("The PROBLEM is : ",dictionary["PROBLEM"])
        dictionary = ibm_db.fetch_both(stmt)
        
def insertdb(conn,DEPARTMENT,DOCTOR,DATE,TIME,FULLNAME,PHONE NUMBER,EMAIL,WHATSAP NUMBER,PROBLEM):
    sql= "INSERT into USER VALUES('{}','{}','{}','{}','{}','{}','{}')".format(name,email,contact,address,role,branch,password)
    stmt = ibm_db.exec_immediate(conn, sql)
    print ("Number of affected rows: ", ibm_db.num_rows(stmt))
    
    
import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=b1bc1829-6f45-4cd4-bef4-10cf081900bf.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32304;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=rqy41363;PWD=9ozyrz3LXNz0Fwhv",'','')
print(conn)
print("connection successful...")

@app.route('/')
def index():
    return render_template('registration.html')

@app.route('/register', methods=['POST','GET'])
def register():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        contact = request.form['mobile']
        address = request.form['address']
        role = request.form['role']
        if role =="0":
            role = "Faculty"
        else:
            role = "Student"
        branch = request.form['branch']
        password = request.form['pwd']
        
        #inp=[name,email,contact,address,role,branch,password]
        insertdb(conn,name,email,contact,address,role,branch,password)
        return render_template('login.html')
        

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
    app.run( debug = True)
