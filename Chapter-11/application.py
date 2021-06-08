import os 
from flask import Flask, render_template, request
from  flask_bootstrap import Bootstrap
app = Flask (__name__)
Bootstrap(app)
application = app # for beanstalk

questions = [
    {
        "id": "1",
        "question": "What are the maximum read replicas for MySQL, PostGreSQL, and MariaDB RDS?",
        "answers": [
            "a) 3",
            "b) 5",
            "c) 10",
            "d) 25"
        ],
        "correct": "b) 5"
    },
    {
        "id": "2",
        "question": "Which of the following is not a valid type of AWS Load Balancer?",
        "answers": [
            "a) Application Load Balancer",
            "b) Classic Load Balancer",
            "c) Internal Load Balancer",
            "d) Network Load Balancer"
        ],
        "correct": "c) Internal Load Balancer"
    },
    {
        "id": "3",
        "question": "What is the max size for an Elastic Beanstalk Source Bundle?",
        "answers": [
            "a) 128 mb",
            "b) 256 mb",
            "c) 512 mb",
            "d) 1024 mb"
        ],
        "correct": "c) 512 mb"
    }
]

labels = [ 'correct', 'incorrect']
values = [ 3, 1 ]
colors = ["#F7464A", "#46FBD", "#FDB45C", "#FEDCBA"]

@app.route("/", methods=['POST', 'GET'])
def quiz():
    if request.method == 'GET':
        return render_template("index.html", data=questions)
    else:
        result = 0 
        total = 0 
        for question in questions:
            if request.form[question.get('id')] == question.get('correct'):
                result +=1
            total += 1
        return render_template('results.html', total=total, result=result)

if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying to production. 
    app.debug = True 
    app.run()  