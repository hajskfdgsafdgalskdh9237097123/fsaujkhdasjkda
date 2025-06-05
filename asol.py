from flask import Flask,request,render_template
import subprocess

subprocess.run(['unzip','rclone.zip'])

def save_file_to_gd(file_name):
    command = f'./rclone copy uploads/{file_name} aab:'
    subprocess.run(command.split(' '))
    command = f'./rclone link aab:{file_name}'
    res = subprocess.run(command.split(' '),capture_output=True,text=True)
    return res.stdout.strip()



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('a.html')


@app.route('/sub',methods=["POST"])
def up():
    
    
    file = request.files['ff']
    file.save('./uploads/'+file.filename)
    

    link = save_file_to_gd(file.filename)
    return link

app.run(host='0.0.0.0')
