# Challenge Chaordic

### About
Parte01 - API de produtos

### Pre Requirements:
- Python 3.6 ou superior:<br/>
`sudo apt-get install python3.6`
- Git:<br/>
`sudo apt-get install git`
- pip:<br/>
`sudo apt-get install python-pip`
- Bibliotecas:<br/>
`pip install -r requirements.txt`<br/>

**OBS:** o ambiente tambem foi dockerizado

## API
Decidi usar Flask (Python) porque ele é um microframework, o que garante que terei somente o essencial para rodar um método post na API.

### Running 
1. Abra o terminal e clone o repositório: <br/>
`git clone https://github.com/brunocampos01/challenge-chaordic`<br/>
`cd challenge-chaordic/part_1/src`
2. Execute o arquivo part_1.py para inicializar o servidor:<br/>
`python3 part_1.py`<br/>
**OBS:** não alcancei a melhor solução. A negação de request ocorre a partir da análise da última request armazenada.

3. Execute testes de requisição (POST) na aplicação,
- com testes automatizados:<br/>
`cd challenge-chaordic/part_1/src`<br/>
`python3 tests.py`<br/>

- a partir de um outro terminal:</br>
`curl -XPOST http:/127.0.0.1:5000/chaordic.com.br/v1/products/ -d '[{"id": "123", "name": "mesa"}]'`<br/>

## Deploy
#### Dependences
- O desenvolvimento da aplicação foi feito no *virtual environment* do Python. No término do desenvolvimento, salvei todos os requeriments utilizados no arquivo *requeriments.txt*
#### Containers
O ambiente foi dockerizado afim de garantir a uniformidade e facilitar a clusterização.
- Build container (Dockerfile):<br/>
`sudo docker build -t part_1 .`<br/>

- Run container:<br/>
`sudo docker run -d -p 5000:5000 part_1`<br/>



