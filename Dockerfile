FROM ubuntu

RUN apt-get update && apt-get install -y python3 x11vnc xvfb python3-tk
RUN mkdir ~/.vnc
RUN x11vnc -storepasswd 1234 ~/.vnc/passwd
RUN bash -c 'echo "cd /code && read -p Press\\ Enter\\ to\\ start\\ the\\ game. && python3 main.py" >> /.bashrc'

ENV HOME=/
CMD x11vnc -forever -usepw -create
