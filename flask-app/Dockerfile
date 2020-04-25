FROM python:3.8.2-alpine

WORKDIR /project

ADD . /project

RUN apk update
RUN apk add gcc libc-dev g++ libffi-dev libxml2 unixodbc-dev mariadb-dev postgresql-dev
RUN wget https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/msodbcsql17_17.5.1.1-1_amd64.apk && \
    wget https://download.microsoft.com/download/e/4/e/e4e67866-dffd-428c-aac7-8d28ddafb39b/mssql-tools_17.5.1.1-1_amd64.apk && \
    apk add --allow-untrusted msodbcsql17_17.5.1.1-1_amd64.apk && \
    apk add --allow-untrusted mssql-tools_17.5.1.1-1_amd64.apk
RUN pip install -r requirements.txt

CMD ["python","app.py"]