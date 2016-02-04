import requests
from .. import db
from ..netrunner.models import Cycle, Pack, Identity, Faction, Side
from requests.exceptions import HTTPError

cycle_api_url = ''
pack_api_url = 'http://netrunnerdb.com/api/sets/'
cards_api_url = 'http://netrunnerdb.com/api/cards/'


def get_api_data(url):
    try:
        data = requests.get(url=url).json()
    except (HTTPError, ValueError):
        print 'An Error occurred, please try again later.'
        return
    return data


def update_cycles():
    pass  # Waiting on API from Alsciende


def update_packs():
    inserted_packs = 0
    data = get_api_data(pack_api_url)
    data = sorted(data, key=lambda x: (x.get('cyclenumber'), x.get('number')))
    for pack in data:
        if pack.get('code') != 'draft' and Pack.query.filter_by(code=pack.get('code')).first() is None:
            new_pack = Pack()
            new_pack.name = pack.get('name')
            new_pack.code = pack.get('code')
            new_pack.num_in_cycle = pack.get('number')
            new_pack.cycle_id = pack.get('cyclenumber')
            inserted_packs += 1
            db.session.add(new_pack)
    print '{} new packs inserted.'.format(inserted_packs)
    db.session.commit()


def update_ids():
    inserted_ids = 0
    data = get_api_data(cards_api_url)
    identities = filter(lambda x: x.get('type_code') == 'identity', data)
    for ident in identities:
        if ident.get('faction_code') == 'neutral' or ident.get('set_code') == 'draft':
            continue
        if Identity.query.filter_by(code=ident.get('code')).first() is None:
            ident_record = Identity()
            ident_record.code = ident.get('code')
            ident_record.name = ident.get('title')
            if ident.get('imagesrc'):
                ident_record.image_url = 'http://netrunnerdb.com{}'.format(ident.get('imagesrc'))
            ident_record.faction = Faction.query.filter_by(code=ident.get('faction_code')).first()
            inserted_ids += 1
            db.session.add(ident_record)
    print '{} new identities inserted.'.format(inserted_ids)
    db.session.commit()


def setup_tables():
    sides = [
        {'name': 'Corp'},
        {'name': 'Runner'},
    ]
    cycles = [
        {'name': 'Core Set', 'code': 'core'},
        {'name': 'Genesis', 'code': 'genesis'},
        {'name': 'Creation and Control', 'code': 'cac'},
        {'name': 'Spin', 'code': 'spin'},
        {'name': 'Honor and Profit', 'code': 'hap'},
        {'name': 'Lunar', 'code': 'lunar'},
        {'name': 'Order and Chaos', 'code': 'oac'},
        {'name': 'SanSan', 'code': 'sansan'},
        {'name': 'Data and Destiny', 'code': 'dad'},
        {'name': 'Mumbad', 'code': 'mumbad'},
    ]
    for side in sides:
        db.session.add(Side(**side))
    for cycle in cycles:
        db.session.add(Cycle(**cycle))

    corp_id = Side.query.filter_by(name='Corp').first().id
    runner_id = Side.query.filter_by(name='Runner').first().id
    factions = [
        {'name': 'Anarch', 'code': 'anarch', 'side_id': runner_id},
        {'name': 'Criminal', 'code': 'criminal', 'side_id': runner_id},
        {'name': 'Shaper', 'code': 'shaper', 'side_id': runner_id},
        {'name': 'Haas-Bioroid', 'code': 'haas-bioroid', 'side_id': corp_id},
        {'name': 'Jinteki', 'code': 'jinteki', 'side_id': corp_id},
        {'name': 'NBN', 'code': 'nbn', 'side_id': corp_id},
        {'name': 'Weyland Consortium', 'code': 'weyland-consortium', 'side_id': corp_id},
        {'name': 'Apex', 'code': 'apex', 'side_id': runner_id},
        {'name': 'Adam', 'code': 'adam', 'side_id': runner_id},
        {'name': 'Sunny Lebeau', 'code': 'sunny-lebeau', 'side_id': runner_id},
    ]
    for faction in factions:
        db.session.add(Faction(**faction))
    db.session.commit()

    update_packs()
    update_ids()