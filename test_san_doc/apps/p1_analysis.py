from prophecy_analysis_sdk import *
meta_info = MetaInfo(pipeline_id = "p1", parameter_set = "")

with Analysis(app_id = "p1_analysis", meta_info = meta_info) as analysis:
    pass
