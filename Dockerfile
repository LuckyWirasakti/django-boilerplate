FROM python:slim-bullseye

LABEL maintainer="lucky.wirasakti@icloud.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /home/core/
RUN pip install --upgrade pip
RUN pip install -r /home/core/requirements.txt

RUN useradd -ms /bin/bash core
RUN chown -R core:core /home/core/

USER core
WORKDIR /home/core/

ENTRYPOINT ["sh", "entrypoint.sh"]