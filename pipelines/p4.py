Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    p4__constant_value_f3 = Task(
        task_id = "p4__constant_value_f3", 
        component = "Model", 
        modelName = "p4__constant_value_f3"
    )
