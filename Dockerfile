# We're using Ubuntu 20.10
FROM ximfine/xproject:buster

#
# Clone repo and prepare working directory
#
RUN git clone -b sql-extended https://github.com/ximfine/Xbot-Remix /home/xnewbie/
RUN mkdir /home/xnewbie/bin/
WORKDIR /home/xnewbie/

# Upgrade pip
# RUN pip install --upgrade pip

RUN cp sample_config.env userbot/config.env

#Install python requirements
# RUN pip3 install -r https://raw.githubusercontent.com/ximfine/XBot-Remix/sql-extended/requirements.txt

EXPOSE 80 443

CMD ["python3","-m","userbot"]
