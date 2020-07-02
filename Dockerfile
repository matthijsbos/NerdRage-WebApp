FROM matthijsbos/nerdrage-base
WORKDIR /usr/src/app
COPY ./requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python3", "./NerdRageServer.py" ]
