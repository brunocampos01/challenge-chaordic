# Challenge Chaordic

### About
Parte01 - API de produtos

### Requirements
- Python 3.6 ou superior:<br/>
`sudo apt-get install python3.6`
- pip:<br/>
`sudo apt-get install python-pip`
- Bibliotecas:<br/>
`pip install -r requirements.txt`<br/>
- Curl:<br/>
`sudo apt-get -y install curl`
- Git:<br/>
`sudo apt-get install git`

**OBS:** o ambiente tambem foi dockerizado

## API
Decidi usar Flask (Python) porque ele é um microframework, o que garante que terei somente o essencial para rodar um método post na API.

### Running 
1. Abra o terminal e clone o repositório: <br/>
```
git clone https://github.com/brunocampos01/challenge-chaordic; \
cd challenge-chaordic/part_1/src
```

2. Instale as bibliotecas necessárias:<br/>
`pip install -r requirements.txt `

2. Execute o arquivo part_1.py para inicializar o servidor:<br/>
`python3 part_1.py`<br/>

3. Execute **testes** de requisição (POST) na aplicação,
- com testes automatizados:<br/>
```
cd challenge-chaordic/part_1/test; \
python3 tests.py
```

- a partir de um outro terminal:</br>
`curl -XPOST http:/127.0.0.1:5000/chaordic.com.br/v1/products/ -d '[{"id": "123", "name": "mesa"}]'`<br/>

## Deploy
#### Dependences
- O desenvolvimento da aplicação foi feito no *virtual environment* do Python. No término do desenvolvimento, salvei todos os requeriments utilizados no arquivo *requeriments.txt*
#### Containers
O ambiente foi dockerizado afim de garantir a uniformidade e facilitar a clusterização.
- Docker install:<br/>
`sudo apt-get install docker.io`<br/>

- Build container (Dockerfile):<br/>
`sudo docker build -t part_1 .`<br/>

- Run container:<br/>
`sudo docker run -d -p 5000:5000 part_1`<br/>

---

#### Author
<a href="mailto:brunocampos01@gmail.com" target="_blank"><img class="" src="https://github.com/brunocampos01/devops/blob/master/images/gmail.png" width="28"></a>
<a href="https://github.com/brunocampos01" target="_blank"><img class="ai-subscribed-social-icon" src="https://github.com/brunocampos01/devops/blob/master/images/github.png" width="30"></a>
<a href="https://www.linkedin.com/in/brunocampos01/" target="_blank"><img class="ai-subscribed-social-icon" src="https://github.com/brunocampos01/devops/blob/master/images/linkedin.png" width="30"></a>
Bruno Aurélio Rôzza de Moura Campos 

---

#### Copyright
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br/>


