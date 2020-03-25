FROM python:3
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
COPY database_setup.py .
CMD [ "python", "app.py" ]
