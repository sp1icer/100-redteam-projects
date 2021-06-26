FROM python:3

# Setting the source where the files will be hosted.
WORKDIR /usr/src/app
COPY . .

# Install Python library dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Listen on port 1337.
EXPOSE 1337

# Run the application.
CMD [ "python", "./server.py" ]