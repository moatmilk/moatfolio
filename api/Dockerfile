FROM python:3.9

WORKDIR /myapi

COPY . .

RUN pip install "fastapi[standard]"

RUN pip install --no-cache-dir --upgrade -r requirements.txt

#CMD ["uvicorn", "api:main.app", "--host", "0.0.0.0", "--port", "80"]

CMD ["fastapi", "run", "./main.py", "--port", "80"]
