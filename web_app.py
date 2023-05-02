from flask import Flask, render_template, request
import pandas as pd
from CVD_model import *

app = Flask(__name__)

# Load the student scores dataset
data = pd.read_csv('exams.csv')

# create dropdown menus for each form field
gender_options = ["Male", "Female"]
race_options = ["Group A", "Group B", "Group C", "Group D", "Group E"]
education_options = ["Some High School", "High School", "Some College", "Associate's Degree", "Bachelor's Degree", "Master's Degree"]
lunch_options = ["Standard", "Free/Reduced"]

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        gender = request.form['gender']
        if (gender == "Male"):
            gender = 1
        else:
            gender = 0
        race = request.form['race']
        education = request.form['education']
        lunch = request.form['lunch']
        math_score = int(request.form['math_score'])
        if math_score>=50:
            math_pred = "You have higher chance of passing the exam"
        elif math_score<=50:
            math_pred = "You have higher chance of failing the exam"
        reading_score = int(request.form['reading_score'])
        if reading_score>=50:
            reading_pred = "You have higher chance of passing the exam"
        elif reading_score<=50:
            reading_pred = "You have higher chance of failing the exam"
        writing_score = int(request.form['writing_score'])
        if writing_score>=50:
            writing_pred = "You have higher chance of passing the exam"
        elif writing_score<=50:
            writing_pred = "You have higher chance of failing the exam"

        return render_template('index.html',
                               math_pred=math_pred,
                               reading_pred=reading_pred,
                               writing_pred=writing_pred)
    else:
        return render_template('index.html',
                               gender_options=gender_options,
                               race_options=race_options,
                               education_options=education_options,
                               lunch_options=lunch_options)

if __name__ == '__main__':
    app.run(debug=True)

    # arg parser for the standard anaconda-project options
    parser = ArgumentParser(prog="home",
                            description="Simple Flask Application")
    parser.add_argument('--anaconda-project-host', action='append', default=[],
                        help='Hostname to allow in requests')
    parser.add_argument('--anaconda-project-port', action='store', default=8086, type=int,
                        help='Port to listen on')
    parser.add_argument('--anaconda-project-iframe-hosts',
                        action='append',
                        help='Space-separated hosts which can embed us in an iframe per our Content-Security-Policy')
    parser.add_argument('--anaconda-project-no-browser', action='store_true',
                        default=False,
                        help='Disable opening in a browser')
    parser.add_argument('--anaconda-project-use-xheaders',
                        action='store_true',
                        default=False,
                        help='Trust X-headers from reverse proxy')
    parser.add_argument('--anaconda-project-url-prefix', action='store', default='',
                        help='Prefix in front of urls')
    parser.add_argument('--anaconda-project-address',
                        action='store',
                        #default='0.0.0.0',
                        help='IP address the application should listen on.')

    args = parser.parse_args()

    app = Flask(__name__)
    app.register_blueprint(appweb, url_prefix = args.anaconda_project_url_prefix)

    app.config['PREFERRED_URL_SCHEME'] = 'https'

    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(host=args.anaconda_project_address, port=args.anaconda_project_port)




