# Task Manager

Welcome to **Task Manager**, where you can register users as well as add and view tasks.

## Description

This program reads in a list of users and tasks from *'user.txt'* and *'tasks.txt'*, respectively. The user is then required to login using the login information from *'user.txt'*. Once they have signed in, if they are the admin they are able to register new users, give tasks to users, view all the tasks, view their specific tasks or display statistics. To register a new user the admin will be asked to provide a username, which will be checked against the current list of usernames and if it is unique the admin will set the user a password, if the username is not unique the admin will be asked if they wish to register a different user. The admin can also see the number of tasks and the number of users by choosing to display statistics. 

All users are able to add and view tasks. When adding a task the user will choose who it is assigned (registered users only), a name for the task, a description of the task and how many days it should take, this information is then added to *'tasks.txt'*. When viewing tasks the user is can choose to view their own, where all tasks assigned to them will be displayed, or view all tasks where all taks will be displayed. 

## User Guide

Please make sure that, when you run *'task_manager.py'*, the files *'user.txt'* and *'tasks.txt'* are in your directory.

When using this program you can log in with username: admin password: adm1n.
