FROM python
WORKDIR /src
RUN pip install flask
RUN pip install reverse_geocode
COPY . .
CMD ["python","app.py"]
EXPOSE 5000
