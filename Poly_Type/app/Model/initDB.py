#run this in the command line to fill up the database

from app import create_app, db
app = create_app()
app.app_context().push()
from app.Model.models import Host, Challenge, Prompt, Result
db.create_all()

host = Host(id=1, username="tyler", password_hash="123")
db.session.add(host)
db.session.commit()
challenge = Challenge(host_id=1, joincode="AAAAAA", open = False, title="really cool test")
host.challenges.append(challenge)
db.session.add(challenge)
db.session.commit()
prompt = Prompt(text="Test Prompt", challenge_id=1)
challenge.prompts.append(prompt)
db.session.add(prompt)
db.session.commit()
