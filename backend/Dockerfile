FROM python:3.8

LABEL maintainer "Patrick Keller kazefreedom@gmx.at"

WORKDIR /backend

COPY . .

RUN chmod +x start.sh && \
    pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "src/main.py" ]
