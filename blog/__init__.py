from flask import Flask

from flask_login import LoginManager
from flask_migrate import Migrate
from flask_misaka import Misaka
from flask_sqlalchemy import SQLAlchemy
from config import Config



app = Flask(__name__) # syntax : app.run(host =None , port =None , debug =None , options) # app.run(host ='0.0.0.0', port =80) # public # app.run(debug =True) # for development
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

Misaka(app)

with app.app_context():
    if db.engine.url.drivername=='sqlite':
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

from blog import errors, models, routes
