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

SELECT *
FROM rss_list;

DELETE
FROM rss_list
WHERE id = 4;

DELETE
FROM rss_list;

UPDATE rss_list
SET name    = '阡陌',
    url     = 'http://xychen.me/feed',
    updated = 'xxx'
WHERE id = 18;

CREATE TABLE rss_content
(
    id        VARCHAR(50) PRIMARY KEY NOT NULL,
    source_id INTEGER                 NOT NULL,
    author    VARCHAR(100)            NOT NULL,
    title     VARCHAR(100)            NOT NULL,
    summary   VARCHAR(500),
    updated   VARCHAR(100)            NOT NULL,
    link      VARCHAR(200),
    content   TEXT                    NOT NULL
);

ALTER TABLE rss_content
    ALTER COLUMN content SET NOT NULL;

INSERT INTO rss_content(id, source_id, author, title, summary, updated, link, content)
VALUES ('xxx', 17, '刘德华', '德玛西亚万岁', '祝你好运', 'xxx', 'www.baidu.com', '从前有座山，山里有座庙');

SELECT count(id)
FROM rss_content
WHERE id = 'xxx';

SELECT *
FROM rss_content;

DELETE
FROM rss_content;