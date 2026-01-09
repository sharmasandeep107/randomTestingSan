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

reformat_1 AS (

  SELECT concat("a", "b") AS c1
  
  FROM OrchestrationSource_0 AS in0

)

SELECT *

FROM reformat_1
