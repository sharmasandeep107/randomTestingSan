Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    p3__constant_selection = Task(
        task_id = "p3__constant_selection", 
        component = "Model", 
        modelName = "p3__constant_selection"
    )
