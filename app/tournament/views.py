from flask import Blueprint
from models import Tournament, Player, Result

tournament = Blueprint('tournament', __name__, url_prefix='/tournament')

