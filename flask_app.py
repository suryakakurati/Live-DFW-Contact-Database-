from flask import Flask, render_template, request, flash, session
from csv import writer
import csv
import pandas as pd
app = Flask(__name__)
app.secret_key = 'super secret key'



Servlist = []
with open('mysite/Services.csv', mode ='r')as file:
      csvFile = csv.reader(file)
      for x in csvFile:
         Servlist.append(x[0])
Servlist2 = sorted(Servlist)
dundun = 0
with open('mysite/People.csv', mode ='r')as file:
      csvFile = csv.reader(file)
      dundun = 0
      for x in csvFile:
         dundun += 1



@app.route('/')
def home():
   global Servlist
   global Servlist2
   global dundun
   with open('mysite/People.csv', mode ='r')as file:
      csvFile = csv.reader(file)
      dundun = 0
      for x in csvFile:
         dundun += 1
   return render_template('Search.html', services= Servlist2, people = dundun, error='no')








@app.route('/profile', methods=['POST'])
def profile():
      name = request.form['name']
      phone = request.form['phone']

      print(name, phone)
   #  df = pd.read_csv("People.csv", header=0)
   #  df = df.loc[df['Name'].str.contains(name, case=False)]
   #  df = df.loc[df['Phone'].str.contains(phone, case=False)]
   #  lol = list[df.values]
   #  io = lol[1]
      io = []
      f = []
      with open('mysite/People.csv', 'r') as file:
         csv_reader = csv.reader(file)
         for row in csv_reader:
            io.append(row)
      # Render "Profile.html" with the data
      for i in io:


         if (i[0].strip() == name.strip()) and (i[2].strip() == phone.strip()) :
            f = i


      return render_template('Profile.html', value = f )














@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      x = request.form.get('Service')
      y = (request.form.get('Name').lstrip()).rstrip()


      if request.form.get('submit_button') == 'ServSearch':
         if x == x:
            pass
            df = pd.read_csv("mysite/People.csv", header=0)
            df = df.loc[df['Service'].str.contains(x, case=False)]
            Listed = list(df.values)
            if len(df)> 0:
               return render_template("results.html", listed = Listed, error='no')
            else:
               flash('No Service Contacts found for the given criteria!')
               with open('mysite/People.csv', mode ='r')as file:
                  csvFile = csv.reader(file)
                  dundun = 0
                  for x in csvFile:
                     dundun += 1
               return render_template('Search.html', services= Servlist2, error='yes')
      elif request.form.get('submit_button') == 'NameSearch':
         if y == y:
            pass
            df = pd.read_csv("mysite/People.csv", header=0)
            df = df.loc[df['Name'].str.contains(y, case=False)]
            Listed = list(df.values)
            if len(df)> 0:
                return render_template("results.html", listed = Listed, error='no')
            else:
                flash('No Service Contacts found for the given criteria!')
                with open('mysite/People.csv', mode ='r')as file:
                  csvFile = csv.reader(file)
                  dundun = 0
                  for x in csvFile:
                     dundun += 1
                return render_template('Search.html', services= Servlist2, error='yes')
      elif request.form.get('submit_button') == 'AddCont':
            pass
            return render_template('Add.html', services= Servlist2, error='no')

@app.route('/add',methods = ['POST', 'GET'])
def Add():
   a = (request.form.get('CName').lstrip()).rstrip()
   b = (request.form.get('tel1').lstrip()).rstrip()
   b2 = (request.form.get('tel2').lstrip()).rstrip()
   b3 = (request.form.get('tel3').lstrip()).rstrip()
   btotal = str(b) + '-' + str(b2) + '-' + str(b3)
   c = (request.form.get('CService').lstrip()).rstrip()
   e = (request.form.get('CComments').lstrip()).rstrip()
   x = (request.form.get('CEmail').lstrip()).rstrip()
   y = (request.form.get('CWeb').lstrip()).rstrip()
   z = (request.form.get('CRating').lstrip()).rstrip()
   uw = (request.form.get('Rec').lstrip()).rstrip()
   if request.method == 'POST':
      if request.form.get('submit_button') == 'AddContra':
         if e == '':
            e = '-'
         if x == '':
            x = '-'
         if y == '':
            y = '-'
         if uw == '':
             uw = '-'

         if (a != '' and b != ''and b2 != ''and b3 != '' and c != ''and z != ''):
            list_data =[a, c, btotal, e, x, y, z, uw]
            with open('mysite/People.csv', 'a+', newline='') as f_object:
               writer_object = writer(f_object)
               writer_object.writerow(list_data)
               f_object.close()
               flash('New Service Contact added!')
               return render_template('Search.html', services= Servlist2, error='no')
         else:
            flash('Please fill in all the required fields (marked with \'*\')')
            return render_template('Add.html', services= Servlist2, error='yes')
      elif request.form.get('submit_button') == 'Back':
         return render_template('Search.html', services= Servlist2, error='no')




app.config['ADMIN_PASSWORD'] = 'admin'






if __name__ == '__main__':
   app.run(debug = True)



