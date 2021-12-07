from app import create_app, db
from config import TestConfig
from app.Model.models import Challenge, Host, Prompt

app = create_app(TestConfig)

@app.before_first_request
def initDB(*args, **kwargs):
    db.drop_all()
    db.create_all()
    # if Challenge.query.count() == 0:
    #     host = Host(id=1, username="tyler", password_hash="123")
    #     db.session.add(host)
    #     db.session.commit()
    #     challenge = Challenge(host_id=1, joincode="AAAAAA", open = True, title="really cool test")
    #     host.challenges.append(challenge)
    #     db.session.add(challenge)
    #     db.session.commit()
    #     prompt = Prompt(text="test prompt zero", challenge_id=1)
    #     challenge.prompts.append(prompt)
    #     db.session.add(prompt)
    #     prompt = Prompt(text="test prompt one", challenge_id=1)
    #     challenge.prompts.append(prompt)
    #     db.session.add(prompt)
    #     db.session.commit()


if __name__ == "__main__":
    app.run(debug=True)