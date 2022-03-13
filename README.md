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
* [Future Development](#future-development)

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
* Show Jenkins pipeline completing

<a href="https://youtu.be/kpKs8LWH-n0/watch?feature=player_embedded&v=kpKs8LWH
" target="_blank"><img src="assets/vid1.png" 
alt="Screen recording CRUD functionality" width="240" height="180" border="10" /></a> <a href="https://youtu.be/kpKs8LWH-n0/watch?feature=player_embedded&v=kpKs8LWH
" target="_blank"><img src="assets/vid1.png" 
alt="Screen recording CRUD functionality" width="240" height="180" border="10" /></a> <a href="https://youtu.be/kpKs8LWH-n0/watch?feature=player_embedded&v=kpKs8LWH
" target="_blank"><img src="assets/vid1.png" 
alt="Screen recording CRUD functionality" width="240" height="180" border="10" /></a>

---

##### PROJECT MANAGEMENT

* Agile/Sprints
* Jira

Jira was used to plan and keep track of the app development. User stories were developed to determine the functionalities of the app. Some of the user stories developed were as follows:

* As a user, I want to be able to add items from my vinyl collection to a list.
* As a user, I want to be able to add, edit or delete items from the list.
* As a developer, I want to create an attractive GUI for the app.

Each user story was assigned a story point estimate and then assigned to an epic. Sprints were conducted lasting 1 week each and where the story points were assigned to the sprints. The backlog of the remaining issues was cleared with each sprint session.

<img src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/via-sprint-3.jpg" data-canonical-src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/via-sprint-3.jpg" width="500" height="" /> <img src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/backlog.jpg" data-canonical-src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/backlog.jpg" width="500" height="" /> <img src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/roadmap.jpg" data-canonical-src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/roadmap.jpg" width="500" height="" /> <img src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/story-map.jpg" data-canonical-src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/story-map.jpg" width="500" height="" />

---

##### SOFTWARE DESIGN

Some Text in here
* VCcode
* Python/Flask
* Flask Alchemy, SQLite
* Bootstrap CSS Framework
---

##### TESTING

Some text in here
* Unit Testing
* Pytest
---

##### PIPELINE

The app was deployed using a CI/CD pipeline. The tools and technologies used for maintaining the pipeline and deployment are:

* Azure VMs
* Ubunto/Linux
* Git and Github
* Jenkins
* Docker/Docker Compose
* Nginx
---

<img src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/jenkins-stage-view.jpg" data-canonical-src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/jenkins-stage-view.jpg" width="500" height="" /> <img src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/docker-hub.png" data-canonical-src="https://github.com/iancollinge/vinyl-island-project/blob/main/assets/docker-hub.png" width="500" height="" />
---
