FROM python:3.8

LABEL maintainer "Patrick Keller kazefreedom@gmx.at"

WORKDIR /backend

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT [ "python" ]
CMD [ "src/main.py" ]
