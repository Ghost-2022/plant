FROM python:3.9.16-slim-bullseye

COPY model/classification/requirements.txt /code/plant/requirements.txt
WORKDIR /code/plant/
RUN pip install --no-cache-dir -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

CMD [ "bash" ]