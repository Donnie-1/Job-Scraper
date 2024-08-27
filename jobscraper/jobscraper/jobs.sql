CREATE TABLE Jobs (
    job_id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    company TEXT,
    location TEXT,
    list_date DATE,
    link TEXT
);

CREATE TABLE Programming_Languages (
    language_id SERIAL PRIMARY KEY,
    language_name VARCHAR(100) UNIQUE
);

CREATE TABLE Job_Languages (
    job_id INT REFERENCES Jobs(job_id),
    language_id INT REFERENCES Programming_Languages(language_id),
    PRIMARY KEY (job_id, language_id)
);

-- Hospitality?
-- location? From my home 
-- pass in search values