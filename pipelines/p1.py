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
    p1__reformat_2 = PipelineProcess(
        name = "p1__Reformat_2",
        metadata = PipelineNodeMetadata(phase = 0),
        properties = GemProperties.ModelTransformSpecProperties(modelName = "p1__Reformat_2"),
        ports = Ports(inputs = [Port(name = "in_0")], outputs = [Port(name = "out_0")], is_custom_output_schema = False)
    )
    p1__limit_1 = PipelineProcess(
        name = "p1__Limit_1",
        metadata = PipelineNodeMetadata(phase = 0),
        properties = GemProperties.ModelTransformSpecProperties(modelName = "p1__Limit_1"),
        ports = Ports(inputs = [Port(name = "in_0")], outputs = [Port(name = "out_0")], is_custom_output_schema = False)
    )
    p1__reformat_1 = PipelineProcess(
        name = "p1__Reformat_1",
        metadata = PipelineNodeMetadata(phase = 0),
        properties = GemProperties.ModelTransformSpecProperties(modelName = "p1__Reformat_1"),
        ports = Ports(inputs = [Port(name = "in_0")], outputs = [Port(name = "out_0")], is_custom_output_schema = False)
    )
    orchestrationsource_0 = PipelineProcess(
        name = "OrchestrationSource_0",
        metadata = PipelineNodeMetadata(phase = 0),
        properties = GemProperties.SharepointSourceSpecProperties(
          connector = {"kind" : "sharepoint", "properties" : {}, "type" : "connector"},
          properties = GemProperties.SharepointSourceSpecProperties.SharepointSourceInternalProperties(
            fileOperationProperties = GemProperties.SharepointSourceSpecProperties.SourceFileOperationProperties()
          ),
          format = GemProperties.SharepointSourceSpecProperties.CsvReadFormatProperties(
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
    email_1 = PipelineProcess(
        name = "Email_1",
        metadata = PipelineNodeMetadata(phase = 0),
        properties = GemProperties.EmailSpecProperties(
          body = "",
          subject = "",
          includeData = False,
          fileName = "",
          to = None,
          fileFormat = "",
          hasTemplate = False
        ),
        ports = Ports(inputs = [Port(name = "in0")], outputs = [], is_custom_output_schema = False)
    )
    p1__reformat_2 >> email_1
    orchestrationsource_0 >> p1__reformat_1
    p1__reformat_1._out(0) >> [p1__reformat_2._in(0), p1__limit_1._in(0)]
