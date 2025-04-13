FROM python:3.12

WORKDIR /API
EXPOSE 8051

#COPY data ./data
COPY . .
RUN pip install --no-cache-dir -r requirements.txt


# Set the command to run your script
ENTRYPOINT ["python", "app.py"]