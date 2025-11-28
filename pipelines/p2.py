Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    p2__fixed_value_query = Task(
        task_id = "p2__fixed_value_query", 
        component = "Model", 
        modelName = "p2__fixed_value_query"
    )
