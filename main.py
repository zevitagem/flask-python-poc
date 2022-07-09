from flask import Flask
from Source.Infrastructure.Http.Controllers import auth
import os

template_dir = os.path.abspath('Source/Application/Views')
app = Flask(__name__, template_folder=template_dir)

if __name__ == "__main__":
  app.register_blueprint(auth.bp)
  app.run()
