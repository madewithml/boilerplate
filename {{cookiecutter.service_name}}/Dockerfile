# ==============================================================================
# 🐳 Dockerfile
# ------------------------------------------------------------------------------
FROM ubuntu:16.04
# FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04 for CUDA9.0
LABEL maintainer="practicalAI <learnpracticalai.com>" \
      version="1.0"

# ==============================================================================
# 🚀 Initialize
# ------------------------------------------------------------------------------
ENV APT_INSTALL "apt-get install -y --no-install-recommends"
ENV PIP_INSTALL "pip3.6 --no-cache-dir install --upgrade"
RUN rm -rf /var/lib/apt/lists/* \
           /etc/apt/sources.list.d/cuda.list \
           /etc/apt/sources.list.d/nvidia-ml.list && \
    apt-get update

# ==============================================================================
# ⚙️ Tools
# ------------------------------------------------------------------------------
RUN DEBIAN_FRONTEND=noninteractive $APT_INSTALL \
        build-essential \
        ca-certificates \
        cmake \
        locales \
        curl \
        wget \
        git \
        vim

# ==============================================================================
# 🐍 Python
# ------------------------------------------------------------------------------
RUN DEBIAN_FRONTEND=noninteractive $APT_INSTALL \
        software-properties-common \
        && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    DEBIAN_FRONTEND=noninteractive $APT_INSTALL \
        python3.6 \
        python3.6-dev \
        && \
    wget https://bootstrap.pypa.io/get-pip.py && \
    python3.6 get-pip.py && \
    $PIP_INSTALL \
        pip==18.1 \
        setuptools

# ==============================================================================
# 🛁 Clean up
# ------------------------------------------------------------------------------
RUN ldconfig && \
    apt-get clean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/* /tmp/* ~/*

# ==============================================================================
# 🚢 Ports
# ------------------------------------------------------------------------------
EXPOSE 5000

# ==============================================================================
# 📖 {{cookiecutter.service_name}}
# ------------------------------------------------------------------------------
COPY src/ $PWD/src/
WORKDIR $PWD/src/
RUN python3.6 setup.py develop
CMD /usr/bin/python3.6 /usr/local/bin/gunicorn --log-level ERROR --workers 4 --timeout 60 --bind 0.0.0.0:5000 --access-logfile - --error-logfile - --reload wsgi
