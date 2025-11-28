Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    p1__constant_selection = Task(
        task_id = "p1__constant_selection", 
        component = "Model", 
        modelName = "p1__constant_selection"
    )
