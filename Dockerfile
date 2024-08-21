FROM fedora:36 AS build
RUN dnf install -y unzip && \
    curl -Lo "/tmp/chromedriver-linux64.zip" "https://storage.googleapis.com/chrome-for-testing-public/127.0.6533.89/linux64/chromedriver-linux64.zip" && \
    curl -Lo "/tmp/chrome-linux64.zip" "https://storage.googleapis.com/chrome-for-testing-public/127.0.6533.89/linux64/chrome-linux64.zip" && \
    unzip /tmp/chromedriver-linux64.zip -d /opt/ && \
    unzip /tmp/chrome-linux64.zip -d /opt/


FROM fedora:36

RUN dnf update -y
# set up chrome browser
RUN dnf install -y atk cups-libs gtk3 libXcomposite alsa-lib \
    libXcursor libXdamage libXext libXi libXrandr libXScrnSaver \
    libXtst pango at-spi2-atk libXt xorg-x11-server-Xvfb \
    xorg-x11-xauth dbus-glib dbus-glib-devel nss mesa-libgbm \
    python3.12 python3-pip

COPY --from=build /opt/chrome-linux64 /opt/chrome
COPY --from=build /opt/chromedriver-linux64 /opt/

WORKDIR /app
# copy dependency file
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

ENV ENV_VAR=development
# copy code src
COPY ./src ./src

# copy models
COPY ./models ./models

# copy lambda
COPY main.py .


# ENTRYPOINT ["xvfb-run", "--server-args=-screen 0 1900x1200x24"]
EXPOSE 8000

CMD ["fastapi", "run", "main.py"]