FROM python:3.12.6

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./ /code/

CMD ["fastapi", "run", "main.py", "--port", "5001"]