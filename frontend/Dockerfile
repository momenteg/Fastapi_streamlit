FROM python:3.8-slim


WORKDIR /code
COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./ /code/frontend/

EXPOSE 8501

CMD ["streamlit", "run", "frontend/streamlit.py"]