from . import DB # in other words, import from __init__

class Comment(DB.Model):
    id = DB.Column(DB.Integer,primary_key=True)
    name = DB.Column(DB.String(30))
    comment_text = DB.Column(DB.String(1000))