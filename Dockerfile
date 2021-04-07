# We're using Ubuntu 20.10
FROM ximfine/remix:buster

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y
RUN pip3 install -U pip
RUN curl -sL https://deb.nodesource.com/setup_15.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm

RUN git clone -b Beta https://github.com/ximfine/Xbot-Remix /home/xnewbie/
RUN mkdir /home/xnewbie/bin/
WORKDIR /home/xnewbie/

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/ximfine/XBot-Remix/Beta/requirements2.txt

CMD ["python3","-m","userbot"]
