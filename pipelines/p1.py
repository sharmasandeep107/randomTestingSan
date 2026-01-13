from prophecy_pipeline_sdk.graph import *
from prophecy_pipeline_sdk.properties import *
configuration = {"schema" : {"type" : "record", "fields" : []}}
metainfo = PipelineGraphMetadata(
    label = "p1",
    version = 1,
    configuration = configuration,
    schedule = schedule,
    sensor_schedule = sensor_schedule,
)

with PipelineGraph(id = "p1", metainfo = metainfo) as graph:
    orchestrationsource_0 = PipelineProcess(
        name = "OrchestrationSource_0",
        metadata = PipelineNodeMetadata(phase = 0),
        properties = GemProperties.S3SourceSpecProperties(
          connector = {"kind" : "s3", "properties" : {"id" : ""}, "type" : "connector"},
          properties = GemProperties.S3SourceSpecProperties.S3SourceInternalProperties(
            fileOperationProperties = GemProperties.S3SourceSpecProperties.SourceFileOperationProperties(
              fileLoadingType = "filepath",
              includeFileNameColumn = True
            )
          ),
          format = GemProperties.S3SourceSpecProperties.CsvReadFormatProperties(
            allowLazyQuotes = False,
            allowEmptyColumnNames = True,
            separator = ",",
            nullValue = "",
            encoding = "UTF-8",
            schema = None,
            header = True
          )
        ),
        ports = Ports(inputs = [], outputs = [Port(name = "out")], is_custom_output_schema = False)
    )
    p1__reformat_1 = PipelineProcess(
        name = "p1__Reformat_1",
        metadata = PipelineNodeMetadata(phase = 0),
        properties = GemProperties.ModelTransformSpecProperties(modelName = "p1__Reformat_1"),
        ports = Ports(inputs = [Port(name = "in_0")], outputs = [Port(name = "out_0")], is_custom_output_schema = False)
    )
    orchestrationsource_0 >> p1__reformat_1
