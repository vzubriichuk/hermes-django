###########
# BUILDER #
###########

FROM python:3.9-slim-bullseye

# set work directory
WORKDIR /home/app/web

# Set environment variables
ENV HTTP_PROXY "http://proxy.fozzy.lan:3128"
ENV HTTPS_PROXY "http://proxy.fozzy.lan:3128"
ENV http_proxy "http://proxy.fozzy.lan:3128"
ENV https_proxy "http://proxy.fozzy.lan:3128"
ENV PYMSSQL_BUILD_WITH_BUNDLED_FREETDS=1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# установка зависимостей psycopg2, pyodbc, pymssql
RUN apt-get update \
    && apt-get install -y curl postgresql-13 postgresql-client-13 gcc gnupg musl-dev g++ unixodbc-dev freetds-dev freetds-bin tdsodbc

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get install -y msodbcsql17
RUN apt-get install -y libgssapi-krb5-2


# установка зависимостей
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . . 