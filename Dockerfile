FROM alpine:latest
RUN echo "Hello form docker Build from jenkins!" > /message.txt
CMD cat /message.txt

