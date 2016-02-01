def name_format(user):
    if user.first_name is not None or user.last_name is not None:
        name = "{user.first_name} '{user.nickname}' {user.last_name}".format(user=user)
    else:
        name = user.nickname
    return name