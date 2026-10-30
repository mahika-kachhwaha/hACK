from app import app, db, Hackathon, User

with app.app_context():
    # Clear existing demo hackathons so rerunning this file
    # does not create duplicates.
    Hackathon.query.delete()
    User.query.delete()
    hackathons = [
        Hackathon(
            name="Spartan Hack",
            location="San Jose, CA",
            date="November 14–15, 2026",
            description="A student hackathon bringing developers together to build creative projects."
        ),
        Hackathon(
            name="Bay Area Hacks",
            location="San Francisco, CA",
            date="December 5–6, 2026",
            description="A weekend hackathon for students interested in technology, design, and innovation."
        ),
        Hackathon(
            name="Hack the Future",
            location="Online",
            date="December 12–13, 2026",
            description="A virtual hackathon for students looking to collaborate and build new ideas."
        )
    ]

    db.session.add_all(hackathons)
    users = [
        User(
            name="Maya Patel",
            university="San Jose State University",
            major="Computer Science",
            year="Junior",
            skills="Python, Machine Learning, Java",
            interests="AI, Sustainability, Education",
            experience="2 hackathons"
        ),
        User(
            name="Jordan Lee",
            university="San Jose State University",
            major="Software Engineering",
            year="Sophomore",
            skills="JavaScript, React, HTML/CSS",
            interests="Web Development, FinTech, Design",
            experience="First-time hacker"
        ),
        User(
            name="Alex Chen",
            university="UC Berkeley",
            major="Data Science",
            year="Junior",
            skills="Python, SQL, Data Visualization",
            interests="Data Science, Healthcare, AI",
            experience="1 hackathon"
        )
    ]

    db.session.add_all(users)
    db.session.commit()

print("Demo hackathons and users added successfully!")