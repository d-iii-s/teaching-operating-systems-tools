FROM mffd3s/nswi004-base:latest

# Enable our Copr repository
RUN dnf copr enable -y d3s/teaching

# Install cross-compiler toolchain
RUN dnf install -y mff-nswi004-binutils-mipsel-linux-gnu mff-nswi004-gcc-mipsel-linux-gnu

CMD echo "Run with -it /bin/bash and proper volume mounted"
