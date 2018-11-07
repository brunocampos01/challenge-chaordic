from flask import Flask, request
from flask_api import FlaskAPI, status
import datetime

# create flask object
app = Flask(__name__)

# saved json and time
datas_registered = []
times_registered = []

@app.route('/chaordic.com.br/v1/products/', methods=['POST'])
def post_route():
    if request.method == 'POST':
        # get json
        data = request.get_json(force=True)
        # get time 
        minute = datetime.datetime.now().minute

        # se times_split empty 
        if len(times_registered) == 0:
            times_registered.append(minute)
            datas_registered.append(data)
            return f"{status.HTTP_201_CREATED} OK\ndatas_split={datas_registered}\n\ntimes_split={times_registered}\n"
        
        # get diferença de tempo, entre o ultimo elemento na lista com o min atual
        diferenca = minute - times_registered[-1]

        '''
        Ainda não é a melhor solução, neste caso esta havendo o bloqueio da última transação
        e não somente da request que tem um mesmo json
        '''

        if data in datas_registered and diferenca < 1 :
            return f"{status.HTTP_403_FORBIDDEN} Forbidden\n"
        elif data in datas_registered and diferenca > 1:
            datas_registered.append(data)
            times_registered.append(minute)
            return f"{status.HTTP_201_CREATED} OK\n\ndatas_split={datas_registered}\n\ntimes_split={times_registered}\n"
        else:
            datas_registered.append(data)
            times_registered.append(minute)
        return f"{status.HTTP_201_CREATED} OK\n\ndatas_split={datas_registered}\n\ntimes_split={times_registered}\n"


if __name__ == "__main__":
    app.run(debug=True, port=5000)