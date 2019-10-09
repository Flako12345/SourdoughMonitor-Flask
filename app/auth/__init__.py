from flask import Blueprint


auth = Blueprint('auth', __name__)

# Imported last to avoid circular dependencies
from . import views, forms