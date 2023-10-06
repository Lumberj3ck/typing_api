FROM python

WORKDIR /app

COPY . .

EXPOSE 8000

RUN python -m venv venv && \
    /bin/bash -c "source venv/bin/activate" && \
    pip install -r requirements.txt

RUN python manage.py collectstatic

# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]