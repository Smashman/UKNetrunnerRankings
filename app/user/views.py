from flask import Blueprint
from models import User

user_bp = Blueprint('user', __name__, url_prefix='/user')