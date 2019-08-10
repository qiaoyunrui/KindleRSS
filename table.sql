CREATE DATABASE kindle_rss;

CREATE TABLE rss_list
(
    id      SERIAL PRIMARY KEY NOT NULL,
    name    VARCHAR(100)       NOT NULL,
    url     VARCHAR(200)       NOT NULL,
    updated VARCHAR(100)       NOT NULL
);

INSERT INTO rss_list (name, url, updated)
VALUES ('阡陌', 'http://xychen.me/feed', '');