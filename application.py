import os
from app import create_app, config, db
from app.models import User
from flask_migrate import Migrate
from flask_migrate import upgrade
import config
import click

appconfig = os.getenv('CONFIG', 'development')# or 'config.DevelopmentConfig'
app = create_app(config_name=appconfig)
app.secret_key = os.getenv('SECRET_KEY', 'VerySecret')
#app.config['SESSION_TYPE'] = 'filesystem'
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(debug=False)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}

@app.cli.command()
def deploy():
    # Migrate database
    upgrade()
    # Insert test user
    User.insert_test_user()











"""
db.create_all()
firstUser=User(email='testemail', username='testusername')
firstUser.set_password('testpassword')
db.session.add(firstUser)
db.session.commit()
"""
"""
feed1 = Feeding(sourdough_id=1)
feed2 = Feeding(sourdough_id=1)
db.session.add(feed1, feed2)
db.session.commit()
current = Sourdough.query.get(1)
feeds = current.feedings.all()
for feed in feeds:
    print(feed.timestamp)
print(current.feedings.all())
"""

#current = User.query.get(1)
#print(current)





