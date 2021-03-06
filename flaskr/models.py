from flaskr import db, ma
from marshmallow_sqlalchemy import ModelSchema

#DBのモデリングを行ったModel-----------------
class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    text = db.Column(db.Text)

    def __repr__(self):
        return '<Entry id={id} title={title!r}>'.format(
                id=self.id, title=self.title)

#json変換用----------------------------------
class EntrySchema(ma.ModelSchema):
    class Meta:
        model = Entry

def init():
    db.create_all()