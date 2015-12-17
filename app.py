import cherrypy
import os
import pickle

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
    
    def addHours(self, card, password, volhours):
    	hours = pickle.loads(open("./static/db.txt").read())
    	passwords = pickle.loads(open("./static/pwords.txt").read())
    	if passwords[card] == password:
    		hours[card] = hours[card] + int(volhours)
    		pickle.dump(hours, open("./static/db.txt", "w"))
    		return """
    			<h1>Hours for """ + card + """
    			<p>""" + str(hours[card]) + """</p>
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
    		return """
    			<h1>Hours volunteered for """ + card + """</h1>
    			<p>""" + str(hours[card]) + """</p>
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