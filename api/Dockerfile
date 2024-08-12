FROM python:3.12

WORKDIR /myapi

COPY . .

RUN pip install "fastapi[standard]"

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app /code/app

CMD ["fastapi", "run", "./main.py", "--port", "80"]
