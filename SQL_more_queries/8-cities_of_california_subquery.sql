-- 8-cities_of_california_subquery.sql
-- Lists all cities in California from the hbtn_0d_usa database
-- Does NOT use JOIN

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id FROM states WHERE name = 'California'
)
ORDER BY id ASC;
