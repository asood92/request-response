from flask import Flask

app = Flask(__name__)


@app.route("/")
def homepage():
    """Shows a greeting to the user."""
    return "Are you there, world? It's me, Ducky!"


@app.route("/penguins")
def myFavoriteAnimal():
    return "Penguins are cute!"


@app.route("/dessert/<users_dessert>")
def userDessert(users_dessert):
    """Display a message tot he user that changes based on their favorite dessert"""
    return f"How did you know I liked {users_dessert}?"


if __name__ == "__main__":
    app.run(debug=True)