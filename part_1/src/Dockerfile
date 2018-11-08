FROM ubuntu:latest
MAINTAINER brunocampos "brunocampos01@gmail.com"

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

COPY . /part-1
WORKDIR /part-1
# requirements.txt primeiro é levado para o Docker cache
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["part-1.py"]