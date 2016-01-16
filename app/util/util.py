import json
from app import tournament_exports
from ..tournament.models import Participant, Result
from ..netrunner.models import Identity


def process_tournament(tournament_record):
    process_json_tournament(tournament_record) if tournament_record.file_type == 'json'\
        else process_txt_tournament(tournament_record)


def process_json_tournament(tournament_record):
    f = open(tournament_exports.path(tournament_record.filename), 'r')
    data = json.load(f)
    f.close()

    participants = sorted(data.get('players'), key=lambda x: (-x.get('matchPoints'), -x.get('strengthOfSchedule'),
                                                              -x.get('extendedStrengthOfSchedule')))

    position = 1
    for participant in participants:
        participant_record = Participant()
        print 'Position:   {}'.format(position)
        print 'Name:       {}'.format(participant.get('name'))
        print 'Corp ID:    {}'.format(participant.get('corpIdentity'))
        print 'Runner ID:  {}'.format(participant.get('runnerIdentity'))
        print 'Points:     {}'.format(participant.get('matchPoints'))
        print 'SoS:        {}'.format(participant.get('strengthOfSchedule'))
        print 'xSoS:       {}'.format(participant.get('extendedStrengthOfSchedule'))
        print ''
        participant_record.corp_ident = Identity.query.filter(Identity.name.like('%{}%'.format(
            participant.get('corpIdentity')))).first()
        participant_record.runner_ident = Identity.query.filter(Identity.name.like('%{}%'.format(
            participant.get('runnerIdentity')))).first()

        result_record = Result()

        result_record.position = position
        position += 1
        result_record.points = participant.get('matchPoints')
        result_record.strength_of_schedule = participant.get('strengthOfSchedule')
        result_record.extended_sos = participant.get('extendedStrengthOfSchedule')

        participant_record.result.append(result_record)

        tournament_record.participants.append(participant_record)


def process_txt_tournament(tournament_record):
    f = open(tournament_exports.path(tournament_record.filename), 'r')
    for idx, line in enumerate(f):
        if idx == 0:
            continue  # Ignore Header line
        player_info = line.strip().split(';')
        print 'Position:   {}'.format(player_info[0])
        print 'Name:       {}'.format(player_info[1])
        names = player_info[1].split('\'')
        print 'First name: {}'.format(names[0].strip())
        print 'Last name:  {}'.format(names[2].strip() if 2 < len(names) else None)
        print 'Nickname:   {}'.format(names[1].strip())
        print 'Corp ID:    {}'.format(player_info[3])
        print 'Runner ID:  {}'.format(player_info[5])
        print 'Points:     {}'.format(player_info[7])
        print 'SoS:        {}'.format(player_info[8])
        wdl = player_info[10].strip().split('-')
        print 'Wins:       {}'.format(wdl[0])
        print 'Draws:      {}'.format(wdl[1])
        print 'Losses:     {}'.format(wdl[2])
        print ''
    f.close()