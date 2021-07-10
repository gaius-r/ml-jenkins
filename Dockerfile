FROM centos

RUN yum install python36 -y

RUN pip3 install numpy

RUN pip3 install joblib

RUN pip3 install scikit-learn

COPY fiftystartups_model.pk1 /

COPY startup_code.py /

CMD python3 startup_code.py

