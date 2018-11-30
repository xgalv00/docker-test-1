FROM python:3.6.1-onbuild

COPY . /usr/src/app
RUN aapt-get update
CMD ["python", "server.py"]
