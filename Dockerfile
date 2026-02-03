FROM ubuntu:24.04

# Install Python, pip, git, venv
RUN apt update && apt upgrade -y && \
    apt install -y python3 python3-pip python3-venv git && \
    rm -rf /var/lib/apt/lists/*

# Set working directory and clone repo
WORKDIR /app
RUN git clone https://github.com/rishiakrishnan/simple-calc.git .

# Move to src folder where app.py lives
WORKDIR /app/src

# Create virtual environment and install Flask
RUN python3 -m venv venv
RUN ./venv/bin/pip install --upgrade pip
RUN ./venv/bin/pip install Flask

# Run the app using venv Python
CMD ["./venv/bin/python", "app.py"]

