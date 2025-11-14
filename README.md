# Инструкция по запуску

Выполнять команду нужно из корня проекта
```bash
docker-compose up
```

1. docker: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. 
Is the docker daemon running? permission denied
2. docker: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
permission denied
3. permission denied while trying to connect to the Docker daemon socket

Если при запуске выводится любой из этих ответов, то можно использовать 

```bash
sudo docker-compose up
```

Если версия Docker 20.10+, то docker-compose входит в основной CLI Docker, 
тогда можно использовать команду: 

```bash
docker compose up
```

или если нет прав доступа:

```bash
sudo docker compose up
```
