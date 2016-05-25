#!/usr/bin/env python
import os
# from app import create_app, db
# from app import app, db
from app import create_app
from app.models import Hd, Wv, Slow
from flask.ext.script import Manager, Shell, Server
from flask.ext.migrate import Migrate, MigrateCommand

app=create_app()
manager = Manager(app)
# migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app,Hd=Hd,Wv=Wv,Slow=Slow)
# manager.add_command("runserver", Server(host='128.175.112.125'))
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)



@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
