FROM cethon1/SourceCethon:slim-buster

#clonning repo 
RUN git clone https://github.com/cethon1/SourceCethon.git /root/SourceCethon 
#working directory 
WORKDIR /root/SourceCethon 

# Install requirements
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/CETHONSOURCE/bin:$PATH"

CMD ["python3","-m","CETHONSOURCE"]
