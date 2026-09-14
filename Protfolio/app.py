from flask import Flask,render_template,request
from database.model import posts,engine
import sqlalchemy as db

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')

@app.route('/read/<int:id>')
def read(id):

    connection = engine.connect()

    post = connection.execute(
        db.select(posts).where(posts.c.id == id)
    ).fetchone()
    
    return render_template(
        'read_post.html',
        post=post
    )


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('project.html')

@app.route('/community')
def community():
    connection=engine.connect()
    result= connection.execute( 
        
        
    db.select(posts))  
    return render_template('community.html',posts=result)
    
    


@app.route('/post', methods=['GET', 'POST'])
def post():

    if request.method == "GET":
        return render_template('create_post.html')

    if request.method == "POST":
        message = "Post created successfully!"
        title=request.form['title']
        content=request.form['content']
        connection=engine.connect()
        connection.execute(
            db.insert(posts).values(title=title,content=content)


        )
        connection.commit()

        return render_template(
            'create_post.html',
            message=message
        )


@app.get('/delete')
def delete():
    connection=engine.connect()
    connection.execute(db.delete(posts))
    connection.commit()
    return render_template("home.html")





if __name__ == "__main__":
    app.run(debug=True)