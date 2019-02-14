-- STEP 1 find city near me in the United States.
SELECT *
	FROM city_list
    WHERE country LIKE 'United States'

-- STEP 2 look the global_data
SELECT * FROM global_data

-- STEP 3 JOIN both tables and select which columns we want and assign unique names to identify easier.
SELECT
  city_data.city AS city,
  city_data.avg_temp AS City_Avg_Temp,
  city_data.year
FROM city_data
  WHERE city LIKE 'Seattle'
  	 OR city LIKE 'New York'


-- STEP 4 Export to .csv file.
