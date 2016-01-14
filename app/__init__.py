from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.uploads import UploadSet, configure_uploads

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('settings')
app.config.from_pyfile('settings.py')

# Setup debugtoolbar, if we're in debug mode.
if app.debug:
    from flask.ext.debugtoolbar import DebugToolbarExtension
    toolbar = DebugToolbarExtension(app)

# Flask extensions
db = SQLAlchemy(app)

# Flask uploads
tournament_exports = UploadSet('tournamentExports', ('json', 'txt'))

configure_uploads(app, [tournament_exports])

# Views
import views

# Blueprints
from .user.views import user_bp as user_blueprint
app.register_blueprint(user_blueprint)

from .tournament.views import tournament as tournament_blueprint
app.register_blueprint(tournament_blueprint)

# Netrunner
from .netrunner.models import Identity, Faction, Side