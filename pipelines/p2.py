Schedule = Schedule(cron = "* 0 2 * * * *", timezone = "GMT", emails = ["email@gmail.com"], enabled = False)
SensorSchedule = SensorSchedule(enabled = False)

with DAG(Schedule = Schedule, SensorSchedule = SensorSchedule):
    p2__constant_selection = Task(
        task_id = "p2__constant_selection", 
        component = "Model", 
        modelName = "p2__constant_selection"
    )
