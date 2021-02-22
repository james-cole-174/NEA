####################################################################################################
#####                   Module Imports                                                         #####
####################################################################################################

from flask import Flask, escape, request, render_template, url_for 
import mysqlmodule as msm

####################################################################################################
#####                   Flask setup                                                            #####
####################################################################################################

app = Flask(__name__)

app.config['SECRET_KEY'] = '201def51bb6b28e0290a585c8eb778d6'

posts = [
    {
        'author': 'James',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2021'
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2022'
    }
]

print(msm.getAllTable("customers"))

####################################################################################################
#####                   Decorator link to pages                                                #####
####################################################################################################

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

####################################################################################################
#####                   Auto run site - MOVE                                                   #####
####################################################################################################

# Auto run site in website if run from this module
#if __name__ == '__main__':
#    app.run(debug=True)