import cherrypy
import os
import pickle
import time

hours = pickle.loads(open("./static/db.txt").read())
passwords = pickle.loads(open("./static/pwords.txt").read())
class HelloWorld(object):
    def index(self):
        return """
        	<!DOCTYPE html>
        	<html>
        		<head>
        		</head>
        		<body>
        			<h1>Add hours</h1>
        			<p>Enter Card #, Password, and Hours. Click "Add Hours"</p>
        			
        			<form method="get" action="addHours">
        				<input type="text" placeholder="card number" name="card"></input>
        				<input type="password" placeholder="password" name="password"></input>
        				<input type="text" placeholder="MM/DD/YY" name="date"></input>
        				<input type="number" placeholder="hours volunteered" name="volhours"></input>
        				<button type="submit">Add Hours</button>
        			</form>
        			
        			<h1>Show Hours</h1>
        			<p>Enter Card # and Password. Click "Retrieve Hours"</p>
        			
        			<form method="get" action="retrieveHours">
        				<input type="text" placeholder="card number" name="card" />
        				<input type="password" placeholder="password" name="password" />
        				<button type="submit">Retrieve Hours</button>
        			</form>
        		</body>
        	</html>
        """
    index.exposed = True
    
    def addHours(self, card, password, date, volhours):
    	hours = pickle.loads(open("./static/db.txt").read())
    	passwords = pickle.loads(open("./static/pwords.txt").read())
    	if passwords[card] == password:
    		hours[card][date] = hours[card].get(date, 0) + int(volhours)
    		pickle.dump(hours, open("./static/db.txt", "w"))
    		all = "<table border='1'>"
    		for key in sorted(hours[card]):
    			all = all + "<tr><td>" + key + "</td><td>" + str(hours[card][key]) + "</td></tr>"
    		all = all + "</table>"
    		return """
    			<h1>Hours for """ + card + """
    			<p>""" + all + """</p>
    			<a href="http://volunteerlogon.herokuapp.com/">Back to the main page</a>
    		"""
    	else:
    		return """
    			<h1>Incorrect password for """ + card + """
    			<a href="http://volunteerlogon.herokuapp.com/">Back to the main page</a>
    		"""
    addHours.exposed = True
    
    def retrieveHours(self, card, password):
    	hours = pickle.loads(open("./static/db.txt").read())
    	passwords = pickle.loads(open("./static/pwords.txt").read())
    	if passwords[card] == password:
    		all = "<table border='1'>"
    		for key in sorted(hours[card]):
    			all = all + "<tr><td>" + key + "</td><td>" + str(hours[card][key]) + "</td></tr>"
    		all = all + "</table>"
    		return """
    			<h1>Hours volunteered for """ + card + """</h1>
    			<p>""" + all + """</p>
    			<a href="http://volunteerlogon.herokuapp.com/">Back to the main page</a>
    		"""
    	else:
    		return """
    			<h1>Incorrect password for """ + card + """
    			<a href="http://volunteerlogon.herokuapp.com/">Back to the main page</a>
    		"""
    retrieveHours.exposed = True
cherrypy.config.update({'server.socket_host': '0.0.0.0',})
cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000')),})
cherrypy.quickstart(HelloWorld())