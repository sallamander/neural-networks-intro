FROM andrewosh/binder-base

MAINTAINER Andrew Osheroff <andrewosh@gmail.com>

USER root

RUN apt-get update
RUN apt-get install -y git  

USER main

ADD requirements.txt requirements.txt

# Install everything for Python2
RUN pip install https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.10.0-cp27-none-linux_x86_64.whl
RUN pip install -r requirements.txt

# Install everything for Python3
RUN /bin/bash -c "source activate python3 && pip install https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.10.0-cp35-cp35m-linux_x86_64.whl"
RUN /bin/bash -c "source activate python3 && pip install -r requirements.txt"

RUN git clone https://github.com/sallamander/neural-networks-intro.git $HOME/neural-networks-intro
ENV PYTHONPATH="$HOME/neural-networks-intro:$PYTHONPATH"
