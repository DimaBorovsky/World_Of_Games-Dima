FROM python:3-alpine
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
COPY Scores.txt /Scores.txt
ENV FLASK_APP=Main_Scores.py
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]


