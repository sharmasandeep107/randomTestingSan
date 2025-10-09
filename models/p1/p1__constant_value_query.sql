{{
  config({    
    "materialized": "ephemeral",
    "database": "sandeep",
    "schema": "default"
  })
}}

WITH constant_value_query AS (

  SELECT 1 AS f1

)

SELECT *

FROM constant_value_query
