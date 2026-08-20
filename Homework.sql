DROP TABLE IF EXISTS marine_observation;
CREATE TABLE IF NOT EXISTS marine_observation (
    observation_id       INTEGER PRIMARY KEY,
    animal_group         TEXT    NOT NULL,
    habitat              TEXT    NOT NULL,
    estimated_weight_kg  REAL    NOT NULL,
    depth_meters         REAL    NOT NULL
);

INSERT INTO marine_observation VALUES (1, 'Whale',   'Open Ocean', 40000.0, 150.0);
INSERT INTO marine_observation VALUES (2, 'Shark',   'Coral Reef',  600.0,   30.0);
INSERT INTO marine_observation VALUES (3, 'Dolphin', 'Coastal',     250.0,   15.0);
INSERT INTO marine_observation VALUES (4, 'Whale',   'Deep Sea',   35000.0, 800.0);
INSERT INTO marine_observation VALUES (5, 'Turtle',  'Coral Reef',  120.0,   12.0);
INSERT INTO marine_observation VALUES (6, 'Shark',   'Open Ocean',  900.0,   60.0);
INSERT INTO marine_observation VALUES (7, 'Octopus', 'Deep Sea',    25.0,    900.0);
INSERT INTO marine_observation VALUES (8, 'Dolphin', 'Open Ocean',  300.0,   40.0);

SELECT * FROM marine_observation;
SELECT DISTINCT animal_group FROM marine_observation;
SELECT COUNT(DISTINCT animal_group) AS unique_groups FROM marine_observation;
SELECT COUNT(observation_id) AS total_observations FROM marine_observation;
SELECT COUNT(observation_id) AS coral_reef_observations 
FROM marine_observation 
WHERE habitat = 'Coral Reef';
SELECT SUM(estimated_weight_kg) AS total_weight_kg FROM marine_observation;
SELECT AVG(depth_meters) AS avg_depth_meters FROM marine_observation;
SELECT
    COUNT(observation_id)        AS total_observations,
    COUNT(DISTINCT animal_group) AS unique_groups,
    SUM(estimated_weight_kg)     AS total_weight_kg,
    AVG(depth_meters)            AS avg_depth_meters
FROM marine_observation;
