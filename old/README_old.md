<p align="center">
  <img src="14098888813_1047e39f08.jpg"/><br>
</p>

### FALTA SUBIR LA DOCUMENTACIÓN ...


### Install docker on Debian 8
<pre>
  apt-get install docker.io -y
</pre>
  
### Find a docker images

<pre>
docker search ubuntu
docker search jenkins
docker search any system
</pre>




Ok, imagine that you need work with a particular version of Ubuntu with some instaled packages.  In the past you needed install a ubuntu and then install your packages.

<pre>
Here we use docker to automate it.  this is the steps
1. Download ubuntu latest
2. run the container
3. install all packages and configs than our need
4. commit and upload our base ubuntu container to the use in the future.
5. donwload and use the image in any place  :)
</pre>

### Pull a ubuntu latest (1)
<pre>
  docker pull ubuntu:latest
</pre>

### Run the container Ubuntu (2)
<pre>
  docker run -it --name ubuntu_base ubuntu /bin/bash
</pre>

### install packages into ubuntu (3)
<pre>
  apt-get update
  apt-get install vim net-tools strace mlocate git sudo -y
  passwd root 
  useradd -m -r -s /bin/bash jprado
  passwd jprado
  exit
</pre>
  
### Commit the new version of ubuntu (ubuntu_base) (4)
<pre>
  # docker commit  -m "Description                " -a " Owner        " Repo_of_docker_hub:tag   Name_of_container
  docker commit  -m "Ubuntu base para desarrollo" -a "Jonathan Prado" jpradoar/ubuntubase:0.1  ubuntu_base
  #
  # push to remote dockerhub
  docker push jpradoar/ubuntubase:0.1
  
</pre>

### Download the new base image or container (5)
<pre>
  docker pull jpradoar/ubuntubase:0.1
</pre>
  
  
### show the image
<pre>
  docker images -a
  REPOSITORY            TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
  jpradoar/ubuntubase   0.1                 9a7afe52d3ef        About an hour ago   302.6 MB
</pre>
  
  
###  Run again the container base
<pre>
  docker run -it --name ubuntu_testing01 jpradoar/ubuntubase:0.1 /bin/bash
</pre>
  
