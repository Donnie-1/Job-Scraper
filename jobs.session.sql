-- drop table if exists job_languages;
-- drop table if exists programming_languages;
-- drop table if exists Jobs;
CREATE TABLE Jobs (
    job_id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    company TEXT,
    location TEXT,
    list_date TEXT,
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

CREATE OR REPLACE VIEW python AS 
SELECT j.title, j.company, j.location, p.language_name
FROM jobs j
JOIN job_languages jl ON jl.job_id = j.job_id
JOIN programming_languages p ON p.language_id = jl.language_id
WHERE p.language_name = 'python'
GROUP BY j.title, j.company, j.location, p.language_name;
