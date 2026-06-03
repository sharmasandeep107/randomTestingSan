{{
  config({    
    "materialized": "ephemeral",
    "database": "qa_catalog",
    "schema": "default"
  })
}}

WITH Table_0 AS (

  SELECT * 
  
  FROM {{ ref('s')}}

),

Unpivot_1 AS (

  SELECT 
    id,
    Name,
    Value
  
  FROM Table_0 AS in0
  UNPIVOT (
    Value
    FOR Name IN (
      col_a, col_b, col_c
    )
  )

)

SELECT *

FROM Unpivot_1
