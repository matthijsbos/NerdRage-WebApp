FROM matthijsbos/nerdrage-base
WORKDIR /usr/src/app
ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONUNBUFFERED 1

# install dependencies 
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
               python3-dev \
               build-essential \
    # minimize image
    && rm -rf ~/.cache \
    && rm -rf /var/lib/apt/lists/*


COPY ./requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python3", "./NerdRageServer.py" ]
