from flask import Flask , jsonify, render_template, request

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template('form.html')

@app.route('/upload',methods=['POST'])
def get_data():
    request.files
    print("file content",request.files)
    return "we have received your data"

if __name__ == '__main__':
    app.run(debug=True)