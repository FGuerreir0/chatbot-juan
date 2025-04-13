#docker build -t juan .  
#docker run -d -p 8051:8051 juan
#docker run juan
#Request: http://localhost:8051/juan/chat

FROM python:3.12

WORKDIR /API
EXPOSE 8051

#COPY data ./data
COPY . .
RUN pip install --no-cache-dir -r requirements.txt


# Set the command to run your script
ENTRYPOINT ["python", "app.py"]