FROM python:3.8

LABEL maintainer "Patrick Keller kazefreedom@gmx.at"

WORKDIR /backend

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
# RUN chmod +x start.sh

ENTRYPOINT [ "python" ]
CMD [ "src/main.py" ]
