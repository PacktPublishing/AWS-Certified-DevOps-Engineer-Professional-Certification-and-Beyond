ARG REPO_LOCATION=public.ecr.aws/ubuntu/
FROM public.ecr.aws/ubuntu/ubuntu:latest
COPY . /app
WORKDIR /app
RUN apt-get update -y
RUN apt-get install -y python-3 pip python-dev build-essential git 
RUN pip3 install flask 
EXPOSE 5001 
ENTRYPOINT [ "python3" ]
CMD [ "flask.py"]
