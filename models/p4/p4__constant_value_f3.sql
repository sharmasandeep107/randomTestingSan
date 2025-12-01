{{
  config({    
    "materialized": "ephemeral",
    "database": "sandeep",
    "schema": "default"
  })
}}

WITH constant_value_f3 AS (

  SELECT 3 AS f3

)

SELECT *

FROM constant_value_f3
