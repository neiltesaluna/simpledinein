FROM python:latest
WORKDIR /app
COPY setup.sh setup.sh
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt 
COPY simpledinein/ .
EXPOSE 8000
ENTRYPOINT [ "./setup.sh" ]