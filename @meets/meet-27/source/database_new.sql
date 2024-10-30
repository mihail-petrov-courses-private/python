CREATE UNIQUE INDEX username_UNIQUE 
ON `task_manager`.`td_users`(`username`);

CREATE TABLE IF NOT EXISTS td_tokens(
	token VARCHAR(32) PRIMARY KEY,
    generated_on TIMESTAMP default current_timestamp
);

ALTER TABLE td_tokens ADD column username VARCHAR(128);