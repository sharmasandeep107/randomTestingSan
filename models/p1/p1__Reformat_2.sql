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

Reformat_2 AS (

  SELECT * 
  
  FROM reformat_1 AS in0

)

SELECT *

FROM Reformat_2
