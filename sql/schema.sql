CREATE TABLE trainer (
    trainer_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE trainer_availability (
    availability_id SERIAL PRIMARY KEY,
    trainer_id INT NOT NULL REFERENCES trainer(trainer_id),
    start_time TIMESTAMP NOT NULL,
    end_time TIMESTAMP NOT NULL,
    CHECK (start_time < end_time)
);