FROM svizor/zoomcamp-model:3.10.12-slim

#need to change it to same with laptop later

RUN pip install pipenv

WORKDIR /app
COPY ["Pipfile", "Pipfile.lock", "./"] 

#./ mean current directory

RUN pipenv install --system --deploy
# --system --deploy need to make virtual environtment and install

COPY ["q6_predict.py", "model1.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["waitress-serve", "--listen=0.0.0.0:9696", "q6_predict:app"]