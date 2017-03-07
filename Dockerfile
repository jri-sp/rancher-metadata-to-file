FROM python:alpine

COPY script.py /

CMD [ "python", "script.py" ]
