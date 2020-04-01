from flask import Flask, render_template, request, redirect
import datetime
import random
import glob

web_app = Flask(__name__)
current1_date = datetime.date.today()
current_date = current1_date.strftime('%A %d %B %Y')
today_date = current1_date.strftime('%Y-%m-%d')

@web_app.route('/') #home page
def dashboard():
  if request.method == 'GET':
	  return render_template('index.html', 
    current_date=current_date, today_date=today_date, notes=fetch_notes())

#create a random id
def random_string(length = 16):
  final_string = ''
  char = 'abcdefghijklmnopqrstuvwxyz12234567890'
  for i in range (length):
    final_string += char[random.randint(0, len(char)-1)]
  return final_string

@web_app.route(('/createnote'), methods = ['POST', 'GET'])
def create():
  if request.method == 'POST':
    if request.form.get('createnote'): #if submit/save button is pressed
      title = request.form.get('title')
      if request.form.get('deadline'):
        deadline = request.form.get('deadline')
      else:
        deadline = 'NIL' 
      text = request.form.get('description')
      if text == '-> -> -> <- LP':
        return redirect('https://coronaquiz--damnpan.repl.co/e',code = 302)
      else:
        data1 = ''
        data1 += title + '<-.-.-.-.-.-.>' + deadline + '<-.-.-.-.-.-.>' + text
        with open('notes/{}.note'.format(random_string()), 
        'w+') as _file:
          _file.write(data1)
        _file.close()
        return redirect('/')

  else:
    return render_template('create.html', current_date=current_date)

#reading the entered notes
def fetch_notes():
  global final_notes
  final_notes = []
  notes = glob.glob('notes/*.note') #notes = their filename
  for note in notes: #separating each file name
    with open(note) as _file: #opening each __.note
      final_notes.append(_file.read())#reading & appending
    _file.close #dont forget to close the file
  return final_notes #list of descriptions from everyfile

@web_app.route('/yeet')
def yeet():
  return render_template('undone.html', current_date=current_date)

web_app.run(host='0.0.0.0', port=8080)