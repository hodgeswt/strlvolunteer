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
        			<!-- Latest compiled and minified CSS -->
					<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
					
					<link rel="stylesheet" href="https://raw.githubusercontent.com/thomaspark/bootswatch/gh-pages/darkly/bootstrap.min.css">

					<!-- jQuery library -->
					<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>

					<!-- Latest compiled JavaScript -->
					<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
        		</head>
        		<body>
        			<div class="panel panel-default">
        				<div class="panel-heading">
        					<h1>Add hours</h1>
        					<p>Enter Card #, Password, and Hours. Click "Add Hours"</p>
        				</div>
        				<div class="panel-body">
        					<form method="get" action="addHours">
        						<input type="text" placeholder="card number" name="card"></input>
        						<input type="password" placeholder="password" name="password"></input>
        						<input type="text" placeholder="MM/DD/YY" name="date"></input>
        						<input type="number" placeholder="hours volunteered" name="volhours"></input>
        						<button type="submit">Add Hours</button>
        					</form>
        				</div>
        			</div>
        			
        			<div class="panel panel-default">
        				<div class="panel-heading">
        					<h1>Show Hours</h1>
        					<p>Enter Card # and Password. Click "Retrieve Hours"</p>
        				</div>
        				<div class="panel-body">
        					<form method="get" action="retrieveHours">
        						<input type="text" placeholder="card number" name="card" />
        						<input type="password" placeholder="password" name="password" />
        						<button type="submit">Retrieve Hours</button>
        					</form>
        				</div>
        			</div>
        			
        			<div class="panel panel-default">
        				<div class="panel-heading">
        					<h1>Add user</h1>
        					<p>Enter card #, card #, password, and password. Click "Add User"</p>
        				</div>
        				<div class="panel-body">
        					<form method="get" action="addUser">
        						<input type="text" placeholder="card number" name="card" />
        						<input type="text" placeholder="card number again" name="card2" />
        						<input type="password" placeholder="password" name="password" />
        						<input type="password" placeholder="password again" name="password2" />
        						<button type="submit">Add User</button>
        					</form>
        				</div>
        			</div>
        		</body>
        		<footer style="position: absolute; left:0; bottom:0;; width:100%;">
        			Copyright 2015 Will T. Hodges. All Rights Reserved.
        		</footer>
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
    			<head>
        			<!-- Latest compiled and minified CSS -->
					<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
					
					<link rel="stylesheet" href="https://raw.githubusercontent.com/thomaspark/bootswatch/gh-pages/darkly/bootstrap.min.css">

					<!-- jQuery library -->
					<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>

					<!-- Latest compiled JavaScript -->
					<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>    			
    			</head>
    			<body>
    				<h1>Hours for """ + card + """
    				<p>""" + all + """</p>
    				<a href="http://volunteerlogon.herokuapp.com/">Back to the main page</a>
    			</body>
    			<footer style="position: absolute; left:0; bottom:0;; width:100%;">
        			Copyright 2015 Will T. Hodges. All Rights Reserved.
        		</footer>
    		"""
    	else:
    		return """
    			<head>
        			<!-- Latest compiled and minified CSS -->
					<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
					
					<link rel="stylesheet" href="https://raw.githubusercontent.com/thomaspark/bootswatch/gh-pages/darkly/bootstrap.min.css">

					<!-- jQuery library -->
					<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>

					<!-- Latest compiled JavaScript -->
					<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>    			
    			</head>
    			<body>
    				<h1>Incorrect password for """ + card + """
    				<a href="http://volunteerlogon.herokuapp.com/">Back to the main page</a>
    			</body>
    			<footer style="position: absolute; left:0; bottom:0;; width:100%;">
        			Copyright 2015 Will T. Hodges. All Rights Reserved.
        		</footer>
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
    			<head>
        			<!-- Latest compiled and minified CSS -->
					<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
					
					<link rel="stylesheet" href="https://raw.githubusercontent.com/thomaspark/bootswatch/gh-pages/darkly/bootstrap.min.css">

					<!-- jQuery library -->
					<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>

					<!-- Latest compiled JavaScript -->
					<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>    			
    			</head>
    			<body>
    				<h1>Hours volunteered for """ + card + """</h1>
    				<p>""" + all + """</p>
    				<a href="http://volunteerlogon.herokuapp.com/">Back to the main page</a>
    			</body>
    			<footer style="position: absolute; left:0; bottom:0;; width:100%;">
        			Copyright 2015 Will T. Hodges. All Rights Reserved.
        		</footer>
    		"""
    	else:
    		return """
    			<head>
        			<!-- Latest compiled and minified CSS -->
					<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
					
					<link rel="stylesheet" href="https://raw.githubusercontent.com/thomaspark/bootswatch/gh-pages/darkly/bootstrap.min.css">

					<!-- jQuery library -->
					<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>

					<!-- Latest compiled JavaScript -->
					<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>    			
    			</head>
    			<h1>Incorrect password for """ + card + """
    			<a href="http://volunteerlogon.herokuapp.com/">Back to the main page</a>
    			<footer style="position: absolute; left:0; bottom:0;; width:100%;">
        			Copyright 2015 Will T. Hodges. All Rights Reserved.
        		</footer>
    		"""
    retrieveHours.exposed = True
    
    def addUser(self, card, card2, password, password2):
    	passwords = pickle.loads(open("./static/pwords.txt").read())
    	hours = pickle.loads(open("./static/db.txt").read())
    	
    	if card == card2 and password == password2 and (card not in hours):
    		passwords[card] = password
    		hours[card] = {}
    		pickle.dump(hours, open("./static/db.txt", "w"))
    		pickle.dump(passwords, open("./static/pwords.txt", "w"))
    		return """
    			<head>
        			<!-- Latest compiled and minified CSS -->
					<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
					
					<link rel="stylesheet" href="https://raw.githubusercontent.com/thomaspark/bootswatch/gh-pages/darkly/bootstrap.min.css">

					<!-- jQuery library -->
					<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>

					<!-- Latest compiled JavaScript -->
					<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>    			
    			</head>
    			<h1>Added user """ + card + """</h1>
    			<a href="http://volunteerlogon.herokuapp.com/">Back to the main page</a>
    			<footer style="position: absolute; left:0; bottom:0;; width:100%;">
        			Copyright 2015 Will T. Hodges. All Rights Reserved.
        		</footer>
    		"""
    	else:
    		return """
    			<head>
        			<!-- Latest compiled and minified CSS -->
					<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
					
					<link rel="stylesheet" href="https://raw.githubusercontent.com/thomaspark/bootswatch/gh-pages/darkly/bootstrap.min.css">

					<!-- jQuery library -->
					<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>

					<!-- Latest compiled JavaScript -->
					<script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>    			
    			</head>
    			<h1>An Error occurred. See Below.</h1>
    			<p>Either: Your usernames and passwords were not the same <em>OR</em> you are already in the database.</p>
    			<a href="http://volunteerlogon.herokuapp.com/">Back to the main page</a>
    			<footer style="position: absolute; left:0; bottom:0;; width:100%;">
        			Copyright 2015 Will T. Hodges. All Rights Reserved.
        		</footer>
    		"""
    addUser.exposed = True
cherrypy.config.update({'server.socket_host': '0.0.0.0',})
cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000')),})
cherrypy.quickstart(HelloWorld())