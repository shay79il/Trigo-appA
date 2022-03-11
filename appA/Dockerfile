FROM python:3.8.3-alpine

RUN adduser -D app
USER app

WORKDIR /home/app

ENV PATH="/home/app/.local/bin:${PATH}"
RUN /usr/local/bin/python -m pip install --upgrade pip

ENV PATH="/usr/local/bin/python:${PATH}"
RUN pip install --user --no-cache-dir flask

COPY --chown=app:app app-a.py /home/app/

CMD [ "python", "/home/app/app-a.py" ]