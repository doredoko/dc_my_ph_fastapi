FROM python:3.11-buster

# 
WORKDIR /src

# 
COPY ./requirements.txt /src/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

# 
COPY ./api /src/api

# 
CMD ["uvicorn", "api.main:app", "--host","0.0.0.0","--reload"]
