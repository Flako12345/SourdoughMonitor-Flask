from flask_httpauth import HTTPBasicAuth
from flask import g
from ..models import User


auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(email, password):
    if email == '':
        return False
    user = User.query.filter_by(email = email).first()
    if not user:
        return False

    g.current_user = user
    return user.check_password(password)

