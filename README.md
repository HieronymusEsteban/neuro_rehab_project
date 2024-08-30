I run this python project in a docker container. In order to replicate it you need docker installed on your computer. Also, I use an m1-mac computer and therefore I use a docker container that is compatible with m1-macs. This container may therefore not be compatible with windows machines.

In order to replicate the project clone the git repository, switch on docker, navigate to the project folder in your terminal and run the command docker-compose up.

There are three docker containers running, I currently only use one. The idea is to use the other containers to run PostgreSQL in order to store the data in a data base.

The Data folder is obviously empty as data should be shared by other means as by GitHub. The data is confidential and can only be shared with people involved in the project.