# Crossix exercise 

# Prerequisites:
 - Ubuntu server (Ubuntu 20.x.x LTS)
 - AWS free tier account
 - AWS default vpc
 - SSH client
 - Browser
 - git client should be installed on Ubuntu server
 - AWS access & secrets keys should be generated
 - AWS Keys pair with KeyName - "crossix"
 - Kubernetis Clusster


### Jenkins installation

Login to your Ubuntu server

Install Python 3, Ansible, and the openshift module

```sh
$sudo apt update && sudo apt install -y python3 && sudo apt install -y python3-pip  && sudo pip3 install boto3 && sudo pip3 install ansible && sudo pip3 install openshift
$ echo "export PATH=$PATH:~/.local/bin" >> ~/.bashrc && . ~/.bashrc
```

Download exercise solution files from github

```sh
$  git clone https://github.com/Goshaka/crossix-exercise.git  
```

Create jenkins ec2 server by execute ansible playbook crossix.yml 

```sh
$  cd crossix-exercise/  
$  ansible-playbook crossix.yml -e @crossix-vars.yml -e aws_access_key='your_aws_access_key' -e aws_secret_key='your_aws_secret_key' -e YourInternetIP='YourInternetIP'
```

### Jenkins pipeline creation

After the Jenkins server will be created and UP
Go to AWS console EC2 service and find out instance public IP

![ec2_ip](images/ec2.png)

Open chrome browser or other one and put into address bar <Jenkins Instance public IP>:8080
 
![jn-login](images/jn_login.png)

Login by ssh to jenkins ec2 instace 

```sh

$   ssh -i <pem file location>/crossix.pem ec2-user@54.85.133.174 "sudo cat /var/lib/jenkins/secrets/initialAdminPassword"

```
![jn-pass](images/jn_pass.png)

Copy output of the "cat" command and put to Jenkins login page

Login to jenkins and unlock jenkins 

![jn-login](images/jn_login.png)

![unloc_jenkins](images/unlock_jenkins.png)

Install suggested plugins

![jn-plugin](images/jn_plugin.png)



Create new user
![jn-user](images/jn_user.png)

Configuring Jenkins User to Connect to the Cluster
As mentioned, this lab assumes that you already have a Kubernetes cluster up and running.
```sh

$ sudo cp ~/.kube/config ~jenkins/.kube/
$ sudo chown -R jenkins: ~jenkins/.kube/

```
Create the Jenkins Pipeline Job

![new_job](images/new_job.png)

Configure new job according to the following screenshots

![git_hook](images/git_hook.png)

Put git https url "https://github.com/Goshaka/crossix-exercise.git" into "Repository Url" field 

![pp-conf](images/pp-conf.png)

![run_build](images/run_build.png)

Open docker rest API

![docker_test](images/docker_test.png)






