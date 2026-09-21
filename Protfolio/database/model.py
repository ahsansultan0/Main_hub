import sqlalchemy as db
from sqlalchemy import text

engine=db.create_engine('sqlite:///posts.db')

print('Engine created')


meta_obj=db.MetaData()

posts=db.Table(

    'posts',
    meta_obj,
    db.Column('id', db.Integer, primary_key=True),
    db.Column("title",db.String,nullable=False),
    db.Column('content',db.String,nullable=False),
    db.Column("user_id", db.String(255), nullable=False)


)

#with engine.begin() as connection:
 #   connection.execute(
  #      text("ALTER TABLE posts DROP COLUMN author")
   # )
connection =engine.connect()
meta_obj.create_all(engine)



