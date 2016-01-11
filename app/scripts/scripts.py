import json, requests
from .. import db
from ..netrunner.models import Cycle, Pack

cycle_api_url = ''
pack_api_url = 'http://netrunnerdb.com/api/sets/'


def update_cycles():
    pass  # Waiting on API from Alsciende


def update_packs():
    data = requests.get(url=pack_api_url).json()
    data = sorted(data, key=lambda x: (x.get('cyclenumber'), x.get('number')))
    all_packs = Pack.query.all()
    for pack in data:
        if pack.get('code') != 'draft':
            new_pack = Pack()
            new_pack.name = pack.get('name')
            new_pack.code = pack.get('code')
            new_pack.num_in_cylce = pack.get('number')
            new_pack.cycle_id = pack.get('cyclenumber')
            print new_pack.name
            db.session.add(new_pack)
    db.session.commit()