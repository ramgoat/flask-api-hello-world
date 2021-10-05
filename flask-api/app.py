from flask import Flask
import rq_dashboard
from init_redis_rq import rq
from routes.main import blueprint_main
from routes.fruits import blueprint_fruit

def create_app():
    app = Flask(__name__)
    app.config["JSON_SORT_KEYS"] = False
    #app.config["RQ_REDIS_URL"] = 'redis://localhost:6379/0'
    #app.config['RQ_QUEUES'] = ['default']
    app.config.from_object(rq_dashboard.default_settings)

    app.register_blueprint(blueprint_fruit)
    app.register_blueprint(blueprint_main)
    app.register_blueprint(rq_dashboard.blueprint, url_prefix='/rq')

    rq.init_app(app)
    #create_workers()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run()