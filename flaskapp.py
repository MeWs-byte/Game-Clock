from flask import Flask, render_template, request, redirect, url_for, flash
from segmentTimer import showTimer
import button 

gameTime = ""
gameTimeB = ""
lastGameTimePlayer1 = ""
lastGameTimePlayer2 = ""
gameStart = ""
gameStatus = "unstarted"
app = Flask(__name__)
app.secret_key = b'_1#y2l"F4Q8z\n\xec]/'

@app.route('/', methods=['GET', 'POST'])
@app.route('/index/', methods=['GET', 'POST'])      # get a mini dash going here to control all the states and see incoming alarm
def index():
    
    global gameTime, gameStatus, gameTimeB
    global endIt
    
    if request.method == "POST":
        try:
            
            return redirect(url_for('index'))
            
        except:
            flash("Invalid type for clockStateButton")
        return redirect(url_for('index'))
    
    if request.method == "GET" and request.args.get("GameTime", ""):
        gameTime = request.args.get("GameTime", "")
        print('this is gametime')
        print(gameTime)  
        gameStatus = "started"
    
    if request.method == "GET" and request.args.get("GameTimeB", ""):
        gameTimeB = request.args.get("GameTimeB", "")
        print('this is gametime')
        print(gameTimeB) 
        gameStatus = "startedB"
    if request.method == "GET" and request.args.get("reset", ""):
        resetMe = request.args.get("reset", "")
        print('this is reset')
        #print(resetMe) 
        gameStatus = "unstarted"
        button.endIt = 'ended'
   
    #showTimer(int(gameTime),00)

      
    return render_template('index.html')
    


def flaskRunner():          #  who runs the world?

    app.run(host="0.0.0.0",threaded=True)