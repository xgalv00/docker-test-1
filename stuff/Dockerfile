FROM joyzoursky/python-chromedriver:3.6-selenium

COPY . /usr/src/app
WORKDIR /usr/src/app
RUN pip install -r requirements.txt
CMD ["bash", "run_server.sh"]
