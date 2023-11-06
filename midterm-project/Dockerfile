FROM python:3.10-slim

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "model.bin", "dv.bin", "predict.py", "./"] 

RUN pipenv install --system --deploy

EXPOSE 9696

ENTRYPOINT [ "waitress-serve", "--port=9696", "predict:app" ]