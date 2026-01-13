{{
  config({    
    "materialized": "ephemeral",
    "database": "sandeep",
    "schema": "default"
  })
}}

WITH Reformat_1 AS (

  SELECT *
  
  FROM {{ ref('p1__Reformat_1')}}

),

Limit_1 AS (

  SELECT * 
  
  FROM Reformat_1 AS in0
  
  LIMIT 10

)

SELECT *

FROM Limit_1
