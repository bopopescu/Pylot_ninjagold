"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

import random
import time
import datetime

class Ninjagold(Controller):
    def __init__(self, action):
        super(Ninjagold, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.

            self.load_model('WelcomeModel')
        """

    """ This is an example of a controller method that will load a view for the client """
    def index(self):
        """ 
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_all_users()
        """
        try:
            session['YourGold']
        except:
            session['YourGold'] = 0

        if not(session.get('Activities')): 
            session['Activities'] = [ 'Start' ]
        print session['YourGold']
        return self.load_view('index.html')
    
    def process(self):
        if request.form['building'] == "farm":
            print "From farm"
            val = random.randrange(10,20)
            session['YourGold']  += val 
            print val
        elif request.form['building'] == "cave":
            print "From cave"
            val = random.randrange(5,10)
            session['YourGold']  += val
        elif request.form['building'] == "house":
            print "from house"
            val = random.randrange(2,5)
            session['YourGold']  += val
        elif request.form['building'] == "casino":
            print "from casino"
            i = random.randrange(0,1)
            if i:
                val = random.randrange(0,50)
                session['YourGold']  += val
            else:
                val = random.randrange(0,50)
                session['YourGold']  -= val

        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

        actv = ''
        if  request.form['building'] == 'farm' or request.form['building'] == 'cave' or request.form['building'] == 'house':            
            actv = 'Earned ' + str(val) + ' gold from ' + request.form['building'] + ' ! ' +  st
        else:
            actv = 'Entered a casino and lost ' + str(val) + ' gold ... Ouch... ' + st

        print session['Activities']
        session['Activities'].append(actv)


        return redirect('/')

 