DROP TABLE IF EXISTS community_activity;
CREATE TABLE IF NOT EXISTS community_activity (
    activity_id    INTEGER PRIMARY KEY,
    name           TEXT    NOT NULL,
    activity_type  TEXT    NOT NULL,
    rating         REAL    NOT NULL,
    participants   INTEGER NOT NULL,
    duration_mins  INTEGER NOT NULL
);

INSERT INTO community_activity VALUES (1, 'Yoga Flow',         'Fitness',  9.2, 15, 60);
INSERT INTO community_activity VALUES (2, 'Oil Painting',      'Arts',     8.5, 8,  90);
INSERT INTO community_activity VALUES (3, 'Beginner Pottery',  'Arts',     7.8, 6,  120);
INSERT INTO community_activity VALUES (4, 'HIIT Workout',      'Fitness',  9.5, 20, 45);
INSERT INTO community_activity VALUES (5, 'Zumba Dance',       'Fitness',  8.1, 25, 60);
INSERT INTO community_activity VALUES (6, 'Chess Club',        'Leisure',  7.2, 12, 90);
INSERT INTO community_activity VALUES (7, 'Watercolor Basics', 'Arts',     8.9, 10, 90);
INSERT INTO community_activity VALUES (8, 'Baking Workshop',   'Leisure',  9.0, 14, 150);

SELECT * FROM community_activity;
SELECT name, rating FROM community_activity ORDER BY rating ASC;
SELECT name, rating FROM community_activity ORDER BY rating DESC;
SELECT name, activity_type, rating FROM community_activity ORDER BY activity_type ASC, rating DESC;
SELECT name, rating FROM community_activity ORDER BY rating DESC LIMIT 3;
SELECT name, duration_mins FROM community_activity ORDER BY duration_mins ASC LIMIT 5;
SELECT activity_type, COUNT(*) AS activity_count FROM community_activity GROUP BY activity_type;
SELECT activity_type, SUM(participants) AS total_participants, AVG(rating) AS avg_rating
FROM community_activity
GROUP BY activity_type;

SELECT activity_type, COUNT(*) AS activity_count
FROM community_activity
GROUP BY activity_type
HAVING COUNT(*) > 2;

SELECT activity_type, AVG(rating) AS avg_rating
FROM community_activity
GROUP BY activity_type
HAVING AVG(rating) >= 8.5;
