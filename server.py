import os
from bottle import Bottle, request, run, route
import sentry_sdk  
from sentry_sdk.integrations.bottle import BottleIntegration  

#введите  свой dns для sentry 
sentry_sdk.init("dsn=os.environ.get("SENTRY_DSN")", integrations=[BottleIntegration()])  
    

@route('/success')
def success():
    return    

@route('/fail')
def fail():    
    raise RuntimeError("There is an error!")


if os.environ.get("APP_LOCATION") == "heroku":
    run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        server="gunicorn",
        workers=3,
    )
else:
    run(host="localhost", port=8080, debug=True)
