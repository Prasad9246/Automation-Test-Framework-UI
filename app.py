import subprocess
import os
from flask import Flask, render_template, jsonify, request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

LOG_FOLDER = "C:/Users/Prasad Kamble/OneDrive - chiacon.com/Documents/web selenium interface/version6/logs"

def run_pytest_framework(test_type):
    try:
        if test_type == "login":
            subprocess.run(["pytest", "testcases/T1_Login_Pg_Test.py"], check=True, shell=True)
        elif test_type == "product":
            subprocess.run(["pytest", "testcases/T2_Product_Pg_Test.py"], check=True, shell=True)
        elif test_type == "cart":
            subprocess.run(["pytest", "testcases/T3_YourCart_Pg_Test.py"], check=True, shell=True)
        elif test_type == "info":
            subprocess.run(["pytest", "testcases/T4_Info_Pg_Test.py"], check=True, shell=True)
        elif test_type == "overview":
            subprocess.run(["pytest", "testcases/T5_CkOverview_Pg_Test.py"], check=True, shell=True)
        elif test_type == "allure":
            subprocess.run(["pytest", "--alluredir=allure-results"], check=True, shell=True)
            subprocess.run(["allure", "generate", "allure-results", "-o", "allure-report"], check=True, shell=True)
        else:
            subprocess.run(["pytest"], check=True, shell=True)
        return jsonify({'success': True, 'message': 'Pytest framework executed successfully.'})
    except subprocess.CalledProcessError as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run_pytest', methods=['GET'])
def run_pytest():
    test_type = request.args.get('type', 'all')
    return run_pytest_framework(test_type)


@app.route('/start_allure', methods=['GET'])
def start_allure():
    try:
        subprocess.Popen(["allure", "serve", "allure-results"], shell=True)
        return jsonify({'success': True, 'message': 'Allure server started successfully.'})
    except subprocess.CalledProcessError as e:
        return jsonify({'success': False, 'message': str(e)})

@app.route('/logs', methods=['GET'])
def list_log_files():
    log_files = [f for f in os.listdir(LOG_FOLDER) if f.endswith('.log')]
    return jsonify(log_files)

@app.route('/logs/<filename>', methods=['GET'])
def get_log_file(filename):
    return send_from_directory(LOG_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)
