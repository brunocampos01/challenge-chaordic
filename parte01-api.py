from flask import request
from flask_api import FlaskAPI, status, exceptions
import time

# contrução de uma instancia da class Flask
app = FlaskAPI(__name__)

products = {
    0: 'mesa',
    1: 'cadeira'
}

def note_repr(key):
    return {
        'id': key,
        'name': products[key]
    }

# route p todos os products e para updates
@app.route("/chaordic.com.br/v1/products/", methods=['GET', 'POST'])
def products_list():
    """
    List or create products.
    """


    if request.method == 'POST':
        note = str(request.data.get('text', ''))
        idx = max(products.keys()) + 1
        products[idx] = note
        return note_repr(idx), status.HTTP_201_CREATED

    # request.method == 'GET'
    return [note_repr(idx) for idx in sorted(products.keys())]


@app.route("/chaordic.com.br/v1/products/<int:key>/", methods=['GET', 'PUT', 'DELETE'])
def products_detail(key):
    """
    Retrieve, update or delete note instances.
    """
    if request.method == 'PUT':
        note = str(request.data.get('text', ''))
        products[key] = note
        return note_repr(key)

    elif request.method == 'DELETE':
        products.pop(key, None)
        return '', status.HTTP_204_NO_CONTENT

    # request.method == 'GET'
    if key not in products:
        raise exceptions.NotFound()
    return note_repr(key)




if __name__ == "__main__":
    app.run(debug=True, port=5000)