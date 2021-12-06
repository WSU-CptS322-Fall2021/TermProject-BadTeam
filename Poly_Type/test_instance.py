from app import create_app, db
from config import TestConfig

app = create_app(TestConfig)

@app.before_first_request
def initDB(*args, **kwargs):
    db.drop_all()
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)