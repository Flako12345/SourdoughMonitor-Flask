from flask import Blueprint



main = Blueprint('main',__name__)

# Imported last to avoid circular dependencies
from . import views, forms