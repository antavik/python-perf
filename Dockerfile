FROM python:3.9-slim

COPY ./test.py /

CMD ["python", "test.py"]