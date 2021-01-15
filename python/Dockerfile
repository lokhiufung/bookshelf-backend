FROM ubuntu:18.04
RUN apt-get update
RUN apt-get install -y software-properties-common vim
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv && apt-get install -y git
RUN python3.6 -m pip install pip --upgrade && python3.6 -m pip install wheel

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
WORKDIR /python
COPY .  .
RUN pip3.6 install -r requirements.txt
CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8000", "run:app"]