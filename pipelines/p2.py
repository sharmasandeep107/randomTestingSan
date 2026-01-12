with DAG():
    OrchestrationSource_0 = SourceTask(
        task_id = "OrchestrationSource_0", 
        component = "OrchestrationSource", 
        kind = "SFTPSource", 
        compression = {"kind" : "uncompressed"}, 
        isNew = False, 
        connector = Connection(kind = "sftp", id = "sftp_1"), 
        format = PARQUETFormat(Schema = None, MultiDoc = False), 
        fileOperationProperties = {"fileLoadingType" : "filepath", "includeFileNameColumn" : True}, 
        filePath = {"type" : "concat_operation", "properties" : {"elements" : [{"type" : "literal", "properties" : {"value" : "abc"}}]}}
    )
    reformat_1 = Task(
        task_id = "reformat_1", 
        component = "Reformat", 
        columnsSelector = [], 
        expressions = [{"expression" : {"expression" : "concat(\"first\",\"second\")"}, "alias" : "nam", "_row_id" : "qGCVKMnk2l"}]
    )
    OrchestrationSource_0.out >> reformat_1.in0
