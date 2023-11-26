from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
# from .models import Employee
from . import db
import json
from datetime import date
from .models import Note

from . import mydb
mycursor = mydb.cursor()

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    emp_list = []
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        # new_employee = Employee(email=email, first_name=first_name)
        # db.session.add(new_employee)
        mycursor.execute('SELECT max(id) from employee')
        userID = 0
        for i in mycursor:
            if i[0]==None:
                pass
            else:
                userID = i[0]+1
        mycursor.execute(f'INSERT INTO  employee(Id,Fname) VALUES ({userID},"{first_name}")')
        mycursor.execute(f'INSERT INTO  employee_email(Id,Email) VALUES ({userID},"{email}")')
        mycursor.execute(f'SELECT e.Fname , ee.Email from employee e ,employee_email ee')
        
        for i in mycursor:
            print(i)
        mydb.commit()
        # db.session.commit()
        flash('New employee Added!', category='success')
        
        mycursor.execute("SELECT e.id,fname,email FROM employee as e,employee_email as ee WHERE e.id=ee.id")
        for i in mycursor:
            emp_list.append((i[0],i[1],i[2]))
        #print("Employee: ",Employee)
        print(emp_list)
    return render_template("home.html",user=current_user,emp_list=emp_list)

@views.route('/feedback', methods=['GET', 'POST'])
@login_required
def feedback():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    today = date.today()
    return render_template("feedback.html", user=current_user,date=today)



