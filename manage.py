from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import db
from run import create_app
import os

app = create_app(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()