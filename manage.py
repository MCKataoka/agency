from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from models import db, Actor, Movie

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def seed():
    Movie(title='Movie 1', release_date='2022-05-06').insert()
    Movie(title='Movie 2', release_date='2022-05-07').insert()

    Actor(name='Jason', age=22, gender='male').insert()
    Actor(name='Janice', age=11, gender='female').insert()


if __name__ == '__main__':
    manager.run()
