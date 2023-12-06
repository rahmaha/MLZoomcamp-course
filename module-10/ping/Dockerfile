FROM python:3.10-slim
#need to change it to same with laptop later

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"] 

#./ mean current directory

RUN pipenv install --system --deploy
# --system --deploy need to make virtual environtment and install

COPY "ping.py" .

EXPOSE 9696

ENTRYPOINT [ "waitress-serve", "--port=9696", "ping:app" ]
