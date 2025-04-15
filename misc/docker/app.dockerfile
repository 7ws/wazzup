FROM python:3.12
WORKDIR /app

# Não acumula saída de terminal do Python, exibe imediamente
ENV PYTHONUNBUFFERED=1

# Não cria arquivos de cache (__pycache__)
ENV PYTHONDONTWRITEBYTECODE=1

# Install Python packages
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Bundle the application
COPY . /app/
