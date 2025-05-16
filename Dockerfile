FROM apache/airflow:2.10.3
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install psycopg2-binary --no-cache-dir
RUN pip install -r requirements.txt