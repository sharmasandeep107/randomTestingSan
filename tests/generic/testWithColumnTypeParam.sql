{% test testWithColumnTypeParam(model, input1, input2, input3) %}
select * from {{ model }} where {{ input1 }} = 1 and {{ input2 }} = "hello" and {{input3}} is null
{% endtest %}

 