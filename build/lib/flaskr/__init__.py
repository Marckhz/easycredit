import os

from flask import Flask
from flask import Flask, render_template, request, json
#from sqlachemy import create_engine
from flask_sqlalchemy import SQLAlchemy




#db_string= #here goes path for app


def create_app(test_config=None):

    """
    create app
    """

    app = Flask(__name__, instance_relative_config = True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    

    from . import auth
    app.register_blueprint(auth.bp)

    from . import db
    db.init_app(app)





    return app
if __name__ == '__main__':
        app.run()