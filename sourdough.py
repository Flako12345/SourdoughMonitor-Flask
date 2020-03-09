import os
from app import create_app, config, db
from app.models import User
from flask_migrate import Migrate
import os
from config import config

app = create_app(config_name='development')
migrate = Migrate(app, db)

app.run(debug=True)

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}


#User.insert_test_user()










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





