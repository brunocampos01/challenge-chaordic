# Challenge Chaordic

## API
Descidi usar Flask (Python) porque ele é um microframework, o que garante que terei somente o essencial para rodar a API.

#### Run art-1
`python3 part-1.py`<br/>
**OBS:** não alcancei a melhor solução. A negação de request ocorre a partir da análise da última request armazenada.

#### Test
`curl -XPOST http:/127.0.0.1:5000/chaordic.com.br/v1/products/ -d '[{"id": "123", "name": "mesa"}]'`

## Deploy
#### Dependences
- O desenvolvimento da aplicação foi feito no *virtual environment* do Python. No término do desenvolvimento, salvei todos os requeriments utilizados no arquivo *requeriments.txt*
#### Containers
- Build container (Dockerfile):<br/>
`sudo docker build -t part-1 .`<br/>

- Run container:<br/>
`sudo docker run -d -p 5000:5000 part-1`<br/>

## Cluster
- Mesos



