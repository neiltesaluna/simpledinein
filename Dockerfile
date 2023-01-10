FROM python:latest
WORKDIR /app
COPY setup.sh setup.sh
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt 
EXPOSE 8000
# Comment out lines below for local development
COPY simpledinein/ .
ENTRYPOINT [ "./setup.sh" ]