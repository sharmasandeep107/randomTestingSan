{{
  config({    
    "materialized": "ephemeral",
    "database": "sandeep",
    "schema": "default"
  })
}}

WITH reformat_1 AS (

  SELECT *
  
  FROM {{ ref('p1__reformat_1')}}

),

Limit_1 AS (

  SELECT * 
  
  FROM reformat_1 AS in0
  
  LIMIT 10

)

SELECT *

FROM Limit_1
