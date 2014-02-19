CREATE TABLE IF NOT EXISTS tasks (
    id INT NOT NULL AUTO_INCREMENT,
    name CHAR(100) NOT NULL,
    closed INT NOT NULL,
    PRIMARY KEY (id)
);

-- INSERT INTO tasks (name, closed) VALUES ('Start learning Pyramid', 0);
-- INSERT INTO tasks (name, closed) VALUES ('Do quick tutorial', 0);
-- INSERT INTO tasks (name, closed) VALUES ('Have some beer!', 0);
