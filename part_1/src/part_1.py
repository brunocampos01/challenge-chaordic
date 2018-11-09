import datetime
from flask import Flask, request
from flask_api import FlaskAPI, status

# flask object
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

        if data in datas_registered:
            # armazena a posição na lista do data, quando ele foi armazenado pela última vez
            position = len(datas_registered)-datas_registered[::-1].index(data)-1
            # diferença entre o minuto atual e o minuto da ultima vez que esse dado apareceu na lista
            difference = minute - times_registered[position]
            
            if difference <=10:
                print('Forbidden')
                return f"{status.HTTP_403_FORBIDDEN} Forbidden\n\n{times_registered}\n{datas_registered}\nposition_data={position}\nminute={minute}\ndifference={difference}\n" 
            else:
                datas_registered.append(data)
                times_registered.append(minute)
                return f"{status.HTTP_201_CREATED} OK\n (difference > 1)\n\n{times_registered}\n{datas_registered}\nposition_data={position}\nminute={minute}\ndifference={difference}\n"
        else:
            datas_registered.append(data)
            times_registered.append(minute)
        return f"{status.HTTP_201_CREATED} OK\n (data not in)\n{times_registered}\n{datas_registered}\n"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
