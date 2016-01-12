import requests
from .. import db
from ..netrunner.models import Cycle, Pack
from requests.exceptions import HTTPError

cycle_api_url = ''
pack_api_url = 'http://netrunnerdb.com/api/sets/'


def update_cycles():
    pass  # Waiting on API from Alsciende


def update_packs():
    inserted_packs = 0
    try:
        data = requests.get(url=pack_api_url).json()
    except (HTTPError, ValueError):
        print 'An Error occurred, please try again later.'
        return
    data = sorted(data, key=lambda x: (x.get('cyclenumber'), x.get('number')))
    for pack in data:
        if pack.get('code') != 'draft' and Pack.query.filter_by(code=pack.get('code')).first() is None:
            new_pack = Pack()
            new_pack.name = pack.get('name')
            new_pack.code = pack.get('code')
            new_pack.num_in_cylce = pack.get('number')
            new_pack.cycle_id = pack.get('cyclenumber')
            inserted_packs += 1
            db.session.add(new_pack)
    print '{} new packs inserted.'.format(inserted_packs)
    db.session.commit()