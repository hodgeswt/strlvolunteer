import cherrypy
import os

file = open("./static/db.txt")
hours = file.read()
file.close()

file = open("./static/pwords.txt")
passwords = file.read()
file.close()

class HelloWorld(object):
    def index(self):
        return """
        	<!DOCTYPE html>
        	<html>
        		<head>
        		</head>
        		<body>
        			<h1>Add hours</h1>
        			<p>Enter Card #, Password, and Hours. Click "enter"</p>
        			
        			<form method="get" action="addHours">
        				<input type="text" placeholder="card number" name="card"></input>
        				<input type="password" placeholder="password" name="password"></input>
        				<input type="number" placeholder="hours volunteered" name="hours"></input>
        				<button type="submit">Add Hours</button>
        			</form>
        		</body>
        	</html>
        """
    index.exposed = True
    
    def addHours(self, card, password, hours):
    	if passwords[card] == password:
    		hours[card] = hours[card] + hours
    		return """
    			<h1>Hours for """ + card + """
    			<p>""" + hours[card] + """</p>
    			<a href="http://volunteerlogon.herokuapp.com/">Back to the main page</a>
    		"""
    	else:
    		return """
    			<h1>Incorrect password for """ + card + """
    			<a href="http://volunteerlogon.herokuapp.com/">Back to the main page</a>
    		"""
    index.exposed = True

cherrypy.config.update({'server.socket_host': '0.0.0.0',})
cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000')),})
cherrypy.quickstart(HelloWorld())