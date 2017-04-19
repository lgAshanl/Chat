-- Database: test_db

-- DROP DATABASE test_db;

DROP TABLE users, chats, chat_users, messages;

CREATE TABLE users(
  user_id	SERIAL		PRIMARY KEY,
  name 		VARCHAR(60) 	NOT NULL DEFAULT '',
  status	BOOLEAN 	NOT NULL DEFAULT FALSE,
  hidden	BOOLEAN		NOT NULL DEFAULT FALSE,
  password	VARCHAR(18)	NOT NULL
);

CREATE TABLE chats(
  chat_id	SERIAL		PRIMARY KEY,
  admin_id 	INTEGER 	NOT NULL DEFAULT 0,
  name		VARCHAR(666) 	NOT NULL DEFAULT 'Chat'
);

CREATE TABLE chat_users(
  user_id	INTEGER		NOT NULL REFERENCES users (user_id),
  chat_id 	INTEGER 	NOT NULL REFERENCES chats (chat_id),
  hidden	BOOLEAN		NOT NULL DEFAULT FALSE
);

CREATE TABLE answers(
  answer_id	SERIAL		PRIMARY KEY,
  to_id		INTEGER		NOT NULL REFERENCES users (user_id),
  text		VARCHAR(666)	NOT NULL DEFAULT '__ANSWER__'
);

CREATE TABLE files(
  file_id	SERIAL		PRIMARY KEY,
  name		VARCHAR(666)	NOT NULL,
  file_data	BYTEA		NOT NULL
);

CREATE TABLE messages(
  message_id	SERIAL		PRIMARY KEY,
  chat_id	INTEGER		NOT NULL REFERENCES chats (chat_id),
  ip		INTEGER 	NOT NULL,
  from_id	INTEGER		NOT NULL,
  time		TIMESTAMP 	without time zone NOT NULL,
  tag		VARCHAR(7) 	NOT NULL CHECK(
				  tag = 'message' OR
				  tag = 'answer' OR
				  tag = 'info' OR
				  tag = 'error'
				),
  text		VARCHAR(666)	NOT NULL DEFAULT '__TEXT__',
  answer_id	INTEGER		REFERENCES answers (answer_id),
  file_id	INTEGER		REFERENCES files (file_id)
);

CREATE TABLE deleted_messages(
  user_id	INTEGER		NOT NULL REFERENCES users (user_id),
  chat_id 	INTEGER 	NOT NULL REFERENCES chats (chat_id),
  message_id	INTEGER		NOT NULL REFERENCES messages (message_id)
);