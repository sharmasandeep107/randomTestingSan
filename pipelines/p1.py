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
        properties = GemProperties.SFTPSourceSpecProperties(
          format = GemProperties.SFTPSourceSpecProperties.JSONReadFormatProperties(multiDoc = False, schema = None),
          properties = GemProperties.SFTPSourceSpecProperties.SFTPSourceInternalProperties(
            fileOperationProperties = GemProperties.SFTPSourceSpecProperties.SourceFileOperationProperties(
              fileLoadingType = "filepath",
              includeFileNameColumn = True
            ),
            filePath = {
              "type": "concat_operation",
              "properties": {"elements" : [{"type" : "literal", "properties" : {"value" : "/"}}]}
            }
          ),
          connector = {"kind" : "sftp", "properties" : {"id" : "sftp_1"}, "type" : "connector"}
        ),
        ports = Ports(inputs = [], outputs = [Port(name = "out")], is_custom_output_schema = False)
    )
    dataset_orchestrationsource_0 = PipelineProcess(
        name = "OrchestrationSource_0",
        metadata = PipelineNodeMetadata(),
        properties = GemProperties.DatasetSpecProperties(
          label = "OrchestrationSource_0",
          table = GemProperties.DatasetSpecProperties.DBTSource(
            name = "{{ prophecy_tmp_source('p1', 'OrchestrationSource_0') }}",
            sourceType = "UnreferencedSource"
          )
        ),
        ports = Ports(inputs = [Port(name = "input_port_0")], outputs = [Port(name = "output_port_0")], is_custom_output_schema = False)
    )
    p1__reformat_1 = PipelineProcess(
        name = "p1__reformat_1",
        metadata = PipelineNodeMetadata(phase = 0),
        properties = GemProperties.ModelTransformSpecProperties(modelName = "p1__reformat_1"),
        ports = Ports(inputs = [Port(name = "in_0")], outputs = [Port(name = "out_0")], is_custom_output_schema = False)
    )
    orchestrationsource_0 >> dataset_orchestrationsource_0
    dataset_orchestrationsource_0 >> p1__reformat_1
