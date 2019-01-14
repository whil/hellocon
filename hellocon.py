# sixth Hello World program
__author__ = 'whil'

from datetime import datetime

import requests
from flask import Flask #, render_template
#from flask_script import Manager
#from flask_bootstrap import Bootstrap
from flask_moment import Moment

print('Hello World. Context is everything.')
ipgreeting = 'Hello from Flask!' 

response = requests.get('https://httpbin.org/ip')
ipquad = '{0}'.format(response.json()['origin'])
print('Your IP is {0}'.format(response.json()['origin']))

app = Flask(__name__)
#manager = Manager(app)
#bootstrap = Bootstrap(app)
moment = Moment(app)


##################################################

@app.errorhandler(404)
def page_not_found(e):
    return 'Four Oh Four' #render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return 'Five Oh Oh' #render_template('500.html'), 500

@app.route('/')
def index():
    str = '<h1>Hello World, from Flask! Context is everything!</h1>'
    return str #render_template('index.html', current_time=datetime.utcnow())
#    return render_template('index.html')

@app.route('/admin')
def admin():
    str = '<h1>Admin Interface</h1>'
    return str #render_template('index.html', current_time=datetime.utcnow())
#    return render_template('index.html')

###################
# THIS DOES NOT WORK
# localhost:5000/id/44
###################

@app.route('/id/pid')
def processVisitor(pid):
    str = pid
    print(pid)
#    str = 'Hello World, from Flask! Context is everything!' + id + '!'
    return str #render_template('index.html', current_time=datetime.utcnow())
#    return render_template('index.html')

'''
@app.route('/ip')
def ip():
    jello = 'chocolate cake'
    ipstr = 'not here'
    return render_template('ip.html', ipgreeting=ipgreeting, jello=jello, ipquad=ipquad)
'''
##################################################

if __name__ == '__main__':
    app.run(debug=True)

