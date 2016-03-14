FROM ubuntu
 
RUN apt-get update -qq
RUN apt-get install -y build-essential nodejs npm nodejs-legacy vim
  
RUN npm install -g phantomjs grunt-cli grunt bower jasmine-core jasmine karma grunt-karma
RUN npm install
RUN bower install --allow-root

RUN chmod -R a+rwx .
 
EXPOSE 9000
 
CMD ["grunt", "serve"]