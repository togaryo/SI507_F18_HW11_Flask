from flask import Flask, render_template
import requests
import json
from secrets import api_key

params={'api-key': api_key}


app = Flask(__name__) # app is named from the name of file

@app.route('/')
def index():
    return '<h1>Welcome!</h1>'



#nm = input("what is the name ")
@app.route('/user/<nm>' ) #decorating function
def user_name(nm):
    baseurl ='https://api.nytimes.com/svc/topstories/v2/'
    global params
    url = baseurl + 'technology' +'.json'
    data =requests.get(url, params).json()
    count = 0
    data_list = []

    for i in data["results"]:
        count += 1
        data_list.append(str(count) + ". " + str(i["title"]) + " (" + str(i["url"]) + ") ")
        #print(count)
        if (count == 5):
            break
    return render_template('user.html', name=nm, my_list=data_list)


if __name__ == '__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)
