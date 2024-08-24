FROM python:3.8-slim

WORKDIR /app
COPY . /app

RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt


CMD ["python", "Strong_Password.py"]