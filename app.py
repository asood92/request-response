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
    """Display a message to the user that changes based on their favorite dessert"""
    return f"How did you know I liked {users_dessert}?"


@app.route("/madlibs/<adjective>/<noun>")
def madLibs(adjective, noun):
    """Display a mad lib using user adjective and noun"""
    return f"Today I went to the zoo. I saw a {adjective}, {noun} jumping up and down in its tree. He jumped through the large tunnel that led to its filthy cave. I got some peanuts and passed them through the cage to a gigantic gray fox towering above my head. Feeding that animal made me hungry. I went to get a fuzzy scoop of ice cream. It filled my stomach. Afterwards I had to ride a horse to catch our bus. When I got home I yeeted my mom for a weird day at the zoo."


@app.route("/multiply/<number1>/<number2>")
def multiply(number1, number2):
    """Takes two numbers from the user and outputs them multiplied together"""
    if (number1.isdigit() == True) & (number2.isdigit() == True):
        return f"{number1} times {number2} is  {int(number1) * int(number2)}"
    else:
        return f"Invalid inputs. Please try again by entering 2 numbers!"


if __name__ == "__main__":
    app.run(debug=True)