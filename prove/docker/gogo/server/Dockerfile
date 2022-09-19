FROM ubuntu
USER root

WORKDIR /usr/local/
ADD go.mod .
ADD go.sum .
ADD proto ./proto
ADD gen ./gen
ADD MicroServer.go .

# Update and upgrade repo
RUN apt-get update -y -q && apt-get upgrade -y -q 

# Install tools we might need
RUN DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y -q curl build-essential ca-certificates git 

# Download Go 1.18.5 and install it to /usr/local/go
RUN curl -s https://storage.googleapis.com/golang/go1.18.5.linux-amd64.tar.gz| tar -v -C /usr/local -xz

# Download protobuf-compiler
RUN apt install -y protobuf-compiler

# Let's people find our Go binaries
ENV PATH $PATH:/usr/local/go/bin
ENV GO $GO:/usr/local/go

EXPOSE 50051
CMD ["go", "run", "./MicroServer.go"]
