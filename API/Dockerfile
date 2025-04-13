#docker build -t juan-chatbot .  
#docker run juan-chatbot

FROM python:3.12

WORKDIR /
EXPOSE 8051

#COPY data ./data
COPY . .
RUN pip install --no-cache-dir -r requirements.txt


# Set the command to run your script
ENTRYPOINT ["python", "app.py"]