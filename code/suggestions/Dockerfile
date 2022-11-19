FROM ubuntu
USER root

WORKDIR /app
COPY . .
COPY ./credentials /root/.aws/

# Install OpenJDK-8
RUN apt-get update && apt-get install -y openjdk-8-jdk && apt-get install -y ant && apt-get clean
    
# Fix certificate issues
RUN apt-get update && apt-get install ca-certificates-java && apt-get clean && update-ca-certificates -f

# Setup JAVA_HOME -- useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

#Download Maven
RUN apt-get update && apt install -y maven

# Download protobuf-compiler
RUN apt-get update && apt install -y protobuf-compiler

# Mi consente di poter utilizzare il comando DIG per risolvere gli indirizzi IP necessari.
RUN apt-get install -y dnsutils

# Devo modificare i permessi di accesso per poter eseguire il file bash
RUN chmod a+x setup.sh

EXPOSE 50054

# Lancio il file di configurazione.
CMD ["./setup.sh"]
#CMD ["sh", "-c", "mvn clean verify ; mvn exec:java -Dexec.mainClass='control.Suggestions'"]
