FROM python:3.9-slim
WORKDIR /home/data
RUN mkdir -p /home/data/output
COPY scripts.py /home/scripts.py
CMD ["python", "/home/scripts.py"]