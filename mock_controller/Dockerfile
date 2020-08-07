FROM python:3
RUN mkdir /app

COPY mock_controller.py /app

RUN pip install autobahn[asyncio,serialization]

CMD python3 /app/mock_controller.py