from project import db

class Recipe(db.Model):

    __tablename__ = "recipes"

    id = db.Column(db.INTEGER, primary_key=True)
    recipe_title = db.Column(db.String, nullable=False)
    recip_description = db.Column(db.String, nullable=False)

    def __init__(self, title, description):
        self.recipe_title = title
        self.recip_description = description

    def __repr__(self):
        return '<title {}'.format(self.name)