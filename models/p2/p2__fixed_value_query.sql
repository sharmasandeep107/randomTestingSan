{{
  config({    
    "materialized": "ephemeral",
    "database": "sandeep",
    "schema": "default"
  })
}}

WITH constant_selection AS (

  SELECT 1 AS f1

),

fixed_value_query AS (

  SELECT 2 AS f2

)

SELECT *

FROM fixed_value_query
