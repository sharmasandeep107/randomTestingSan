{{
  config({    
    "materialized": "ephemeral",
    "database": "sandeep",
    "schema": "default"
  })
}}

WITH OrchestrationSource_0 AS (

  SELECT *
  
  FROM {{ prophecy_tmp_source('p1', 'OrchestrationSource_0') }}

),

Reformat_1 AS (

  SELECT * 
  
  FROM OrchestrationSource_0 AS in0

)

SELECT *

FROM Reformat_1
