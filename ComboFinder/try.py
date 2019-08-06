from werkzeug.utils import secure_filename
from flask import Flask, flash, request, redirect, render_template
import urllib.request
from django.conf import settings
import os
from flask import Flask
import random

UPLOAD_FOLDER = 'D:/wrkshp/Combo finder/templates python'
app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])



@app.route('/')
def try1():
    return render_template('try1.html')


@app.route('/try2', methods=['POST'])
def try2():

    if request.method == 'POST':
        first = request.form['first']
        last = request.form['last']
        file = request.files['file_name']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        file_name1=file.filename
    readfp=open(str(file_name1))
    mydict=dict()
    setlb=3
    setub=6
    resultlist=set()
    iterations = 1000
    result = set()
    sum=0
    for line in readfp:
        l=line.split(',')
        l[1]=l[1].strip()
        mydict[l[0]]=int(l[1])
    for i in range(iterations): 
        sum=0
        setsize=random.randint(setlb,setub)
        c=tuple(random.sample(list(mydict.keys()),setsize))
        for j in c:
            sum=sum+mydict[j]
        if sum>=int(first) and sum<=int(last) :
            resultlist.add(c)
        for r in resultlist:
            r=list(r)
            r.sort()
            r=tuple(r)
            result.add(r)
    readfp.close()
    return render_template('try2.html',first=path,last=last,result=result)
if __name__ == '__main__':
    app.run(debug=True)
