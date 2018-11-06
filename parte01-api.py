from flask import Flask, request
from flask_api import FlaskAPI, status
from time import sleep
import datetime

# create the flask object
app = Flask(__name__)

# saved json and time
datas_registered = []
times_registered = []
datas_split = []
times_split = []

@app.route('/chaordic.com.br/v1/products/', methods=['POST'])
def post_route():
    if request.method == 'POST':
        # get json
        data = request.get_json(force=True)
        # get time 
        minute = datetime.datetime.now().minute
        
        # 
        buffer_10min()

        if data in datas_split:
            return f"{status.HTTP_403_FORBIDDEN} Forbidden\n "
        else:
            datas_registered.append(data)
            times_registered.append(minute)
        return f"{status.HTTP_201_CREATED} OK\ndatas={datas_registered}\ndatas_split={datas_split}\ntimes={times_registered}\n"


def buffer_10min():
    # percorre times_registered
    for i in times_registered: 
        index_decr = (len(times_registered) - times_registered.index(i)) - 1 # -1 pois index começa com 0
        elem_atual = times_registered[index_decr]
        elem_ultimo = times_registered[-1]
        diferenca = elem_ultimo - elem_atual

        # ultimos 10 min 
        if diferenca < 1:
            times_split.append(elem_atual)
            datas_split.append(datas_registered[index_decr])
        else:
            times_split.pop(index_decr)
            datas_split.pop(index_decr)
            break # garante que não vai comparar todos os elementos
                   



if __name__ == "__main__":
    app.run(debug=True, port=5000)