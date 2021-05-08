FROM python:3.9
COPY ./web /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["worker.py"]
