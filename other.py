from app import db
from app.models import User, Post

u = User(username = "John", email = "john@ex.com")
db.session.add(u)
db.session.commit()