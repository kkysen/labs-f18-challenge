from flask import Flask, Response, render_template

from api.pokeapi import Pokemon, fetch_pokemon

app: Flask = Flask(__name__)


@app.route("/")
def index() -> Response:
    return render_template("index.html")


def is_int(int_or_string: str) -> bool:
    try:
        int(int_or_string)
        return True
    except ValueError:
        return False


def query_pokemon_response(query: str) -> str:
    is_id = is_int(query)
    id_or_name = "id" if is_id else "name"
    
    # suppress errors b/c user-facing code
    # noinspection PyBroadException
    try:
        pokemon: Pokemon = fetch_pokemon(query.lower())
    except Exception:
        return f"The pokemon with {id_or_name} {query} doesn't exist"
    
    if is_id:
        return f"The pokemon with id {pokemon.id} is {pokemon.name.capitalize()}"
    else:
        return f"{pokemon.name.capitalize()} has id {pokemon.id}"


@app.route("/pokemon/<query>")
def query_pokemon(query: str) -> str:
    return f"<h1>{query_pokemon_response(query)}</h1>"


if __name__ == "__main__":
    app.run()
