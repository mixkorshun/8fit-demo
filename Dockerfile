FROM python:3.6

ENV SECRET_KEY=build
ENV BASE_URL=eightfit.loc

COPY ./requirements.txt /code/requirements.txt
RUN pip install -r /code/requirements.txt

RUN apt-get update && apt-get install -y netcat

COPY . /code/
WORKDIR /code/

RUN python manage.py collectstatic --no-input

RUN useradd wagtail
RUN chown -R wagtail /code
USER wagtail

EXPOSE 8000
ENTRYPOINT [ "/code/docker-entrypoint.sh" ]
CMD [ "start" ]
