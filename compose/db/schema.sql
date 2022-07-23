\c fast_voting;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR (30),
    lastname VARCHAR (30),
    email VARCHAR (50),
    password VARCHAR (80)
);

CREATE TABLE groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR (30),
    private BOOLEAN,
    CONSTRAINT fk_owner FOREIGN KEY (id) REFERENCES users(id)
);

CREATE TABLE user_group(
    CONSTRAINT user FOREIGN KEY (id) REFERENCES users(id),
    CONSTRAINT group FOREIGN KEY (id) REFERENCES groups(id),
    PRIMARY KEY(user, group)
);

CREATE TABLE polls (
    id SERIAL PRIMARY KEY,
    title VARCHAR (50),
    description VARCHAR (300),
    CONSTRAINT author FOREIGN KEY (id) REFERENCES users(id),
    CONSTRAINT group FOREIGN KEY (id) REFERENCES groups(id)
);

CREATE TABLE options (
    id SERIAL PRIMARY KEY,
    CONSTRAINT poll FOREIGN KEY (id) REFERENCES polls(id),
    content VARCHAR (200),
);

CREATE TABLE votes (
    CONSTRAINT user FOREIGN KEY (id) REFERENCES users(id),
    CONSTRAINT poll FOREIGN KEY (id) REFERENCES polls(id),
    PRIMARY KEY (user, group)
);

/*INSERT INTO users (name, lastname, email, password)
VALUES ('Armando', 'Barragan', 'armandobp765@gmail.com', 'xxx.123')*/