FROM ubuntu
USER root

WORKDIR /usr/local/
ADD src ./src
ADD InstallServer.sh .
ADD pom.xml .

# Install OpenJDK-8
RUN apt-get update && apt-get install -y openjdk-8-jdk && apt-get install -y ant && apt-get clean
    
# Fix certificate issues
RUN apt-get install ca-certificates-java && apt-get clean && update-ca-certificates -f

# Setup JAVA_HOME -- useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

#Download Maven
RUN apt install -y maven

#Flush on stdout all the prints
ENV  PYTHONUNBUFFERED=1

CMD ["bash", "./InstallServer.sh"]
CMD ["sh", "-c", "mvn clean verify ; mvn exec:java -Dexec.mainClass='Consumer'"]
