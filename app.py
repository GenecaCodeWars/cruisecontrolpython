# imports
import os
import json
from bottle import route, run, request
from command import Command
from coordinate import Coordinate

# routes
@route('/')
def index():
    return "Placeholder for Python app"
    
@route('/command',method='POST')
def index():
    status = json.loads(request.body.read())
    if (status["RoundNumber"] == 0) :
        print "New game, I should probably reset"
    return json.dumps(createCommands())
    
def createCommands():
    cmdArray = []
    cmdArray.append(createCommand(1).__dict__)
    cmdArray.append(createCommand(2).__dict__)
    return cmdArray
    
def createCommand(vesselid):
    cmd = Command()
    cmd.vesselid = vesselid
    cmd.coordinate = createCoordinate(1, 1).__dict__
    return cmd
	
def createCoordinate(x, y):
    coordinate = Coordinate()
    coordinate.X = x
    coordinate.Y = y
    return coordinate

# start server and listen for requests
# for Cloud9 run(host=os.environ["OPENSHIFT_DIY_IP"], port=int(os.environ["PORT"]), debug=True)
run(host='0.0.0.0', port=int(os.environ["PORT"]), debug=True)
