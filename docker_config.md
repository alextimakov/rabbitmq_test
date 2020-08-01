first step is to run rabbitmq itself  
```shell script
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3-management
sudo rabbitmqctl list_queues
```

in case error upon 'already busy port 5672' pops up:
```shell script
# find process on needed port
netstat -tlpn | grep .*5672
kill -9 pid
```