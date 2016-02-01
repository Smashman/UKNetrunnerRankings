from flask import Blueprint, render_template
from ..netrunner.models import Identity

nr_bp = Blueprint('netrunner', __name__, url_prefix='/netrunner')


@nr_bp.route('/identity/<int:identity_id>/')
def ident_page(identity_id):
    identity = Identity.query.get_or_404(identity_id)
    return render_template('netrunner/identity.html', identity=identity)