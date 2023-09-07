"""
ComPDFKit API Libraries Constant Module

This module contains all the constants used in the ComPDFKit API Libraries.
"""


class CPDFConstant:
    """
    CPDFConstant class

    This class defines all the url suffixes and error messages used in the ComPDFKit API Libraries.
    """
    API_V1_OAUTH_TOKEN = "v1/oauth/token"
    API_V1_CREATE_TASK = "v1/task/{executeTypeUrl}"
    API_V1_TOOL_SUPPORT = "v1/tool/support"
    API_V1_FILE_INFO = "v1/file/fileInfo"
    API_V1_ASSET_INFO = "v1/asset/info"
    API_V1_TASK_LIST = "v1/task/list"
    API_V1_UPLOAD_FILE = "v1/file/upload"
    API_V1_EXECUTE_TASK = "v1/execute/start"
    API_V1_TASK_INFO = "v1/task/taskInfo"
    COM_PDF_KIT_TOKEN = "ComPDFKit_AccessToken"
    EXCEPTION_MSG_GET_TOKEN_FAIL = "Failed to get ComPDFKit Token: "
    EXCEPTION_MSG_CREATE_TASK_FAIL = "Saas task creation failed: "
    EXCEPTION_MSG_UPLOAD_FILE_FAIL = "Saas upload file failed: "
    EXCEPTION_MSG_EXECUTE_TASK_FAIL = "Saas file conversion failed: "
    EXCEPTION_MSG_TASK_INFO_FAIL = "Failed to query saas file status: "
    EXCEPTION_MSG_QUERY_FILE_INFO_FAIL = "Saas query file info failed: "
    EXCEPTION_MSG_QUERY_TOOLS_FAIL = "Saas query tools  failed: "
    EXCEPTION_MSG_QUERY_TENANT_ASSET_FAIL = "Saas query tenant asset failed: "
    EXCEPTION_MSG_QUERY_TASK_LIST_FAIL = ""
    SUCCESS_CODE = "200"
    SUCCESS = 200
    RESULT_SUCCESS = "success"
    STRING_SIGN_PERIOD = "."
    STRING_SIGN_COLON = ":"
    PARAMS_MISSING_ERROR = "Missing required parameter!"
    TASK_FINISH = "TaskFinish"
    EXCEPTION_CODE_PARAMETERS_ERROR = 300
    EXCEPTION_CODE_SERVER_ERROR = 500
    EXCEPTION_CODE_RUNTIME_ERROR = 700


class CPDFLanguageConstant:
    """
    CPDFLanguageConstant class

    This class defines the logging languages supported by the ComPDFKit API.
    """
    ENGLISH = 1
    CHINESE = 2
