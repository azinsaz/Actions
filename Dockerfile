FROM python:3.10 AS builder

RUN apt-get update && apt-get install -y && rm -rf /var/lib/apt/lists/*

RUN python -m venv /venv
ENV PATH=/venv/bin:$PATH

WORKDIR /Dice

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "./main.py"]