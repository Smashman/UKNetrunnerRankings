from flask import Blueprint
from models import Tournament, Participant, Result

tournament = Blueprint('tournament', __name__, url_prefix='/tournament')

