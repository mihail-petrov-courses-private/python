from flask import Flask

from controllers.task_controller    import task_route_registry
from controllers.project_controller import project_route_registry
from controllers.user_controller    import user_route_registry

# трябва да си направим Flask приложение
app = Flask(__name__)

app.register_blueprint(task_route_registry)
app.register_blueprint(project_route_registry)
app.register_blueprint(user_route_registry)

if __name__ == '__main__':
    app.run()