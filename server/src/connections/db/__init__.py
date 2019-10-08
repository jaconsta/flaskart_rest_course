from sqlalchemy.orm import scoped_session

from .engine import Db, init_db, drop_db  # , Session

# session = scoped_session(Session)

db = Db()
