from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:eeeee552@localhost/my soundcloud'
db = SQLAlchemy(app)  
class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    upload = db.Column(db.String(80), unique=True, nullable=False)  

    def __repr__(self,upload):
        return '<User %r>' % self.upload                            

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/page', methods= ['GET', 'POST'])
def page():
    if request.method == 'POST':
        file = request.files['uploads']
        file.save(f'{file.filename}')


        upload = user(upload=f'{file.filename}')
        db.session.add(upload)
        db.session.commit()


    return render_template('upload page.html')


if __name__ == "__main__":

    app.run(debug=True)
