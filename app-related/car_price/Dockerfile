FROM amazonlinux:latest
RUN yum -y update
RUN yum install -y python3-pip
RUN pip3 install scikit-learn==0.24.0
RUN pip3 install flask
RUN pip3 install boto3
COPY ./handler_car_price.py handler_car_price.py
COPY ./car_price_rf_model.pkl car_price_rf_model.pkl
EXPOSE 5000
ENTRYPOINT [ "python3" ]
CMD [ "handler_car_price.py" ]



