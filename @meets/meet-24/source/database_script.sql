CREATE DATABASE task_manager;

USE task_manager;

CREATE TABLE IF NOT EXISTS td_users(
	id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(128) NOT NULL,
    password VARCHAR(256) NOT NULL,
    first_name VARCHAR(64) NOT NULL,
    last_name VARCHAR(64) NOT NULL
);

CREATE TABLE IF NOT EXISTS td_projects(
	id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(128) NOT NULL,
    description TEXT
);

CREATE TABLE IF NOT EXISTS td_tasks(
	id INT PRIMARY KEY AUTO_INCREMENT,
    project_id INT NOT NULL, 
    user_id INT, 
    title VARCHAR(256) NOT NULL,
    summary TEXT,
    task_status VARCHAR(32) DEFAULT 'OPEN'
);

CREATE TABLE IF NOT EXISTS tc_user__project(
	user_id INT,
    project_id INT,
    PRIMARY KEY(user_id, project_id)
)



SELECT * FROM td_users;
