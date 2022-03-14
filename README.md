![alt text](https://github.com/iancollinge/vinyl-island-project/blob/main/assets/vi-temp-logo.jpg "Vinyl Island - Vinyl Collectors Paradise")

# Vinyl Island Project
Final Project For QA DevOps Bootcamp

## Introduction

This project is the final submission for the QA DevOps bootcamp. The app is served through a CI/CD pipeline to the end user. Microsoft Azure VMs were used to maintain the pipeline. These sections document each of the stages and processes completed.

---


### Contents:

* [Introduction](#introduction)
* [Project Overview](#project-overview)
* [Quick Look](#quick-look)
* [Screen Video Recordings](#screen-video-recordings)
* [Project Management](#project-management)
* [Software Design](#software-design)
* [Testing](#testing)
* [Pipeline](#pipeline)
* [Outcomes](#outcomes)

---

##### PROJECT OVERVIEW

This project aims to create an intuitive application to create and manage a collection of vinyl records. It could be easily adapted for any type of collection.


This current version has the basic CRUD functionality with which the user can create a collection, add items to the collection, edit or delete those items.


Additional features have been included in the Jira backlog. These features include login/authentication, share collections with friends, add links to sound files (mp3), a wants list that will allow the user to search existing vinyl market places for items on their wants list. A feature to allow an image to be added to each record.

##### Quick Look

<img src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/home.jpg" data-canonical-src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/home.jpg" width="500" height="" /> <img src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/addto.jpg" data-canonical-src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/addto.jpg" width="500" height="" /><img src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/update.jpg" data-canonical-src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/update.jpg" width="500" height="" /> <img src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/edit-added-success.jpg" data-canonical-src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/edit-added-success.jpg" width="500" height="" /> <img src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/mobile-ui.jpg" data-canonical-src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/mobile-ui.jpg" width="500" height="" />

---

## Screen video recordings

* Show usage of the app
* Show update through Git to pipeline
* Show Jenkins pipeline stages

<a href="https://youtu.be/d8Jx0swfENg/watch?feature=player_embedded&v=d8Jx0swfENg" target="_blank"><img src="https://github.com/iancollinge/vinyl-island-project/raw/main/assets/home.jpg" alt="Screen recording CRUD functionality" width="400" height="" border="10" /> </a> <a href="https://youtu.be/rBNQtvLtzSc/watch?feature=player_embedded&v=rBNQtvLtzSc" target="_blank"><img src="https://github.com/iancollinge/vinyl-island-project/raw/main/assets/home.jpg" alt="Screen recording Git Push to CI/CD Pipline" width="400" height="" border="10" /></a> 

---

##### PROJECT MANAGEMENT

* Agile/Sprints
* Jira

Jira was used to plan and keep track of the app development. User stories were developed to determine the functionalities of the app. Some of the user stories developed were as follows:

* As a user, I want to be able to add items from my vinyl collection to a list.
* As a user, I want to be able to add, edit or delete items from the list.
* As a developer, I want to create an attractive GUI for the app.

I created user stories to dictate tasks. Each story was given a time and added to the Epic and sprints created to complete the tasks.

<img src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/via-sprint-3.jpg" data-canonical-src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/via-sprint-3.jpg" width="500" height="" /> <img src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/backlog.jpg" data-canonical-src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/backlog.jpg" width="500" height=""/> <img src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/roadmap.jpg" data-canonical-src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/roadmap.jpg" width="500" height="" /> <img src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/story-map.jpg" data-canonical-src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/story-map.jpg" width="500" height=""/>

---

##### SOFTWARE DESIGN

* VCcode
* Python/Flask
* Flask Alchemy, SQLite
* Bootstrap CSS Framework
---

##### TESTING

* Unit Testing
* Pytest
---

##### PIPELINE

The app was deployed using a CI/CD pipeline. This is a list of tools used for the CI/CD pipeline.

* Azure VMs
* Ubunto/Linux
* Git and Github
* Jenkins
* Docker/Docker Compose
* Nginx

---

<img src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/jenkins-stage-view.jpg" data-canonical-src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/jenkins-stage-view.jpg" width="500" height="" /> <img src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/docker-hub.png" data-canonical-src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/docker-hub.png" width="500" height="" />

---

##### OUTCOMES

Most stages of the CI/CD pipeline completed but not without some issues. One of the main problems I encountered was with permissions at various points of the pipeline run. Permissions on the Docker socket prevented the pipeline from mving to the next stage and braking it. Solution was to use 'sudo chmod 666 /var/run/docker.sock' which solved the issue though seems temporary!

Final deployment failed with a persistent ssh issue. I have not managed to fix this yet!

Overall, app works and for the most part the pipeline works though missing key stage of deploying. I'm working to understnd the problem so I can resolve and complete the process successfully.

* Triggers from Git Push
* Checks out Git Repo
* Installs Packages
* Runs Unit Tests
* Completes Build
* Pushes the Build to Docker Hub
* Deployment FAILS
* Post Build Actions would likely complete if Deployment succeeded.
