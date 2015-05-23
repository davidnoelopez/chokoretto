from google.appengine.ext import ndb
import model

class Post(model.Base):
  user_key = ndb.KeyProperty(kind=model.User, required=True)
  date = ndb.StringProperty(default='')
  title = ndb.StringProperty(required=True)
  body = ndb.StringProperty(default='')
  