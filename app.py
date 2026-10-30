from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hack.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Hackathon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(300), nullable=False)

    def __repr__(self):
        return f"<Hackathon {self.name}>"
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    university = db.Column(db.String(150), nullable=False)
    major = db.Column(db.String(100), nullable=False)
    year = db.Column(db.String(50), nullable=False)
    skills = db.Column(db.String(300), nullable=False)
    interests = db.Column(db.String(300), nullable=False)
    experience = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"
    
class Ack(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_name = db.Column(db.String(100), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    status = db.Column(db.String(20), default="pending")

    receiver = db.relationship("User", backref="acks_received")

    def __repr__(self):
        return f"<Ack to {self.receiver_id}>"
    
@app.route("/discover")
def discover():
    hackathons = Hackathon.query.all()
    return render_template("discover.html", hackathons=hackathons)
   
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/teammates")
def teammates():
    users = User.query.all()
    return render_template("teammates.html", users=users)

@app.route("/send-ack/<int:user_id>", methods=["POST"])
def send_ack(user_id):
    user = User.query.get_or_404(user_id)

    existing_ack = Ack.query.filter_by(
        sender_name="Demo User",
        receiver_id=user.id
    ).first()

    if not existing_ack:
        ack = Ack(
            sender_name="Demo User",
            receiver_id=user.id,
            status="pending"
        )

        db.session.add(ack)
        db.session.commit()

    return redirect(url_for("teammates", sent=user.id))

if __name__ == "__main__":
    app.run(debug=True)

