# docker build -t sudeeppatel/dockerizing-django-rest-framework-app .

FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code
WORKDIR /code

# COPY startup script into known file location in container
COPY start.sh /start.sh
# EXPOSE port 8000 to allow communication to/from server
EXPOSE 8000
RUN chmod +x /start.sh
# CMD specifcies the command to execute to start the server running.
CMD ["/start.sh"]
# done!
