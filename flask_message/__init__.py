from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Shell, Manager
from flask_debugtoolbar import DebugToolbarExtension as DebugTool


app = Flask('flask_message')
# manager = Manager(app)
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
Migrate(app, db)
# manager.add_command('db', MigrateCommand)
toolbar = DebugTool(app)

from flask_message import views, errors
