# Tweet-Word-Counter

Tweet-Word-Counter is a dockerized python application that collects real time data from Twitter and counts the number of words of tweets posted during a specific amount of time using Apache-Kafka. 
## Installation

Use the guide given below to successfully install and run the application using Docker.

1. Start with installing [Docker](https://www.digitalocean.com/community/tutorials/docker-ubuntu-18-04-1-ru) on your Linux. 

2. After installation is complete, pull the image that we have pushed to [DockerHub](https://cloud.docker.com/repository/registry-1.docker.io/hpc2019/hpc_twitter_2019).

```bash
docker pull hpc2019/ubuntu:twitter
```
3. Install Docker Compose. For guidelines visit the [link](https://docs.docker.com/compose/install/). 

4. Pull or download the `Dockerfile`, `docker_composer.yml`, `consumer.py` and `producer.py` from our [GitHub Repository](https://github.com/nelliaghajanyan/HPC-Midterm-Assessment). Place them into one directory.

5. Afterwards execute the commands written below to pull the zookeeper and kafka images from DockerHub.
```bash
docker pull wurstmeister/zookeeper 
docker pull wurstmeister/kafka
```
## Usage

1. After all installations are complete, navigate to the directory were you have placed all the downloaded files and run 
```bash
docker-compose build
```
2. When build is completed, run 
```bash
docker-compose up
```

## Contributors (Team members)

[Grigor Nalbandyan](https://github.com/GRIGORR) - Python/Kafka Expert   
[Nelli Aghajanyan](https://github.com/nelliaghajanyan) - Kafka Expert  
[Levon Avetisyan](https://github.com/12levoav) - Group Leader, Docker Expert  
[Lilit Harutyunyan](https://github.com/HLilit) - Linux/Docker Expert   
[Arsen Ignatosyan](https://github.com/arsenignatosyan) -  Linux Expert  
[Artyom Hakobyan](https://github.com/tyomhak) - Python Expert 

