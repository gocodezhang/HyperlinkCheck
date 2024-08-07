FROM public.ecr.aws/lambda/python:3.9 AS build
RUN yum install -y unzip && \
    curl -Lo "/tmp/chromedriver-linux64.zip" "https://storage.googleapis.com/chrome-for-testing-public/127.0.6533.88/linux64/chromedriver-linux64.zip" && \
    curl -Lo "/tmp/chrome-linux64.zip" "https://storage.googleapis.com/chrome-for-testing-public/127.0.6533.88/linux64/chrome-linux64.zip" && \
    unzip /tmp/chromedriver-linux64.zip -d /opt/ && \
    unzip /tmp/chrome-linux64.zip -d /opt/


FROM public.ecr.aws/lambda/python:3.9
# set up chrome browser
RUN yum install -y atk cups-libs gtk3 libXcomposite alsa-lib \
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

CMD ["verify_links.handler"]