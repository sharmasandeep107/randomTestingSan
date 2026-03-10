from prophecy_pipeline_sdk.graph import *
from prophecy_pipeline_sdk.properties import *
args = PipelineArgs(label = "p1", version = 1, auto_layout = False)

with Pipeline(args) as pipeline:
    orchestrationsource_2 = Process(
        name = "OrchestrationSource_2",
        properties = DatabricksVolumeSource(
          format = DatabricksVolumeSource.CsvReadFormat(schema = "external_sources/p1/OrchestrationSource_2.yml"),
          compression = DatabricksVolumeSource.Compression(kind = "uncompressed"),
          properties = DatabricksVolumeSource.DatabricksVolumeSourceInternal(
            filePath = {
              "type": "concat_operation",
              "properties": {"elements" : [{"type" : "literal", "properties" : {"value" : "abc.csv"}}]}
            }
          ),
          connector = "databricks_1"
        ),
        input_ports = None
    )
    p1__table_0 = Process(name = "p1__Table_0", properties = ModelTransform(modelName = "p1__Table_0"))
    orchestrationsource_2 >> p1__table_0
