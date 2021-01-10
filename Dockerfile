FROM alpine:3.12.3 as builder

WORKDIR /opt

ADD https://github.com/cortesi/modd/releases/download/v0.8/modd-0.8-linux64.tgz .
RUN tar xvf modd-0.8-linux64.tgz

FROM python:3.9.1-slim

WORKDIR /opt

COPY --from=builder /opt/modd-0.8-linux64/modd /usr/local/bin/

CMD ["modd"]
