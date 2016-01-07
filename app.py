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
        			<a href="https://github.com/hodgeswt/strlvolunteer"><img style="position: absolute; top: 0; right: 0; border: 0;" src="https://camo.githubusercontent.com/a6677b08c955af8400f44c6298f40e7d19cc5b2d/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6769746875622f726962626f6e732f666f726b6d655f72696768745f677261795f3664366436642e706e67" alt="Fork me on GitHub" data-canonical-src="https://s3.amazonaws.com/github/ribbons/forkme_right_gray_6d6d6d.png"></a>
        			<div class="panel panel-default">
        				<div class="panel-heading">
        					<h1>Add hours</h1>
        					<p>Enter username, Password, and Hours. Click "Add Hours"</p>
        				</div>
        				<div class="panel-body">
        					<form method="get" action="addHours">
        						<input type="text" placeholder="username" name="card"></input>
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
        					<p>Enter username and Password. Click "Retrieve Hours"</p>
        				</div>
        				<div class="panel-body">
        					<form method="get" action="retrieveHours">
        						<input type="text" placeholder="username" name="card" />
        						<input type="password" placeholder="password" name="password" />
        						<button type="submit">Retrieve Hours</button>
        					</form>
        				</div>
        			</div>
        			
        			<div class="panel panel-default">
        				<div class="panel-heading">
        					<h1>Add user</h1>
        					<p>Enter username, username, password, and password. Click "Add User"</p>
        					<p>Username must be letters only. No numbers or special characters.</p>
        				</div>
        				<div class="panel-body">
        					<form method="get" action="addUser">
        						<input type="text" placeholder="username" name="card" />
        						<input type="text" placeholder="username" name="card2" />
        						<input type="password" placeholder="password" name="password" />
        						<input type="password" placeholder="password again" name="password2" />
        						<button type="submit">Add User</button>
        					</form>
        				</div>
        			</div>
        			
        			<div class="panel panel-default">
        				<div class="panel-heading">
        					<h1>Change password</h1>
        					<p>Enter username, current password, new password, and new password again.</p>
        				</div>
        				<div class="panel-body">
        					<form method="get" action="changeUsername">
        						<input type="text" placeholder="username" name="card" />
        						<input type="password" placeholder="current password" name="cpass" />
        						<input type="password" placeholder="new password" name="npass1" />
        						<input type="password" placeholder="new password" name="npass2" />
        						<button type="submit">Change password</button>
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
    		total = 0
    		for key in sorted(hours[card]):
    			all = all + "<tr><td>" + key + "</td><td>" + str(hours[card][key]) + "</td></tr>"
    			total = total + hours[card][key]
    		all = all + "<tr><td>Total hours:</td><td>" + str(total) + "</td></tr></table>"
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
    				<h1>Hours for """ + card + """</h1>
    				<p>""" + all + """</p>
    				<a href="http://strlvolunteerlogs.herokuapp.com/">Back to the main page</a>
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
    				<a href="http://strlvolunteerlogs.herokuapp.com/">Back to the main page</a>
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
    		total = 0
    		for key in sorted(hours[card]):
    			all = all + "<tr><td>" + key + "</td><td>" + str(hours[card][key]) + "</td></tr>"
    			total = total + hours[card][key]
    		all = all + "<tr><td>Total hours:</td><td>" + str(total) + "</td></tr></table>"
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
    				<a href="http://strlvolunteerlogs.herokuapp.com/">Back to the main page</a>
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
    			<a href="http://strlvolunteerlogs.herokuapp.com/">Back to the main page</a>
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
    		file = open("./static/db.txt", "w")
    		pickle.dump(hours, file)
    		file.close()
    		
    		file = open("./static/pwords.txt", "w")
    		pickle.dump(passwords, file)
    		file.close()
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
    			<a href="http://strlvolunteerlogs.herokuapp.com/">Back to the main page</a>
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
    			<a href="http://strlvolunteerlogs.herokuapp.com/">Back to the main page</a>
    			<footer style="position: absolute; left:0; bottom:0;; width:100%;">
        			Copyright 2015 Will T. Hodges. All Rights Reserved.
        		</footer>
    		"""
    addUser.exposed = True
    
    def pwords(self):
		return open("./static/pwords.txt").read()
    pwords.exposed = True
    
    def db(self):
		return open("./static/db.txt").read()
    db.exposed = True
    
    @cherrypy.expose
    def changeUsername(self, card, cpass, npass1, npass2):
    	passwords = pickle.loads(open("./static/pwords.txt").read())
    	hours = pickle.loads(open("./static/db.txt").read())
    	
    	if passwords[card] == cpass and npass1 == npass2:
    		passwords[card] = npass1
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
    			<h1>Password successfully changed for """ + card + """</h1>
    			<a href="http://strlvolunteerlogs.herokuapp.com/">Back to the main page</a>
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
    			<p>Either: Your new password did not match in both fields <em>OR</em> your current password is incorrect.</p>
    			<p>If you do not know your current password, email <a href=="mailto:hodges.wt@gmail.com">Will Hodges</a> and he can reset it for you.</p>
    			<a href="http://strlvolunteerlogs.herokuapp.com/">Back to the main page</a>
    			<footer style="position: absolute; left:0; bottom:0;; width:100%;">
        			Copyright 2015 Will T. Hodges. All Rights Reserved.
        		</footer>
    		"""
	changeUsername.exposed = True

    	
cherrypy.config.update({'server.socket_host': '0.0.0.0',})
cherrypy.config.update({'server.socket_port': int(os.environ.get('PORT', '5000')),})
cherrypy.quickstart(HelloWorld())