FROM mcr.microsoft.com/mssql/server:2019-latest

# Use root user
USER root

# Initial update and install
RUN apt-get update && \
    apt-get -y install sudo && \
    apt-get -y install curl

# Project files
ARG PROJECT_DIR=/srv/db-sql-server
RUN sudo mkdir -p $PROJECT_DIR
WORKDIR $PROJECT_DIR
COPY ./init/ ./

# Grant permissions for scripts to be executable
RUN chmod +x $PROJECT_DIR/entrypoint.sh
RUN chmod +x $PROJECT_DIR/setup.sh

# SQL Restore Setup
RUN mkdir /var/opt/mssql/backup
RUN cd ~
RUN curl -L -o wwi.bak 'https://github.com/Microsoft/sql-server-samples/releases/download/wide-world-importers-v1.0/WideWorldImporters-Full.bak'
RUN cp wwi.bak /var/opt/mssql/backup

CMD ["/bin/bash", "entrypoint.sh"]