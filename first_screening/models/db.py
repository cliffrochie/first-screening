from first_screening import db


class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text)
    content = db.relationship("Content", backref="topic", lazy="dynamic")

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return "<Topic %r>" % self.name


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sequence_number = db.Column(db.Integer)
    title = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text, nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey("topic.id"), nullable=False)

    def __init__(self, sequence_number, title, body, topic_id):
        self.sequence_number = sequence_number
        self.title = title
        self.body = body
        self.topic_id = topic_id

    def __repr__(self):
        return "<Content %r>" % self.title


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False)

    def __init__(self, username, password, is_admin):
        self.username = username
        self.password = password
        self.is_admin = is_admin

    def __repr__(self):
        return "<User %r>" % self.username
