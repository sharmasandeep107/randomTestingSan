{% test newTestDef(model, col) %}
select * from {{model}} where {{col}} is NULL
{% endtest %}

 