FROM debian:10

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get dist-upgrade -y && \
    apt-get install --no-install-recommends -y \
            autoconf \
            automake \
            autopoint \
            bash \
            bash-completion \
            ca-certificates \
            ccache \
            chrony \
            cpanminus \
            gcc \
            gdb \
            gettext \
            git \
            libc6-dev \
            libtool \
            libtool-bin \
            libvirt-dev \
            libxml2-dev \
            libxml2-utils \
            locales \
            lsof \
            make \
            net-tools \
            ninja-build \
            patch \
            perl \
            php-dev \
            php-imagick \
            pkgconf \
            python3 \
            python3-pip \
            python3-setuptools \
            python3-wheel \
            screen \
            strace \
            sudo \
            vim \
            xsltproc \
            xz-utils && \
    apt-get autoremove -y && \
    apt-get autoclean -y && \
    sed -Ei 's,^# (en_US\.UTF-8 .*)$,\1,' /etc/locale.gen && \
    dpkg-reconfigure locales && \
    mkdir -p /usr/libexec/ccache-wrappers && \
    ln -s /usr/bin/ccache /usr/libexec/ccache-wrappers/cc && \
    ln -s /usr/bin/ccache /usr/libexec/ccache-wrappers/$(basename /usr/bin/gcc)

RUN pip3 install \
         meson==0.54.0

ENV LANG "en_US.UTF-8"

ENV MAKE "/usr/bin/make"
ENV NINJA "/usr/bin/ninja"
ENV PYTHON "/usr/bin/python3"

ENV CCACHE_WRAPPERSDIR "/usr/libexec/ccache-wrappers"
