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

Reformat_2 AS (

  SELECT * 
  
  FROM Reformat_1 AS in0

)

SELECT *

FROM Reformat_2
