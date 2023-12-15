import os
from random import choice, randint

import crud
import model
import server

os.system("")

model.connect_to_db(server.app)

with app.app_context():
    model.db.create_all()