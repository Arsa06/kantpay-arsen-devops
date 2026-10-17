FROM python:3.12-slim
WORKDIR /app
COPY app/ /app/
RUN echo "Preparing application..."
EXPOSE 8088
CMD ["python3", "app.py"]
