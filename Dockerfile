FROM python:3-alpine

ARG VERSION=3.0.6

RUN mkdir /var/lib/radicale
VOLUME /var/lib/radicale
COPY startmail.py .
COPY radicale.cfg .
EXPOSE 5232
ENV PYTHONPATH=.
CMD ["radicale", "--hosts", "0.0.0.0:5232,[::]:5232", "--config", "radicale.cfg"]

RUN apk add --no-cache ca-certificates openssl
RUN pip install --no-cache-dir "https://github.com/Kozea/Radicale/archive/${VERSION}.tar.gz"
