FROM python

WORKDIR /src/app/ykingboos/pinterest-video-info

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "__init__.py"]