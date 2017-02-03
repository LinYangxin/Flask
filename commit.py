import datetime
from app import db,models
u = models.User.query.get(2)
p = models.Post(body='i love Fenrir', timestamp=datetime.datetime.utcnow(), author=u)
db.session.add(p)
db.session.commit()