{{
  config({    
    "materialized": "ephemeral",
    "database": "sandeep",
    "schema": "default"
  })
}}

WITH constant_selection AS (

  SELECT 1 AS f1

)

SELECT *

FROM constant_selection
