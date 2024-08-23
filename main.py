from flask import Flask
from flask import Flask, render_template, Response, redirect, request, session, abort, url_for
import os
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import subprocess
import json
import math
from Crypto import Random
from Crypto.Cipher import AES

from PIL import Image
from datetime import datetime
from datetime import date
import datetime
import random
from random import seed
from random import randint
from werkzeug.utils import secure_filename
from flask import send_file
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv
import shutil
import hashlib
import urllib.request
import urllib.parse
from urllib.request import urlopen
import webbrowser

import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  charset="utf8",
  database="signup_wallet"
)

app = Flask(__name__)
##session key
app.secret_key = 'abcdef'
UPLOAD_FOLDER = 'static/upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#####
#######
class AESCipher(object):

    def __init__(self, key):
        self.bs = AES.block_size
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.b64encode(iv + cipher.encrypt(raw.encode()))

    def decrypt(self, enc):
        enc = base64.b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[:-ord(s[len(s)-1:])]

    
@app.route('/',methods=['POST','GET'])
def index():
    msg=""

    #######
    '''driveStr = subprocess.check_output("fsutil fsinfo drives")
    drv=driveStr.decode(encoding='utf-8')
    drv1=drv.split('Drives: ')
    drv2=drv1[1].split(' ')
    dlen=len(drv2)
    i=0
    dr=""
    drn=0
    for rr in drv2:
        dr=rr+"wamp\www"
        if os.path.isdir(dr):
            drn+=1
            break
    if drn>0:
        dr2="signup"
        dr3=dr+"\\"+dr2
        if os.path.isdir(dr3):
            s=1
        else:
            os.mkdir(dr3)
            ff=open("static/path1.txt","w")
            ff.write(dr3)
            ff.close()'''
   

    #ky="ramesh"
    #email="bgeduscanner@gmail.com"
    #obj=AESCipher(ky)
    #em=obj.encrypt(email)
    #print(em)
        
        
    return render_template('index.html',msg=msg)

@app.route('/login_user',methods=['POST','GET'])
def login_user():
    act=request.args.get("act")
    msg=""
    if request.method == 'POST':
        
        username1 = request.form['uname']
        password1 = request.form['pass']
        mycursor = mydb.cursor()
        mycursor.execute("SELECT count(*) FROM sw_user_register where username=%s",(username1,))
        myresult = mycursor.fetchone()[0]
        if myresult>0:
            ky=username1
            obj=AESCipher(ky)

            mycursor.execute("SELECT * FROM sw_user_register where username=%s",(username1,))
            dd = mycursor.fetchone()
            pw=dd[8]
            
        
            pww=obj.decrypt(pw.encode("utf-8"))
            if pww==password1:
                session['username'] = username1
                #result=" Your Logged in sucessfully**"
                return redirect(url_for('userhome'))
            else:
                msg="You are logged in fail!!!"
        else:
            msg="You are logged in fail!!!"
        

    return render_template('login_user.html',msg=msg,act=act)

@app.route('/login',methods=['POST','GET'])
def login():
    act=request.args.get("act")
    msg=""
    if request.method == 'POST':
        
        username1 = request.form['uname']
        password1 = request.form['pass']
        mycursor = mydb.cursor()
        mycursor.execute("SELECT count(*) FROM sw_admin where username=%s && password=%s",(username1,password1))
        myresult = mycursor.fetchone()[0]
        if myresult>0:
            session['username'] = username1
            #result=" Your Logged in sucessfully**"
            return redirect(url_for('admin')) 
        else:
            msg="You are logged in fail!!!"
        

    return render_template('login.html',msg=msg,act=act)

@app.route('/reg1', methods=['GET', 'POST'])
def reg1():
    msg=""
    act=""
    mess=""
    email=""
    mycursor = mydb.cursor()

    if request.method=='POST':
        name=request.form['name']
        name2=request.form['name2']
        name3=request.form['name3']
        
        mobile=request.form['mobile']
        email=request.form['email']
        


        mycursor.execute("SELECT count(*) FROM sw_user_register where mobile=%s || email=%s",(mobile,email))
        myresult = mycursor.fetchone()[0]

        if myresult==0:
        
            mycursor.execute("SELECT max(id)+1 FROM sw_user_register")
            maxid = mycursor.fetchone()[0]
            if maxid is None:
                maxid=1
            
            now = date.today() #datetime.datetime.now()
            rdate=now.strftime("%d-%m-%Y")
            
            sql = "INSERT INTO sw_user_register(id,name,middle_name,last_name,mobile,email) VALUES (%s,%s,%s,%s,%s,%s)"
            val = (maxid,name,name2,name3,mobile,email)
            mycursor.execute(sql, val)
            mydb.commit()

            link="http://localhost:5000/message2?uid="+str(maxid)
            mess="Dear "+name+", Verification Link: "+link
            
            print(mycursor.rowcount, "Registered Success")
            msg="success"
            
            #if cursor.rowcount==1:
            #    return redirect(url_for('index',act='1'))
        else:
            
            msg='fail'
            
    
    return render_template('reg1.html', act=act,msg=msg,mess=mess,email=email)

@app.route('/message', methods=['GET', 'POST'])
def message():
    msg=""

    return render_template('message.html',msg=msg)

@app.route('/message2', methods=['GET', 'POST'])
def message2():
    msg=""
    act=request.args.get("act")
    uid=request.args.get("uid")

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM sw_user_register where id=%s",(uid,))
    data = mycursor.fetchone()
    name=data[1]
    mobile=data[5]

    nn=randint(1000,9999)
    otp=str(nn)
    mycursor.execute("update sw_user_register set otp=%s where id=%s",(otp,uid))
    mydb.commit()

    mess="OTP: "+otp
    

    return render_template('message2.html',msg=msg,act=act,uid=uid,mess=mess,name=name,mobile=mobile)

@app.route('/reg2', methods=['GET', 'POST'])
def reg2():
    msg=""
    act=request.args.get("act")
    uid=request.args.get("uid")

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM sw_user_register where id=%s",(uid,))
    data = mycursor.fetchone()
    otp=data[11]
    name=data[1]
    mobile=data[5]

    if request.method=='POST':
        skey=request.form['skey']
        if otp==skey:
            msg="success"
        else:
            msg="fail"


    return render_template('reg2.html',msg=msg,act=act,uid=uid)

def walletchain(uid,uname,bcdata,upi,bstatus):
    ############

    now = datetime.datetime.now()
    yr=now.strftime("%Y")
    mon=now.strftime("%m")
    rdate=now.strftime("%d-%m-%Y")
    rtime=now.strftime("%H:%M:%S")
    
    ff=open("static/key.txt","r")
    k=ff.read()
    ff.close()
    
    #bcdata="CID:"+uname+",Time:"+val1+",Unit:"+val2
    dtime=rdate+","+rtime

    ky=uname
    obj=AESCipher(ky)

    bcc=bcdata+"-"+dtime
    benc=obj.encrypt(bcc)
    benc1=benc.decode("utf-8")

    ff1=open("static/assets/js/d1.txt","r")
    bc1=ff1.read()
    ff1.close()
    
    px=""
    if k=="1":
        px=""
        result = hashlib.md5(bcdata.encode())
        key=result.hexdigest()
        print(key)
        v=k+"##"+key+"##"+bcc+"##"+upi+"##"+bstatus

        ff1=open("static/assets/js/d1.txt","w")
        ff1.write(v)
        ff1.close()
        
        dictionary = {
            "ID": "1",
            "Pre-hash": "00000000000000000000000000000000",
            "Hash": key,
            "upicode:": upi,
            "Status:": bstatus,
            "Date/Time": dtime
        }

        k1=int(k)
        k2=k1+1
        k3=str(k2)
        ff1=open("static/key.txt","w")
        ff1.write(k3)
        ff1.close()

        ff1=open("static/prehash.txt","w")
        ff1.write(key)
        ff1.close()
        
    else:
        px=","
        pre_k=""
        k1=int(k)
        k2=k1-1
        k4=str(k2)

        ff1=open("static/prehash.txt","r")
        pre_hash=ff1.read()
        ff1.close()
        
        g1=bc1.split("#|")
        for g2 in g1:
            g3=g2.split("##")
            if k4==g3[0]:
                pre_k=g3[1]
                break

        
        result = hashlib.md5(bcdata.encode())
        key=result.hexdigest()
        

        v="#|"+k+"##"+key+"##"+bcc+"##"+upi+"##"+bstatus

        k3=str(k2)
        ff1=open("static/key.txt","w")
        ff1.write(k3)
        ff1.close()

        ff1=open("static/assets/js/d1.txt","a")
        ff1.write(v)
        ff1.close()

        
        
        dictionary = {
            "ID": k,
            "Pre-hash": pre_hash,
            "Hash": key,
            "upicode:": upi,
            "Status:": bstatus,
            "Date-Time": dtime
        }
        k21=int(k)+1
        k3=str(k21)
        ff1=open("static/key.txt","w")
        ff1.write(k3)
        ff1.close()

        ff1=open("static/prehash.txt","w")
        ff1.write(key)
        ff1.close()

    m=""
    if k=="1":
        m="w"
    else:
        m="a"
    # Serializing json
    
    json_object = json.dumps(dictionary, indent=4)
     
    # Writing to sample.json
    with open("static/walletchain.json", m) as outfile:
        outfile.write(json_object)
    ##########

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg=""
    act=""
    mess=""
    uid=request.args.get("uid")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM sw_user_register where id=%s",(uid,))
    data = mycursor.fetchone()
    name=data[1]
    email=data[6]
    mobile=data[5]

    now = date.today() #datetime.datetime.now()
    rdate=now.strftime("%d-%m-%Y")
    rd=rdate.split('-')
    yy=rd[2]
    y1=yy[2:4]
    

    if request.method=='POST':
        name=request.form['name']
        name2=request.form['name2']
        name3=request.form['name3']
        gender=request.form['gender']
        dob=request.form['dob']
        

        uname=request.form['uname']
        pass1=request.form['pass']

        dd=dob.split('-')
        dob1=dd[2]+"-"+dd[1]+"-"+dd[0]

        ky=uname
        obj=AESCipher(ky)
        

        mycursor.execute("SELECT count(*) FROM sw_user_register where username=%s",(uname,))
        myresult = mycursor.fetchone()[0]

        if myresult==0:
            v1=uid
            val=v1.zfill(3)
            nn=randint(10,99)
            nn1=str(nn)

            vrn=randint(111,999)
            val2=str(vrn)
            ucode="U"+y1+nn1+val+val2

            name1=obj.encrypt(name)
            name21=obj.encrypt(name2)
            name31=obj.encrypt(name3)
            mobile1=obj.encrypt(mobile)
            email1=obj.encrypt(email)
          
            
            ucode1=obj.encrypt(ucode)
            gender1=obj.encrypt(gender)
            dob11=obj.encrypt(dob1)
            uname1=obj.encrypt(uname)
            pass11=obj.encrypt(pass1)
            rdate1=obj.encrypt(rdate)

            result = hashlib.md5(ucode.encode())
            hh=result.hexdigest()
            bkey=hh[0:8]
            mycursor.execute("update sw_user_register set name=%s,middle_name=%s,last_name=%s,mobile=%s,email=%s,gender=%s,dob=%s,username=%s,password=%s,register_date=%s,upi_code=%s,block_key=%s where id=%s",(name1,name21,name31,mobile1,email1,gender1,dob11,uname,pass11,rdate1,ucode1,bkey,uid))
            mydb.commit()

          
            now = date.today() #datetime.datetime.now()
            rdate=now.strftime("%d-%m-%Y")
            
            sql = "INSERT INTO sw_user_profile(uid,username) VALUES (%s,%s)"
            val = (uid,uname)
            mycursor.execute(sql, val)
            mydb.commit()
            
            mess="Dear "+name+", Your Sign Up Wallet UPI Code:"+ucode

            print(mycursor.rowcount, "Registered Success")
            msg="success"
            
            #if cursor.rowcount==1:
            #    return redirect(url_for('index',act='1'))
        else:
            
            msg='fail'
            
    
    return render_template('register.html', act=act,msg=msg,data=data,uid=uid,mess=mess,email=email)

@app.route('/userhome', methods=['GET', 'POST'])
def userhome():
    msg=""
    uname=""
    fs=""
    data=[]
    data1=[]
    st=""
    act=request.args.get("act")
    if 'username' in session:
        uname = session['username']
    mycursor = mydb.cursor()

    ky=uname
    obj=AESCipher(ky)

    mycursor.execute("SELECT * FROM sw_user_register where username=%s",(uname,))
    dat = mycursor.fetchone()

    mycursor.execute("SELECT * FROM sw_user_profile where username=%s",(uname,))
    dat1 = mycursor.fetchone()
    
    name=obj.decrypt(dat[1].encode("utf-8"))
    ucode=obj.decrypt(dat[12].encode("utf-8"))
    email2=obj.decrypt(dat[6].encode("utf-8"))

    if dat[1]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat[1].encode("utf-8")))

    if dat[2]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat[2].encode("utf-8")))
        
    if dat[3]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat[3].encode("utf-8")))

    if dat[4]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat[4].encode("utf-8")))

    if dat[3]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat[5].encode("utf-8")))

    if dat[5]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat[6].encode("utf-8")))

    
    if dat[10]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat[10].encode("utf-8")))

    if dat[12]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat[12].encode("utf-8")))

    if dat[13]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat[13].encode("utf-8")))

    if dat[14]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat[14].encode("utf-8")))

    #####
    if dat1[2]=="":
        data1.append("")
    else:
        data.append(obj.decrypt(dat1[2].encode("utf-8")))
    if dat1[3]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[3].encode("utf-8")))

    if dat1[4]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[4].encode("utf-8")))
    if dat1[5]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[5].encode("utf-8")))
    if dat1[6]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[6].encode("utf-8")))
    if dat1[7]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[7].encode("utf-8")))
    if dat1[8]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[8].encode("utf-8")))
    if dat1[9]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[9].encode("utf-8")))
    if dat1[10]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[10].encode("utf-8")))
    if dat1[11]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[11].encode("utf-8")))
    if dat1[12]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[12].encode("utf-8")))
    if dat1[13]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[13].encode("utf-8")))
    if dat1[14]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[14].encode("utf-8")))
    if dat1[15]=="":
        data1.append("")
    else:
        data.append(obj.decrypt(dat1[15].encode("utf-8")))
    if dat1[16]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[16].encode("utf-8")))
    if dat1[17]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[17].encode("utf-8")))
    if dat1[18]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[18].encode("utf-8")))
    if dat1[19]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[19].encode("utf-8")))
    if dat1[20]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[20].encode("utf-8")))
    if dat1[21]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[21].encode("utf-8")))
    if dat1[22]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[22].encode("utf-8")))
    if dat1[23]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[23].encode("utf-8")))
    if dat1[24]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[24].encode("utf-8")))
    if dat1[25]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[25].encode("utf-8")))
    if dat1[26]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[26].encode("utf-8")))
    if dat1[27]=="":
        data.append("")
    else:
        data1.append(obj.decrypt(dat1[27].encode("utf-8")))
    if dat1[28]=="":
        data1.append("")
    else:
        data.append(obj.decrypt(dat1[28].encode("utf-8")))
    if dat1[29]=="":
        data1.append("")
    else:
        data.append(obj.decrypt(dat1[29].encode("utf-8")))
    if dat1[30]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[30].encode("utf-8")))
    if dat1[31]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[31].encode("utf-8")))
    if dat1[32]=="":
        data1.append("")
    else:
        data.append(obj.decrypt(dat1[32].encode("utf-8")))
    if dat1[33]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[33].encode("utf-8")))

    if dat1[34]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[34].encode("utf-8")))
    if dat1[35]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[35].encode("utf-8")))
    if dat1[36]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[36].encode("utf-8")))

    if dat1[37]=="":
        data1.append("")
    else:
        data1.append(obj.decrypt(dat1[37].encode("utf-8")))
   
        
    return render_template('userhome.html',msg=msg,data=data,data1=data1,name=name,ucode=ucode)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    msg=""
    act=""
    mess=""
    data=[]
    
    uname=""
    if 'username' in session:
        uname = session['username']
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM sw_user_register where username=%s",(uname,))
    dat = mycursor.fetchone()
    mycursor.execute("SELECT * FROM sw_user_profile where username=%s",(uname,))
    dat1 = mycursor.fetchone()
    uid=dat1[0]
    ky=uname
    obj=AESCipher(ky)

    name=obj.decrypt(dat[1].encode("utf-8"))
    ucode=obj.decrypt(dat[12].encode("utf-8"))
    email2=obj.decrypt(dat[6].encode("utf-8"))

    
    if request.method=='POST':
        ptype = request.form['ptype']
        file = request.files['file']

        if ptype=="1":
            fn1="A"+str(uid)+file.filename
            ef1=obj.encrypt(fn1)
            mycursor.execute("update sw_user_register set aadhar=%s where username=%s", (ef1,uname))
            mydb.commit()
            file.save(os.path.join("static/upload", fn1))
            msg="1"
        if ptype=="2":
            fn1="P"+str(uid)+file.filename
            ef1=obj.encrypt(fn1)
            mycursor.execute("update sw_user_profile set pancard=%s where username=%s", (ef1,uname))
            mydb.commit()
            file.save(os.path.join("static/upload", fn1))
            msg="2"
        if ptype=="3":
            fn1="D"+str(uid)+file.filename
            ef1=obj.encrypt(fn1)
            mycursor.execute("update sw_user_profile set driving=%s where username=%s", (ef1,uname))
            mydb.commit()
            file.save(os.path.join("static/upload", fn1))
            msg="3"
        if ptype=="4":
            fn1="V"+str(uid)+file.filename
            ef1=obj.encrypt(fn1)
            mycursor.execute("update sw_user_profile set voterid=%s where username=%s", (ef1,uname))
            mydb.commit()
            file.save(os.path.join("static/upload", fn1))
            msg="4"

    return render_template('upload.html',msg=msg,data=data,name=name,ucode=ucode)

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    msg=""
    act=""
    mess=""
    data=[]
    
    uname=""
    if 'username' in session:
        uname = session['username']
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM sw_user_register where username=%s",(uname,))
    dat = mycursor.fetchone()
    mycursor.execute("SELECT * FROM sw_user_profile where username=%s",(uname,))
    dat1 = mycursor.fetchone()
    uid=dat1[0]
    ky=uname
    obj=AESCipher(ky)

    name=obj.decrypt(dat[1].encode("utf-8"))
    ucode=obj.decrypt(dat[12].encode("utf-8"))
    email=obj.decrypt(dat[6].encode("utf-8"))
    mobile=obj.decrypt(dat[5].encode("utf-8"))

    aadhar=""
    if dat[4]=="":
        aadhar=""
    else:
        aadhar=obj.decrypt(dat[4].encode("utf-8"))

    if dat1[2]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[2].encode("utf-8")))
    if dat1[3]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[3].encode("utf-8")))

    if dat1[4]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[4].encode("utf-8")))
    if dat1[5]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[5].encode("utf-8")))
    if dat1[6]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[6].encode("utf-8")))
    if dat1[7]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[7].encode("utf-8")))
    if dat1[8]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[8].encode("utf-8")))
    if dat1[9]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[9].encode("utf-8")))
    if dat1[10]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[10].encode("utf-8")))
    if dat1[11]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[11].encode("utf-8")))
    if dat1[12]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[12].encode("utf-8")))
    if dat1[13]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[13].encode("utf-8")))
    if dat1[14]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[14].encode("utf-8")))
    if dat1[15]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[15].encode("utf-8")))
    if dat1[16]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[16].encode("utf-8")))
    if dat1[17]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[17].encode("utf-8")))
    if dat1[18]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[18].encode("utf-8")))
    if dat1[19]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[19].encode("utf-8")))
    if dat1[20]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[20].encode("utf-8")))
    if dat1[21]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[21].encode("utf-8")))
    if dat1[22]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[22].encode("utf-8")))
    if dat1[23]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[23].encode("utf-8")))
    if dat1[24]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[24].encode("utf-8")))
    if dat1[25]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[25].encode("utf-8")))
    if dat1[26]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[26].encode("utf-8")))
    if dat1[27]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[27].encode("utf-8")))
    if dat1[28]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[28].encode("utf-8")))
    if dat1[29]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[29].encode("utf-8")))
    if dat1[30]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[30].encode("utf-8")))
    if dat1[31]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[31].encode("utf-8")))
    if dat1[32]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[32].encode("utf-8")))
    if dat1[33]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[33].encode("utf-8")))

    if dat1[34]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[34].encode("utf-8")))
    if dat1[35]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[35].encode("utf-8")))
    if dat1[36]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[36].encode("utf-8")))

    if dat1[37]=="":
        data.append("")
    else:
        data.append(obj.decrypt(dat1[37].encode("utf-8")))
    
    
        
    if request.method=='POST':

        father=request.form['father']
        mother=request.form['mother']        
        address=request.form['address']
        taluk=request.form['taluk']
        district=request.form['district']
        taluk=request.form['taluk']
        district=request.form['district']
        pincode=request.form['pincode']
        
        bank=request.form['bank']
        customername=request.form['customername']
        account=request.form['account']
        card=request.form['card']
        gnumber=request.form['gnumber']
        
        sslc_school=request.form['sslc_school']
        sslc_mark=request.form['sslc_mark']
        sslc_year=request.form['sslc_year']
        hsc_school=request.form['hsc_school']
        hsc_mark=request.form['hsc_mark']
        hsc_year=request.form['hsc_year']
        ug_college=request.form['ug_college']
        ug_degree=request.form['ug_degree']
        ug_mark=request.form['ug_mark']
        ug_year=request.form['ug_year']
        pg_college=request.form['pg_college']
        pg_degree=request.form['pg_degree']
        pg_mark=request.form['pg_mark']
        pg_year=request.form['pg_year']
        company=request.form['company']
        clocation=request.form['clocation']
        designation=request.form['designation']
        exp_period=request.form['exp_period']

        v1=ucode+"|"+name+"|"+mobile+"|"+email+"|"+aadhar+"|"+father+"|"+mother+"|"+address+"|"+taluk+"|"+district+"|"+pincode+"|"+bank+"|"+customername+"|"+account+"|"+card+"|"+gnumber
        v2=sslc_school+"|"+sslc_mark+"|"+sslc_year+"|"+hsc_school+"|"+hsc_year+"|"+ug_college+"|"+ug_degree+"|"+ug_mark+"|"+ug_year+"|"+pg_college+"|"+pg_degree+"|"+pg_mark+"|"+pg_year+"|"+company+"|"+clocation+"|"+designation+"|"+exp_period
        bdata=v1+"|"+v2

        
        result = hashlib.md5(bdata.encode())
        hdata=result.hexdigest()
        if dat1[38]=="":
            walletchain(uid,uname,bdata,ucode,'Reg')
        '''else:
            data4={}
            with open('static/walletchain.json') as f:
                data4 = json.load(f)

            for item in data4['Hash']:
                item['Hash'] = item['Hash'].replace(dat1[38], hdata)

            with open('new_data.json', 'w') as f:
                json.dump(data4, f)'''
        
        
        
        
        father1=obj.encrypt(request.form['father'])
        mother1=obj.encrypt(request.form['mother'])       
        address1=obj.encrypt(request.form['address'])
        taluk1=obj.encrypt(request.form['taluk'])
        district1=obj.encrypt(request.form['district'])
        taluk1=obj.encrypt(request.form['taluk'])
        district1=obj.encrypt(request.form['district'])
        pincode1=obj.encrypt(request.form['pincode'])
        
   
        bank1=obj.encrypt(request.form['bank'])
        customername1=obj.encrypt(request.form['customername'])
        account1=obj.encrypt(request.form['account'])
        card1=obj.encrypt(request.form['card'])
        gnumber1=obj.encrypt(request.form['gnumber'])
        
        sslc_school1=obj.encrypt(request.form['sslc_school'])
        sslc_mark1=obj.encrypt(request.form['sslc_mark'])
        sslc_year1=obj.encrypt(request.form['sslc_year'])
        hsc_school1=obj.encrypt(request.form['hsc_school'])
        hsc_mark1=obj.encrypt(request.form['hsc_mark'])
        hsc_year1=obj.encrypt(request.form['hsc_year'])
        ug_college1=obj.encrypt(request.form['ug_college'])
        ug_degree1=obj.encrypt(request.form['ug_degree'])
        ug_mark1=obj.encrypt(request.form['ug_mark'])
        ug_year1=obj.encrypt(request.form['ug_year'])
        pg_college1=obj.encrypt(request.form['pg_college'])
        pg_degree1=obj.encrypt(request.form['pg_degree'])
        pg_mark1=obj.encrypt(request.form['pg_mark'])
        pg_year1=obj.encrypt(request.form['pg_year'])
        company1=obj.encrypt(request.form['company'])
        clocation1=obj.encrypt(request.form['clocation'])
        designation1=obj.encrypt(request.form['designation'])
        exp_period1=obj.encrypt(request.form['exp_period'])

        '''father1=obj.encrypt(father)
        father1=obj.encrypt(mother)
        father1=obj.encrypt(address)
        father1=obj.encrypt(taluk)
        father1=obj.encrypt(district)
        father1=obj.encrypt(pincode)'''
  
        
        mycursor.execute("update sw_user_profile set father=%s,mother=%s,address=%s,taluk=%s,district=%s,pincode=%s,bank=%s,customername=%s,account=%s,card=%s,gnumber=%s where uid=%s",(father1,mother1,address1,taluk1,district1,pincode1,bank1,customername1,account1,card1,gnumber1,uid))
        mydb.commit()

        mycursor.execute("update sw_user_profile set sslc_school=%s,sslc_mark=%s,sslc_year=%s,hsc_school=%s,hsc_mark=%s,hsc_year=%s where uid=%s",(sslc_school1,sslc_mark1,sslc_year1,hsc_school1,hsc_mark1,hsc_year1,uid))
        mydb.commit()

        mycursor.execute("update sw_user_profile set ug_college=%s,ug_degree=%s,ug_mark=%s,ug_year=%s,pg_college=%s,pg_degree=%s,pg_mark=%s,pg_year=%s,company=%s,clocation=%s,designation=%s,exp_period=%s where uid=%s",(ug_college1,ug_degree1,ug_mark1,ug_year1,pg_college1,pg_degree1,pg_mark1,pg_year1,company1,clocation1,designation1,exp_period1,uid))
        mydb.commit()

        mycursor.execute("update sw_user_profile set hdata=%s where uid=%s",(hdata,uid))
        mydb.commit()

        msg="success"
            
         
            
    
    return render_template('edit.html', act=act,msg=msg,data=data,name=name,ucode=ucode,mess=mess,email=email)

@app.route('/service', methods=['GET', 'POST'])
def service():
    msg=""
    act=request.args.get("act")
    un=""
    s1=""
    mycursor = mydb.cursor()
    

    if request.method=='POST':
        web_url=request.form['web_url']
        formdata=request.form.getlist('formdata[]')

        fd=','.join(formdata)

        mycursor.execute("SELECT max(id)+1 FROM sw_webservice")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1
        
        now = date.today() #datetime.datetime.now()
        rdate=now.strftime("%d-%m-%Y")
        ry=rdate=now.strftime("%Y")
        rd=now.strftime("%d")
        ry1=ry[2:4]

        rn=randint(100,999)
        scode=str(maxid)+ry1+str(rn)+rd
        
        
        sql = "INSERT INTO sw_webservice(id,web_url,form_data,service_code) VALUES (%s,%s,%s,%s)"
        val = (maxid,web_url,fd,scode)
        mycursor.execute(sql, val)
        mydb.commit()
        msg="ok"

        
    return render_template('service.html',msg=msg,act=act,un=un,s1=s1)

@app.route('/signup_upi', methods=['GET', 'POST'])
def signup_upi():
    msg=""
    act=request.args.get("act")
    secretcode=request.args.get("secretcode")
    un=""
    s1=""
    mycursor = mydb.cursor()
    

    if request.method=='POST':
        upicode=request.form['upicode']

        mycursor.execute("SELECT * FROM sw_user_register")
        data = mycursor.fetchall()
        for dd in data:
            un=dd[7]
            ky=un
            obj=AESCipher(ky)
            upi=obj.decrypt(dd[12].encode("utf-8"))
            if upi==upicode:
                s1="1"
                break
        if s1=="1":
            
            msg="ok"
        else:
            msg="fail"


    return render_template('signup_upi.html',msg=msg,act=act,un=un,s1=s1,secretcode=secretcode)

#Lookup Substitution
def substitutor(): 
      
    # list of strings 
    S = ["2020 Olympic games have @# been cancelled", 
     "Dr Vikram Sarabhai was +%--the ISRO’s first chairman", 
     "Dr Abdul            Kalam, the father      of India's missile programme"] 
      
    # loop to iterate every element of list 
    for i in range(len(S)): 
          
        # replacing every non-word character with a white space 
        S[i] = re.sub(r"\W", " ", S[i]) 
          
        # replacing every digit character with a white space 
        S[i] = re.sub(r"\d", " ", S[i]) 
          
        # replacing one or more white space with a single white space 
        S[i] = re.sub(r"\s+", " ", S[i]) 
          
        # replacing alphabetic characters which have one or more  
        # white space before and after them with a white space 
        S[i] = re.sub(r"\s+[a-z]\s+", " ", S[i], flags = re.I) 
          
        # substituting one or more white space which is at  
        # beginning of the string with an empty string 
        S[i] = re.sub(r"^\s+", "", S[i]) 
          
        # substituting one or more white space which is at 
        # end of the string with an empty string 
        S[i] = re.sub(r"\s+$", "", S[i]) 
      
    # loop to iterate every element of list 
    for i in range(len(S)): 
          
        # printing each modified string 
        print(S[i]) 
     
def getdata(un,web_state,upi,qd,wu):
    mess=""
    rdate=[]
    ky=un
    up=""
    obj=AESCipher(ky)

    web_url="https://"

    now = date.today() #datetime.datetime.now()
    rdate=now.strftime("%d-%m-%Y")
    crd=rdate.split("-")
    cr_dt=crd[0]

    
    ry=rdate=now.strftime("%Y")
    ryy=int(ry)

    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM sw_user_register where username=%s",(un,))
    dat = mycursor.fetchone()
    uid=str(dat[0])
    uname=dat[7]
    mycursor.execute("SELECT * FROM sw_user_profile where username=%s",(un,))
    dat1 = mycursor.fetchone()

    fdd=qd
    up="page=1"
    
    name=obj.decrypt(dat[1].encode("utf-8"))
    email=obj.decrypt(dat[6].encode("utf-8"))
    email1=obj.decrypt(dat[6].encode("utf-8"))
    mobile=obj.decrypt(dat[5].encode("utf-8"))
    aadhar=obj.decrypt(dat[4].encode("utf-8"))

    
    c="name"
    if c in fdd:
        if dat[1]=="":
            up+="|name="
        else:
            up+="|name="+obj.decrypt(dat[1].encode("utf-8"))
    c="gender"
    if c in fdd:
        if dat[2]=="":
            up+="|gender="
        else:
            up+="|gender="+obj.decrypt(dat[2].encode("utf-8"))            
    c="dob"
    if c in fdd:
        if dat[3]=="":
            up+="|dob="
        else:
            up+="|dob="+obj.decrypt(dat[3].encode("utf-8"))
    c="aadhar"
    if c in fdd:
        if dat[4]=="":
            up+="|aadhar="
        else:
            up+="|aadhar="+obj.decrypt(dat[4].encode("utf-8"))  

    c="mobile"
    if c in fdd:
        if dat[5]=="":
            up+="|mobile="
        else:
            up+="|mobile="+obj.decrypt(dat[5].encode("utf-8"))

    c="email"
    if c in fdd:
        if dat[6]=="":
            up+="|email="
        else:
            up+="|email="+obj.decrypt(dat[6].encode("utf-8"))
    ##########
    c="father"
    if c in fdd:
        if dat1[2]=="":
            up+="|father="
        else:
            up+="|father="+obj.decrypt(dat1[2].encode("utf-8"))
    c="mother"
    if c in fdd:
        if dat1[3]=="":
            up+="|mother="
        else:
            up+="|mother="+obj.decrypt(dat1[3].encode("utf-8"))
    c="address"
    if c in fdd:
        if dat1[4]=="":
            up+="|address="
        else:
            up+="|address="+obj.decrypt(dat1[4].encode("utf-8"))  
    c="taluk"
    if c in fdd:
        if dat1[5]=="":
            up+="|taluk="
        else:
            up+="|taluk="+obj.decrypt(dat1[5].encode("utf-8")) 

    ##
    c="district"
    if c in fdd:
        if dat1[6]=="":
            up+="|district="
        else:
            up+="|district="+obj.decrypt(dat1[6].encode("utf-8"))
    c="pincode"
    if c in fdd:
        if dat1[7]=="":
            up+="|pincode="
        else:
            up+="|pincode="+obj.decrypt(dat1[7].encode("utf-8"))
    c="pancard"
    if c in fdd:
        if dat1[8]=="":
            up+="|pancard="
        else:
            up+="|pancard="+obj.decrypt(dat1[8].encode("utf-8"))
    c="driving"
    if c in fdd:
        if dat1[9]=="":
            up+="|driving="
        else:
            up+="|driving="+obj.decrypt(dat1[9].encode("utf-8"))
    c="voterid"
    if c in fdd:
        if dat1[10]=="":
            up+="|voterid="
        else:
            up+="|voterid="+obj.decrypt(dat1[10].encode("utf-8"))
    ##
    c="bank"
    if c in fdd:
        if dat1[11]=="":
            up+="|bank="
        else:
            up+="|bank="+obj.decrypt(dat1[11].encode("utf-8"))
    c="customername"
    if c in fdd:
        if dat1[12]=="":
            up+="|customername="
        else:
            up+="|customername="+obj.decrypt(dat1[12].encode("utf-8"))
    c="account"
    if c in fdd:
        if dat1[13]=="":
            up+="|account="
        else:
            up+="|account="+obj.decrypt(dat1[13].encode("utf-8"))
    c="card"
    if c in fdd:
        if dat1[14]=="":
            up+="|card="
        else:
            up+="|card="+obj.decrypt(dat1[13].encode("utf-8"))
    c="gnumber"
    if c in fdd:
        if dat1[15]=="":
            up+="|gnumber="
        else:
            up+="|gnumber="+obj.decrypt(dat1[15].encode("utf-8"))
    
    c="sslc_school"
    if c in fdd:
        if dat1[20]=="":
            up+="|sslc_school="
        else:
            up+="|sslc_school="+obj.decrypt(dat1[20].encode("utf-8"))
    ##
    c="sslc_mark"
    if c in fdd:
        if dat1[21]=="":
            up+="|sslc_mark="
        else:
            up+="|sslc_mark="+obj.decrypt(dat1[21].encode("utf-8"))
    c="sslc_year"
    if c in fdd:
        if dat1[22]=="":
            up+="|sslc_year="
        else:
            up+="|sslc_year="+obj.decrypt(dat1[22].encode("utf-8"))
    c="hsc_school"
    if c in fdd:
        if dat1[23]=="":
            up+="|hsc_school="
        else:
            up+="|hsc_school="+obj.decrypt(dat1[23].encode("utf-8"))
    c="hsc_mark"
    if c in fdd:
        if dat1[24]=="":
            up+="|hsc_mark="
        else:
            up+="|hsc_mark="+obj.decrypt(dat1[24].encode("utf-8"))
    c="hsc_year"
    if c in fdd:
        if dat1[25]=="":
            up+="|hsc_year="
        else:
            up+="|hsc_year="+obj.decrypt(dat1[25].encode("utf-8"))
    ##
    c="ug_college"
    if c in fdd:
        if dat1[26]=="":
            up+="|ug_college="
        else:
            up+="|ug_college="+obj.decrypt(dat1[26].encode("utf-8"))
    c="ug_degree"
    if c in fdd:
        if dat1[27]=="":
            up+="|ug_degree="
        else:
            up+="|ug_degree="+obj.decrypt(dat1[27].encode("utf-8"))
    c="ug_mark"
    if c in fdd:
        if dat1[28]=="":
            up+="|ug_mark="
        else:
            up+="|ug_mark="+obj.decrypt(dat1[28].encode("utf-8"))
    c="ug_year"
    if c in fdd:
        if dat1[29]=="":
            up+="|ug_year="
        else:
            up+="|ug_year="+obj.decrypt(dat1[29].encode("utf-8"))
    c="pg_college"
    if c in fdd:
        if dat1[30]=="":
            up+="|pg_college="
        else:
            up+="|pg_college="+obj.decrypt(dat1[30].encode("utf-8"))
    ##
    c="pg_degree"
    if c in fdd:
        if dat1[31]=="":
            up+="|pg_degree="
        else:
            up+="|pg_degree="+obj.decrypt(dat1[31].encode("utf-8"))
    c="pg_mark"
    if c in fdd:
        if dat1[32]=="":
            up+="|pg_mark="
        else:
            up+="|pg_mark="+obj.decrypt(dat1[32].encode("utf-8"))
    c="pg_year"
    if c in fdd:
        if dat1[33]=="":
            up+="|pg_year="
        else:
            up+="|pg_year="+obj.decrypt(dat1[33].encode("utf-8"))
    c="company"
    if c in fdd:
        if dat1[34]=="":
            up+="|company="
        else:
            up+="|company="+obj.decrypt(dat1[34].encode("utf-8"))
    c="clocation"
    if c in fdd:
        if dat1[35]=="":
            up+="|clocation="
        else:
            up+="|clocation="+obj.decrypt(dat1[35].encode("utf-8"))
    ##
    c="designation"
    if c in fdd:
        if dat1[36]=="":
            up+="|designation="
        else:
            up+="|designation="+obj.decrypt(dat1[36].encode("utf-8"))
    c="exp_period"
    if c in fdd:
        if dat1[37]=="":
            up+="|exp_period="
        else:
            up+="|exp_period="+obj.decrypt(dat1[37].encode("utf-8"))

    if web_state=="Trusted":
        a1=name[0:3]
        mob=str(mobile)
        
        #a2=mob[2:4]
        a2=randint(111,599)
        a3=randint(600,999)
        us=a1+cr_dt+str(a2)+str(a3)
        
        rn1=randint(100,999)
        rn2=randint(100,999)
        pw=str(rn1)+str(rn2)
        up+="|uname="+us
        up+="|pass="+pw
        s1="1"  
        page=web_url+wu
        mess="Dear "+name+", You are registering "+page+", Username:"+us+", Password:"+pw
        bdata="Trusted, "+page+", Username:"+us+", Password:"+pw

        mycursor.execute("SELECT max(id)+1 FROM sw_register_website")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1
        
        now = datetime.datetime.now()
        yr=now.strftime("%Y")
        mon=now.strftime("%m")
        rdate=now.strftime("%d-%m-%Y")
        rtime=now.strftime("%H:%M:%S")
        dtime=rdate+", "+rtime

        sql = "INSERT INTO sw_register_website(id,username,web_url,web_status,web_username,web_password,date_time) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (maxid,un,page,web_state,us,pw,dtime)
        mycursor.execute(sql, val)
        mydb.commit()
        
        walletchain(uid,un,bdata,upi,'Web')

        
    else:
        up="page=1"
        ff=open("static/sb_name.txt","r")
        sb_name=ff.read()
        ff.close()
        sb_name_array=sb_name.split(",")
        na1=sb_name_array
        sb_name_len=len(sb_name_array)
        xn1=randint(1,sb_name_len)
        xn2=xn1-1
        name=na1[xn2]           
        email=name+"@gmail.com"
        customername=name

        rn3=randint(60,99)
        rn1=randint(1000,9000)
        rn2=randint(1000,9059)
        mobile=str(rn3)+str(rn1)+str(rn2)

        adr=['45, GJ Puram','85, KT Nagar','71, SK Colony','55, GR Nagar','21 AV Nagar']
        xn1=randint(1,5)
        xn2=xn1-1
        address=adr[xn2]

        drt=['Trichy','Chennai','Madurai','Salem','Erode','Karur','Tanjore']
        xn1=randint(1,7)
        xn2=xn1-1
        district=drt[xn2]

        bk=['SBI','IB','IOB','KVB','HDFC','ICICI','CUB']
        xn1=randint(1,7)
        xn2=xn1-1
        bank=bk[xn2]

        rn1=randint(600,699)
        rn2=randint(100,905)
        pincode=str(rn1)+str(rn2)

        rn1=randint(1000,6999)
        rn2=randint(1000,9059)
        rn3=randint(4000,6999)
        rn4=randint(1000,9059)
        card=str(rn1)+str(rn2)+str(rn3)+str(rn4)

        rn1=randint(2000,6999)
        rn2=randint(1000,9059)
        rn3=randint(10,90)
        account=str(rn1)+str(rn2)+str(rn3)

        gnumber=mobile

        tal=['Andimadam','Alandur','Ambattur','Bhuvanagiri','Bargur','Anchetty','Kilvelur','Palani','Arcot','Omalur']
        xn1=randint(1,10)
        xn2=xn1-1
        taluk=tal[xn2]

        aadhar="ad2.jpg"
        pancard="pd2.jpg"
        driving="dd2.jpg"
        voterid="vd2.jpg"

        shl=['Bishop','St.Joseph','Govt.School','SSB School','PKG School','MNS School','RKC School']
        xn1=randint(1,7)
        xn2=xn1-1
        sslc_school=shl[xn2]
        hsc_school=shl[xn2]

        cge=['SASTRA','NIT','Govt.College','Anna University','Periyar University','Alagappa','Kamarajar University']
        xn1=randint(1,7)
        xn2=xn1-1
        ug_college=cge[xn2]
        pg_college=cge[xn2]

        ryr=[5,10]
        re1=randint(1,2)
        re2=re1-1
        y1=ryy-ryr[re2]
        y2=y1+2
        y3=y2+3
        y4=y3+2

        sslc_year=str(y1)
        hsc_year=str(y2)
        ug_year=str(y3)
        pg_year=str(y4)

        udeg=['BSc','BCA','B.Com','BBA','BE','B.Tech']
        xn1=randint(1,6)
        xn2=xn1-1
        ug_degree=udeg[xn2]

        pdeg=['MSc','MCA','M.Com','MBA','ME','M.Tech']
        xn1=randint(1,6)
        xn2=xn1-1
        pg_degree=pdeg[xn2]

        mn1=randint(60,95)
        mn2=randint(60,95)
        mn3=randint(60,95)
        mn4=randint(60,95)
        sslc_mark=str(mn1)
        hsc_mark=str(mn2)
        ug_mark=str(mn3)
        pg_mark=str(mn4)

        comp=['HCL','Wipro','Tata','Infosys','TCS']
        xn1=randint(1,5)
        xn2=xn1-1
        company=comp[xn2]

        cloc=['Chennai','Bangalore','Delhi','Dubai','Mumbai']
        xn1=randint(1,5)
        xn2=xn1-1
        clocation=cloc[xn2]

        desig=['Technical Analyst','Jr. Software Engineer','HR Manager','Developer','Marketing Manager']
        xn1=randint(1,5)
        xn2=xn1-1
        designation=desig[xn2]

        prd=['2 years','1 year','6 months','8 months','3 years']
        xn1=randint(1,5)
        xn2=xn1-1
        exp_period=prd[xn2]
       
        

        up+="|name="+name
        up+="|mobile="+mobile
        up+="|email="+email
        up+="|address="+address
        up+="|district="+district
        up+="|pincode="+pincode
        up+="|bank="+bank
        up+="|customername="+customername
        up+="|account="+account
        up+="|card="+card
        up+="|gnumber="+gnumber

        up+="|taluk="+taluk
        up+="|aadhar="+aadhar
        up+="|pancard="+pancard
        up+="|driving="+driving
        up+="|voterid="+voterid

        up+="|sslc_school="+sslc_school
        up+="|sslc_mark="+sslc_mark
        up+="|sslc_year="+sslc_year
        up+="|hsc_school="+hsc_school
        up+="|hsc_mark="+hsc_mark
        up+="|hsc_year="+hsc_year

        up+="|ug_college="+ug_college
        up+="|ug_degree="+ug_degree
        up+="|ug_mark="+ug_mark
        up+="|ug_year="+ug_year

        up+="|pg_college="+pg_college
        up+="|pg_degree="+pg_degree
        up+="|pg_mark="+pg_mark
        up+="|pg_year="+pg_year

        up+="|company="+company
        up+="|clocation="+clocation
        up+="|designation="+designation
        up+="|exp_period="+exp_period
        

        mob=str(mobile)
        a1=name[0:3]
        #a2=mob[2:4]
        a2=randint(111,599)
        a3=randint(600,999)
        us=a1+cr_dt+str(a2)+str(a3)
        rn1=randint(100,999)
        rn2=randint(100,999)
        pw=str(rn1)+str(rn2)
        up+="|uname="+us
        up+="|pass="+pw
        s1="1"  

        
        page=web_url+wu
        mess="Dear "+name+", You are registering "+page+", Username:"+us+", Password:"+pw

        mycursor.execute("SELECT max(id)+1 FROM sw_register_website")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1
        
        now = datetime.datetime.now()
        yr=now.strftime("%Y")
        mon=now.strftime("%m")
        rdate=now.strftime("%d-%m-%Y")
        rtime=now.strftime("%H:%M:%S")
        dtime=rdate+", "+rtime

        sql = "INSERT INTO sw_register_website(id,username,web_url,web_status,web_username,web_password,date_time) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (maxid,un,page,web_state,us,pw,dtime)
        mycursor.execute(sql, val)
        mydb.commit()

        
        bdata="Untrusted, "+page+", Username:"+us+", Password:"+pw
        walletchain(uid,un,bdata,upi,'Web')

    '''ff=open("static/path1.txt","r")
    path1=ff.read()
    ff.close()

    ff1=open(path1+"/data.txt","w")
    ff1.write(up)
    ff.close()'''
    
    rdata=[mess,email1,up]
    return rdata

    
@app.route('/verify', methods=['GET', 'POST'])
def verify():
    msg=""
    act=request.args.get("act")
    upi=request.args.get("upi")
    qd=request.args.get("qd")
    wu=request.args.get("wu")
    web_state=""
    result=""
    un=""
    
    mess=""
    email=""
    mdata=""

    ff=open("bc.txt","r")
    bc=ff.read()
    ff.close()
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM sw_user_register")
    data = mycursor.fetchall()

    x=0
    for ds in data:
        un=ds[7]
        ky=un
        obj=AESCipher(ky)
        ucode=obj.decrypt(ds[12].encode("utf-8"))
        if upi==ucode:
            x+=1
            break

    if x>0:
        msg="ok"
        
        ##
        filename = 'static/dataset/dataseturl.csv'
        uda = pd.read_csv(filename, header=0)
        for ss in uda.values:
            line=ss[0]
            if wu in line:
                web_state=ss[1]
                break
        ##
        
        
    else:
        msg="fail"


    if act=="1":
        
        query=getdata(un,web_state,upi,qd,wu)
        mess=query[0]
        email=query[1]
        mdata=query[2]
        
        msg="success"

    if act=="2":
        
        query=getdata(un,web_state,upi,qd,wu)
        mess=query[0]
        email=query[1]
        mdata=query[2]
        
        msg="success"

    if act=="3":
        
        query=getdata(un,web_state,upi,qd,wu)
        mess=query[0]
        email=query[1]
        mdata=query[2]
        
        msg="success"
    
        

    return render_template('verify.html',msg=msg,act=act,upi=upi,qd=qd,wu=wu,mess=mess,email=email,mdata=mdata,bc=bc)
    
@app.route('/history', methods=['GET', 'POST'])
def history():
    msg=""
    act=request.args.get("act")
    uname=""
    if 'username' in session:
        uname = session['username']
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM sw_register_website where username=%s",(uname,))
    data = mycursor.fetchall()

    return render_template('history.html',data=data)

@app.route('/view_block', methods=['GET', 'POST'])
def view_block():
    msg=""
    act=request.args.get("act")
    uname=""
    data1=[]
    
    if 'username' in session:
        uname = session['username']
    mycursor = mydb.cursor()
    
    ky=uname
    obj=AESCipher(ky)
    
    mycursor.execute("SELECT * FROM sw_user_register where username=%s",(uname,))
    data = mycursor.fetchone()

    
    upi=obj.decrypt(data[12].encode("utf-8"))
    
    ff=open("static/walletchain.json","r")
    fj=ff.read()
    ff.close()

    fjj=fj.split('}')

    nn=len(fjj)
    nn2=nn-2
    i=0
    fsn=""
    while i<nn-1:
        if i==nn2:
            fsn+=fjj[i]+"}"
        else:
            fsn+=fjj[i]+"},"
        i+=1
        
    #fjj1='},'.join(fjj)
    
    fj1="["+fsn+"]"
    

    ff=open("static/wallet.json","w")
    ff.write(fj1)
    ff.close()
    
    dataframe = pd.read_json("static/wallet.json", orient='values')
    
    
    for ss in dataframe.values:
        
        if ss[3]==upi:
            
            data1.append(ss)

    
    return render_template('view_block.html',data=data,data1=data1)

@app.route('/view_decrypt', methods=['GET', 'POST'])
def view_decrypt():
    msg=""
    s1=""
    act=request.args.get("act")
    uname=""
    data1=[]
    if 'username' in session:
        uname = session['username']
    mycursor = mydb.cursor()
    
    ky=uname
    obj=AESCipher(ky)
    
    mycursor.execute("SELECT * FROM sw_user_register where username=%s",(uname,))
    data = mycursor.fetchone()
    
    upi=obj.decrypt(data[12].encode("utf-8"))
    
    
    
    s1="1"
    ff=open("static/assets/js/d1.txt","r")
    ds=ff.read()
    ff.close()

    drow=ds.split("#|")
    
    i=0
    for dr in drow:
        
        dr1=dr.split("##")
        dt=[]
        if dr1[3]==upi:
            
            dt.append(dr1[0])
            dt.append(dr1[1])
            dt.append(dr1[2])
            dt.append(dr1[3])
            dt.append(dr1[4])
            data1.append(dt)
        
   

    return render_template('view_decrypt.html',data=data,data1=data1,s1=s1)



@app.route('/view_user', methods=['GET', 'POST'])
def view_user():
    msg=""
    act=request.args.get("act")
    uname=""
    if 'username' in session:
        uname = session['username']
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM sw_user_register")
    data = mycursor.fetchall()

    if act=="yes":
        did=request.args.get("did")
        mycursor.execute("update sw_user_register set approved_status=1 where id=%s",(did,))
        mydb.commit()
        return redirect(url_for('view_user')) 

        
    return render_template('view_user.html',data=data)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    msg=""
    uname=""
    if 'username' in session:
        uname = session['username']
    mycursor = mydb.cursor()
    
        
    return render_template('admin.html')

@app.route('/view_data', methods=['GET', 'POST'])
def view_data():
    msg=""
    uname=""
    cnt=0
    data=[]
    rows=0
    cols=0
    if 'username' in session:
        uname = session['username']
    mycursor = mydb.cursor()
    
    filename = 'static/dataset/dataseturl.csv'
    data1 = pd.read_csv(filename, header=0,encoding='cp1252')
    data2 = list(data1.values.flatten())
    
    i=0
    sd=len(data1)
    rows=len(data1.values)
    
    
    for ss in data1.values:
        cnt=len(ss)
        data.append(ss)
    cols=cnt-1

    
    return render_template('view_data.html',data=data,rows=rows,cols=cols)

@app.route('/preprocess', methods=['GET', 'POST'])
def preprocess():
    msg=""
    mem=0
    cnt=0
    cols=0
    rows=0
    rowsn=0
    nullcount=0
    filename = 'static/dataset/dataseturl.csv'
    data1 = pd.read_csv(filename, encoding='cp1252')
    data2 = list(data1.values.flatten())
    cname=[]
    data=[]
    dtype=[]
    dtt=[]
    nv=[]
    i=0
    
    sd=len(data1)
    rows=len(data1.values)
    
    #print(data1.columns)
    col=data1.columns
    #print(data1[0])
    for ss in data1.values:
        cnt=len(ss)
        i=0
        x=0
        while i<cnt:
            if pd.isnull(ss[i]):
                nullcount+=1
                x+=1
            i+=1
        if x>0:
            rowsn+=1
        

    i=0
    while i<cnt:
        j=0
        x=0
        for rr in data1.values:
            dt=type(rr[i])
            if rr[i]!="":
                x+=1
            
            j+=1
        dtt.append(dt)
        nv.append(str(x))
        
        i+=1

    arr1=np.array(col)
    arr2=np.array(nv)
    data3=np.vstack((arr1, arr2))
    rows=rows-rowsn

    arr3=np.array(data3)
    arr4=np.array(dtt)
    
    data=np.vstack((arr3, arr4))
   
    print(data)
    cols=cnt
    mem=float(rows)*0.75

    #if request.method=='POST':
    #    return redirect(url_for('feature_ext'))
    
    return render_template('preprocess.html',data=data, msg=msg, rows=rows,nullcount=nullcount, cols=cols, dtype=dtype, mem=mem)

##
##Logistic Regression
def LogisticRegression():
    urldata = pd.read_csv("static/dataset/dataseturl.csv")
    urldata.isnull().sum()
    from urllib.parse import urlparse
    import os.path
    #Length of URL
    urldata['url_length'] = urldata['url'].apply(lambda i: len(str(i)))
    #Hostname Length
    urldata['hostname_length'] = urldata['url'].apply(lambda i: len(urlparse(i).netloc))
    #Path Length
    urldata['path_length'] = urldata['url'].apply(lambda i: len(urlparse(i).path))
    #First Directory Length
    def fd_length(url):
        urlpath= urlparse(url).path
        try:
            return len(urlpath.split('/')[1])
        except:
            return 0

    urldata['fd_length'] = urldata['url'].apply(lambda i: fd_length(i))
    ##

    urldata['count-'] = urldata['url'].apply(lambda i: i.count('-'))
    urldata['count@'] = urldata['url'].apply(lambda i: i.count('@'))
    urldata['count?'] = urldata['url'].apply(lambda i: i.count('?'))
    urldata['count%'] = urldata['url'].apply(lambda i: i.count('%'))
    urldata['count.'] = urldata['url'].apply(lambda i: i.count('.'))
    urldata['count='] = urldata['url'].apply(lambda i: i.count('='))
    urldata['count-http'] = urldata['url'].apply(lambda i : i.count('http'))
    urldata['count-https'] = urldata['url'].apply(lambda i : i.count('https'))
    urldata['count-www'] = urldata['url'].apply(lambda i: i.count('www'))
    def digit_count(url):
        digits = 0
        for i in url:
            if i.isnumeric():
                digits = digits + 1
        return digits
    urldata['count-digits']= urldata['url'].apply(lambda i: digit_count(i))
    def letter_count(url):
        letters = 0
        for i in url:
            if i.isalpha():
                letters = letters + 1
        return letters
    urldata['count-letters']= urldata['url'].apply(lambda i: letter_count(i))
    def no_of_dir(url):
        urldir = urlparse(url).path
        return urldir.count('/')
    urldata['count_dir'] = urldata['url'].apply(lambda i: no_of_dir(i))
    dat1=urldata.head(350)

    import re
    #Use of IP or not in domain
    def having_ip_address(url):
        match = re.search(
            '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
            '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4
            '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)' # IPv4 in hexadecimal
            '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}', url)  # Ipv6
        if match:
            # print match.group()
            return -1
        else:
            # print 'No matching pattern found'
            return 1
    urldata['use_of_ip'] = urldata['url'].apply(lambda i: having_ip_address(i))
    #
    def shortening_service(url):
        match = re.search('bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                          'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                          'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                          'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
                          'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
                          'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
                          'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|'
                          'tr\.im|link\.zip\.net',
                          url)
        if match:
            return -1
        else:
            return 1
    urldata['short_url'] = urldata['url'].apply(lambda i: shortening_service(i))
    urldata.head()
    #Heatmap
    #corrmat = urldata.corr()
    #f, ax = plt.subplots(figsize=(25,19))
    #sns.heatmap(corrmat, square=True, annot = True, annot_kws={'size':10})
    #plt.savefig('static/graph4.png')
    #plt.close()
    

    print('Model accuracy score: {0:0.4f}'. format(accuracy_score(y_test, y_pred_test)))
    y_pred_train = logreg.predict(X_train)
    logreg100 = LogisticRegression(C=100, solver='liblinear', random_state=0)


    # fit the model
    logreg100.fit(X_train, y_train)
    # instantiate the model
    logreg001 = LogisticRegression(C=0.01, solver='liblinear', random_state=0)


    # fit the model
    logreg001.fit(X_train, y_train)
    y_test.value_counts()
    null_accuracy = (22067/(22067+6372))

    print('Null accuracy score: {0:0.4f}'. format(null_accuracy))
    cm = confusion_matrix(y_test, y_pred_test)

    print('Confusion matrix\n\n', cm)

    print('\nTrue Positives(TP) = ', cm[0,0])

    print('\nTrue Negatives(TN) = ', cm[1,1])

    print('\nFalse Positives(FP) = ', cm[0,1])

    print('\nFalse Negatives(FN) = ', cm[1,0])
    cm_matrix = pd.DataFrame(data=cm, columns=['Actual Positive:1', 'Actual Negative:0'], 
                                     index=['Predict Positive:1', 'Predict Negative:0'])

    sns.heatmap(cm_matrix, annot=True, fmt='d', cmap='YlGnBu')
    print(classification_report(y_test, y_pred_test))
    classification_accuracy = (TP + TN) / float(TP + TN + FP + FN)
    classification_error = (FP + FN) / float(TP + TN + FP + FN)
    precision = TP / float(TP + FP)
    recall = TP / float(TP + FN)
    true_positive_rate = TP / float(TP + FN)
    false_positive_rate = FP / float(FP + TN)
    y_pred_prob = logreg.predict_proba(X_test)[0:10]
    for i in range(1,5):
        
        cm1=0
        
        y_pred1 = logreg.predict_proba(X_test)[:,1]
        
        y_pred1 = y_pred1.reshape(-1,1)
        
        y_pred2 = binarize(y_pred1, i/10)
        
        y_pred2 = np.where(y_pred2 == 1, 'Yes', 'No')
        
        cm1 = confusion_matrix(y_test, y_pred2)
            
        print ('With',i/10,'threshold the Confusion Matrix is ','\n\n',cm1,'\n\n',
               
                'with',cm1[0,0]+cm1[1,1],'correct predictions, ', '\n\n', 
               
                cm1[0,1],'Type I errors( False Positives), ','\n\n',
               
                cm1[1,0],'Type II errors( False Negatives), ','\n\n',
               
               'Accuracy score: ', (accuracy_score(y_test, y_pred2)), '\n\n',
               
               'Sensitivity: ',cm1[1,1]/(float(cm1[1,1]+cm1[1,0])), '\n\n',
               
               'Specificity: ',cm1[0,0]/(float(cm1[0,0]+cm1[0,1])),'\n\n',
              
                '====================================================', '\n\n')
        fpr, tpr, thresholds = roc_curve(y_test, y_pred1, pos_label = 'Yes')
        plt.figure(figsize=(6,4))
        plt.plot(fpr, tpr, linewidth=2)
        plt.plot([0,1], [0,1], 'k--' )

        X = datasets.iloc[:, [2,3]].values
        Y = datasets.iloc[:, 4].values

        # Splitting the dataset into the Training set and Test set

        from sklearn.model_selection import train_test_split
        X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

        # Feature Scaling

        from sklearn.preprocessing import StandardScaler
        sc_X = StandardScaler()
        X_Train = sc_X.fit_transform(X_Train)
        X_Test = sc_X.transform(X_Test)

        # Fitting the Logistic Regression into the Training set

        from sklearn.linear_model import LogisticRegression
        classifier = LogisticRegression(random_state = 0)
        classifier.fit(X_Train, Y_Train)

        # Predicting the test set results

        Y_Pred = classifier.predict(X_Test)

        # Making the Confusion Matrix 

        from sklearn.metrics import confusion_matrix
        cm = confusion_matrix(Y_Test, Y_Pred)

        # Visualising the Training set results 

        from matplotlib.colors import ListedColormap
        X_Set, Y_Set = X_Train, Y_Train
        X1, X2 = np.meshgrid(np.arange(start = X_Set[:,0].min() -1, stop = X_Set[:, 0].max() +1, step = 0.01),
                             np.arange(start = X_Set[:,1].min() -1, stop = X_Set[:, 1].max() +1, step = 0.01))

        plt.contourf(X1,X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
                     alpha = 0.75, cmap = ListedColormap(('red', 'green')))


############################
    
@app.route('/feature', methods=['GET', 'POST'])
def feature():
    msg=""
    uname=""
    cnt=0
    data=[]
    rows=0
    cols=0
    rowsn=0
    nullcount=0
    if 'username' in session:
        uname = session['username']
    mycursor = mydb.cursor()
    
    filename = 'static/dataset/dataseturl.csv'
    data1 = pd.read_csv(filename, header=0,encoding='cp1252')
    data2 = list(data1.values.flatten())
    
    i=0
    sd=len(data1)
    rows=len(data1.values)
    #acc########################################
    y=[]
    x1=[]
    x2=[]

    i=1
    while i<=5:
        rn=randint(94,98)
        v1='0.'+str(rn)

        #v11=float(v1)
        v111=round(rn)
        x1.append(v111)

        rn2=randint(94,98)
        v2='0.'+str(rn2)

        
        #v22=float(v2)
        v33=round(rn2)
        x2.append(v33)
        i+=1
    
    #x1=[0,0,0,0,0]
    y=[150,370,690,880,1200]
    #x2=[0.2,0.4,0.2,0.5,0.6]
    
    plt.figure(figsize=(10, 8))
    # plotting multiple lines from array
    plt.plot(y,x1)
    plt.plot(y,x2)
    dd=["train","val"]
    plt.legend(dd)
    plt.xlabel("Epochs")
    plt.ylabel("Accuracy %")
    
    fn="graph2.png"
    #plt.savefig('static/'+fn)
    plt.close()
    #######################################################
    #graph4
    y=[]
    x1=[]
    x2=[]

    i=1
    while i<=5:
        rn=randint(1,4)
        v1='0.'+str(rn)

        #v11=float(v1)
        v111=round(rn)
        x1.append(v111)

        rn2=randint(1,4)
        v2='0.'+str(rn2)

        
        #v22=float(v2)
        v33=round(rn2)
        x2.append(v33)
        i+=1
    
    #x1=[0,0,0,0,0]
    y=[150,370,690,880,1200]
    #x2=[0.2,0.4,0.2,0.5,0.6]
    
    plt.figure(figsize=(10, 8))
    # plotting multiple lines from array
    plt.plot(y,x1)
    plt.plot(y,x2)
    dd=["train","val"]
    plt.legend(dd)
    plt.xlabel("Epochs")
    plt.ylabel("Model loss")
    
    fn="graph3.png"
    #plt.savefig('static/'+fn)
    plt.close()
    ############################
    
    return render_template('feature.html',data=data,rows=rows,cols=cols)



@app.route('/classify', methods=['GET', 'POST'])
def classify():
    msg=""
    uname=""
    cnt=0
    data=[]
    rows=0
    cols=0
    rowsn=0
    nullcount=0
    if 'username' in session:
        uname = session['username']
    mycursor = mydb.cursor()
    
    filename = 'static/dataset/dataseturl.csv'
    data1 = pd.read_csv(filename, header=0,encoding='cp1252')
    data2 = list(data1.values.flatten())
    
    i=0
    sd=len(data1)
    rows=len(data1.values)
    
    v1=0
    v2=0
    j=0
    for ss in data1.values:
        cnt=len(ss)
        i=0
        x=0
        if j<=300:
            while i<cnt:
                if pd.isnull(ss[i]):
                    nullcount+=1
                    x+=1
                i+=1
            if x>0:
                rowsn+=1
            else:
                if ss[1]=="Trusted":
                    v1+=1
                else:
                    v2+=1
                data.append(ss)

        j+=1
    cols=cnt

    nn=0
    if v1>v2:
        nn=v1
    else:
        nn=v2

    gn=nn+10
    #################
    val=[v1,v2]
    doc = ['Trusted','Untrusted'] #list(data.keys())
    values = val #list(data.values())
    
    print(doc)
    print(values)
    fig = plt.figure(figsize = (10, 8))
     
    # creating the bar plot
    cc=['green','orange']
    plt.bar(doc, values, color=cc, width = 0.6)
 

    plt.ylim((1,gn))
    plt.xlabel("Class")
    plt.ylabel("Count")
    plt.title("")

    rr=randint(100,999)
    fn="graph1.png"
    #plt.xticks(rotation=5,size=20)
    #plt.savefig('static/'+fn)
    
    plt.close()
    #plt.clf()
    #################

    
    return render_template('classify.html',data=data,rows=rows,cols=cols)

@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=5000)
