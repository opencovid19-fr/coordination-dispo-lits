from model.user import User


def find_users():
    return [user.json for user in User.query]


def get_user_by_id(_id):
    """

    :param _id:
    :return:
    """
    return User.query.filter_by(id=_id).first()


def create_user(params):
    """

    :param params:
    :return:
    """
    user = User(**params)
    user.save()
    return user


def get_user_by_email(email):
    return User.query.filter_by(email=email).first()
