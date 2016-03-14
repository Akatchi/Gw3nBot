FROM java:8u72-jdk

RUN curl -o mvn.tar.gz "http://www.eu.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz" &&\
	tar xzvf mvn.tar.gz &&\
	mv apache-maven-3.3.9 mvn &&\
	rm mvn.tar.gz

WORKDIR /usr/src/app

ENTRYPOINT scripts/entrypoint.sh