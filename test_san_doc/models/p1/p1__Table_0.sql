{{
  config({    
    "materialized": "table",
    "alias": "media_customer_reviews",
    "database": "samples",
    "schema": "bakehouse"
  })
}}

WITH OrchestrationSource_2 AS (

  SELECT *
  
  FROM {{ prophecy_tmp_source('p1', 'OrchestrationSource_2') }}

),

sqlstatement_1 AS (

  SELECT 1 AS f1

)

SELECT *

FROM sqlstatement_1
