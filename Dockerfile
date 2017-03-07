FROM python:alpine

COPY script.py /

RUN mkdir /output

VOLUME /output

CMD [ "python", "script.py" ]
