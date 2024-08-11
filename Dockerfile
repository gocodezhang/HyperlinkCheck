FROM public.ecr.aws/lambda/python:3.12 AS build
RUN dnf install -y unzip && \
    curl -Lo "/tmp/chromedriver-linux64.zip" "https://storage.googleapis.com/chrome-for-testing-public/127.0.6533.89/linux64/chromedriver-linux64.zip" && \
    curl -Lo "/tmp/chrome-linux64.zip" "https://storage.googleapis.com/chrome-for-testing-public/127.0.6533.89/linux64/chrome-linux64.zip" && \
    unzip /tmp/chromedriver-linux64.zip -d /opt/ && \
    unzip /tmp/chrome-linux64.zip -d /opt/


FROM public.ecr.aws/lambda/python:3.12
# set up chrome browser
RUN dnf install -y atk cups-libs gtk3 libXcomposite alsa-lib \
    libXcursor libXdamage libXext libXi libXrandr libXScrnSaver \
    libXtst pango at-spi2-atk libXt xorg-x11-server-Xvfb \
    xorg-x11-xauth dbus-glib dbus-glib-devel nss mesa-libgbm

COPY --from=build /opt/chrome-linux64 /opt/chrome
COPY --from=build /opt/chromedriver-linux64 /opt/

# copy dependency file
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# install dependencies
RUN pip install -r requirements.txt

# copy code src
COPY ./src ${LAMBDA_TASK_ROOT}/src

# copy models
COPY ./models ${LAMBDA_TASK_ROOT}/models

# copy lambda
COPY verify_links.py ${LAMBDA_TASK_ROOT}


# ENTRYPOINT ["xvfb-run", "--server-args=-screen 0 1900x1200x24"]

CMD ["verify_links.handler"]