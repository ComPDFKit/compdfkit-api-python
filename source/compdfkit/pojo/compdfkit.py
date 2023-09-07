"""
The module contains all the POJO classes used in the ComPDFKit API Libraries.
"""


class CPDFCreateTaskResult:
    """
    CPDFCreateTaskResult class

    This class defines the task id result returned by the ComPDFKit API.
    """
    _task_id = None

    def __init__(self, json):
        self._task_id = json["taskId"]

    @property
    def task_id(self):
        """
        Task id from the creation result.
        :return:
        """
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value

    def __str__(self):
        return f"CreateTaskResult{{task_id='{self._task_id}'}}"


class CPDFFileInfo:
    """
    CPDFFileInfo class

    This class defines the file information returned by the ComPDFKit API.
    """

    def __init__(self, json):
        self._file_key = json['fileKey']
        self._task_id = json['taskId']
        self._file_name = json['fileName']
        self._file_url = json['fileUrl']
        self._download_url = json['downloadUrl']
        self._source_type = json['sourceType']
        self._target_type = json['targetType']
        self._file_size = json['fileSize']
        self._convert_size = json['convertSize']
        self._convert_time = json['convertTime']
        self._status = json['status']
        self._failure_code = json['failureCode']
        self._failure_reason = json['failureReason']
        self._down_file_name = json['downFileName']
        self._file_parameter = json['fileParameter']

    @property
    def file_key(self):
        """
        File key from the file information.
        :return:
        """
        return self._file_key

    @file_key.setter
    def file_key(self, value):
        self._file_key = value

    @property
    def task_id(self):
        """
        Task id from the file information.
        :return:
        """
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value

    @property
    def file_name(self):
        """
        File name from the file information.
        :return:
        """
        return self._file_name

    @file_name.setter
    def file_name(self, value):
        self._file_name = value

    @property
    def file_url(self):
        """
        File url from the file information.
        :return:
        """
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value

    @property
    def download_url(self):
        """
        The result download url from the file information.
        :return:
        """
        return self._download_url

    @download_url.setter
    def download_url(self, value):
        self._download_url = value

    @property
    def source_type(self):
        """
        Source type from the file information.
        :return:
        """
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value

    @property
    def target_type(self):
        """
        Target type from the file information.
        :return:
        """
        return self._target_type

    @target_type.setter
    def target_type(self, value):
        self._target_type = value

    @property
    def file_size(self):
        """
        File size from the file information.
        :return:
        """
        return self._file_size

    @file_size.setter
    def file_size(self, value):
        self._file_size = value

    @property
    def convert_size(self):
        """
        Convert size from the file information.
        :return:
        """
        return self._convert_size

    @convert_size.setter
    def convert_size(self, value):
        self._convert_size = value

    @property
    def convert_time(self):
        """
        Convert time from the file information.
        :return:
        """
        return self._convert_time

    @convert_time.setter
    def convert_time(self, value):
        self._convert_time = value

    @property
    def status(self):
        """
        Task status from the file information. Returns "success" or "failed".
        :return:
        """
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def failure_code(self):
        """
        Failure code from the file information. For the list of failure codes, see
        https://api.compdf.com/api-reference/errors
        :return:
        """
        return self._failure_code

    @failure_code.setter
    def failure_code(self, value):
        self._failure_code = value

    @property
    def failure_reason(self):
        """
        Failure reason from the file information.
        :return:
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, value):
        self._failure_reason = value

    @property
    def down_file_name(self):
        """
        Filename of the result from the file information.
        :return:
        """
        return self._down_file_name

    @down_file_name.setter
    def down_file_name(self, value):
        self._down_file_name = value

    @property
    def file_parameter(self):
        """
        File parameter for the task.
        :return:
        """
        return self._file_parameter

    @file_parameter.setter
    def file_parameter(self, value):
        self._file_parameter = value

    def __str__(self):
        return (f"FileInfo{{fileKey='{self._file_key}', taskId='{self._task_id}', fileName='{self._file_name}', " +
                f"fileUrl='{self._file_url}', downloadUrl='{self._download_url}', sourceType='{self._source_type}', " +
                f"targetType='{self._target_type}', fileSize='{self._file_size}', " +
                f"convertSize='{self._convert_size}', convertTime='{self._convert_time}', status='{self._status}', " +
                f"failureCode='{self._failure_code}', failureReason='{self._failure_reason}', " +
                f"downFileName='{self._down_file_name}', fileParameter='{self._file_parameter}'}}")


class CPDFOauthResult:
    """
    CPDFOauthResult class

    This class defines the oauth result returned by the ComPDFKit API.
    """

    def __init__(self, json):
        self._expires_in = json['expiresIn']
        self._scope = json['scope']
        self._tenant_id = None
        self._access_token = json['accessToken']
        self._token_type = json['tokenType']
        self._project_name = json['projectName']
        self._project_id = None
        self._refresh_token = None

    @property
    def expires_in(self):
        """
        Expiration time of the token.
        :return:
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, value):
        self._expires_in = value

    @property
    def scope(self):
        """
        Token Range.
        :return:
        """
        return self._scope

    @scope.setter
    def scope(self, value):
        self._scope = value

    @property
    def access_token(self):
        """
        Access token string.
        :return:
        """
        return self._access_token

    @access_token.setter
    def access_token(self, value):
        self._access_token = value

    @property
    def token_type(self):
        """
        The type of the token.
        :return:
        """
        return self._token_type

    @token_type.setter
    def token_type(self, value):
        self._token_type = value

    @property
    def project_name(self):
        """
        Project Name.
        :return:
        """
        return self._project_name

    @project_name.setter
    def project_name(self, value):
        self._project_name = value

    def __str__(self):
        return (f"CPDFKitOauthResult{{expires_in='{self._expires_in}', scope='{self._scope}', " +
                f"tenant_id='{self._tenant_id}', access_token='{self._access_token}', " +
                f"token_type='{self._token_type}', project_name='{self._project_name}', " +
                f"project_id='{self._project_id}', refresh_token='{self._refresh_token}'}}")


class CPDFRecordsItem:
    def __init__(self):
        self._server = None
        self._updated_by = None
        self._creation_time = None
        self._asset_type_id = None
        self._task_fail_num = None
        self._update_time = None
        self._target_type = None
        self._use_tool_id = None
        self._task_cost = None
        self._created_by = None
        self._task_url = None
        self._source_type = None
        self._task_file_num = None
        self._task_success_num = None
        self._tenant_id = None
        self._task_finish_time = None
        self._callback_url = None
        self._id = None
        self._task_load_url = None
        self._project_id = None
        self._task_id = None
        self._task_status = None
        self._task_time = None

    @property
    def server(self):
        return self._server

    @server.setter
    def server(self, value):
        self._server = value

    @property
    def updated_by(self):
        return self._updated_by

    @updated_by.setter
    def updated_by(self, value):
        self._updated_by = value

    @property
    def creation_time(self):
        return self._creation_time

    @creation_time.setter
    def creation_time(self, value):
        self._creation_time = value

    @property
    def asset_type_id(self):
        return self._asset_type_id

    @asset_type_id.setter
    def asset_type_id(self, value):
        self._asset_type_id = value

    @property
    def task_fail_num(self):
        return self._task_fail_num

    @task_fail_num.setter
    def task_fail_num(self, value):
        self._task_fail_num = value

    @property
    def update_time(self):
        return self._update_time

    @update_time.setter
    def update_time(self, value):
        self._update_time = value

    @property
    def target_type(self):
        return self._target_type

    @target_type.setter
    def target_type(self, value):
        self._target_type = value

    @property
    def use_tool_id(self):
        return self._use_tool_id

    @use_tool_id.setter
    def use_tool_id(self, value):
        self._use_tool_id = value

    @property
    def task_cost(self):
        return self._task_cost

    @task_cost.setter
    def task_cost(self, value):
        self._task_cost = value

    @property
    def created_by(self):
        return self._created_by

    @created_by.setter
    def created_by(self, value):
        self._created_by = value

    @property
    def task_url(self):
        return self._task_url

    @task_url.setter
    def task_url(self, value):
        self._task_url = value

    @property
    def source_type(self):
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value

    @property
    def task_file_num(self):
        return self._task_file_num

    @task_file_num.setter
    def task_file_num(self, value):
        self._task_file_num = value

    @property
    def task_success_num(self):
        return self._task_success_num

    @task_success_num.setter
    def task_success_num(self, value):
        self._task_success_num = value

    @property
    def tenant_id(self):
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, value):
        self._tenant_id = value

    @property
    def task_finish_time(self):
        return self._task_finish_time

    @task_finish_time.setter
    def task_finish_time(self, value):
        self._task_finish_time = value

    @property
    def callback_url(self):
        return self._callback_url

    @callback_url.setter
    def callback_url(self, value):
        self._callback_url = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def task_load_url(self):
        return self._task_load_url

    @task_load_url.setter
    def task_load_url(self, value):
        self._task_load_url = value

    @property
    def project_id(self):
        return self._project_id

    @project_id.setter
    def project_id(self, value):
        self._project_id = value

    @property
    def task_id(self):
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value

    @property
    def task_status(self):
        return self._task_status

    @task_status.setter
    def task_status(self, value):
        self._task_status = value

    @property
    def task_time(self):
        return self._task_time

    @task_time.setter
    def task_time(self, value):
        self._task_time = value

    def __str__(self):
        return (f"RecordsItem{{server='{self._server}', updatedBy={self._updated_by}, " +
                f"creationTime='{self._creation_time}', assetTypeId={self._asset_type_id}, " +
                f"taskFailNum={self._task_fail_num}, updateTime='{self._update_time}', " +
                f"targetType='{self._target_type}', useToolId={self._use_tool_id}, " +
                f"taskCost={self._task_cost}, createdBy={self._created_by}, taskUrl='{self._task_url}', " +
                f"sourceType='{self._source_type}', taskFileNum={self._task_file_num}, " +
                f"taskSuccessNum={self._task_success_num}, tenantId={self._tenant_id}, " +
                f"taskFinishTime='{self._task_finish_time}', callbackUrl='{self._callback_url}', id={self._id}, " +
                f"taskLoadUrl='{self._task_load_url}', projectId={self._project_id}, taskId='{self._task_id}', " +
                f"taskStatus='{self._task_status}', taskTime={self._task_time}}}")


class CPDFResult(object):
    """
    CPDFResult class

    This class defines the common result returned by the ComPDFKit API.
    """

    def __init__(self, code, msg, data):
        self._code = code
        self._msg = msg
        self._data = data

    @property
    def code(self):
        """
        The result code.
        :return:
        """
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    @property
    def msg(self):
        """
        The result message.
        :return:
        """
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value

    @property
    def data(self):
        """
        The data information of the result.
        :return:
        """
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def __str__(self):
        return f"ComPdfKitResult{{code='{self._code}', msg='{self._msg}', data={self._data}}}"


class CPDFTaskInfoResult:
    """
    CPDFTaskInfoResult class

    This class defines the task information returned by the ComPDFKit API.
    """
    _cpdf_file_info_list = []

    def __init__(self, json):
        self._task_id = json["taskId"]
        self._task_file_num = json["taskFileNum"]
        self._task_success_num = json["taskSuccessNum"]
        self._task_fail_num = json["taskFailNum"]
        self._task_status = json["taskStatus"]
        self._asset_type_id = json["assetTypeId"]
        self._task_cost = json["taskCost"]
        self._task_time = json["taskTime"]
        self._source_type = json["sourceType"]
        self._target_type = json["targetType"]
        self._callback_url = json["callbackUrl"]

        json_list = json["fileInfoDTOList"]
        for json_file_info in json_list:
            self._cpdf_file_info_list.append(CPDFFileInfo(json_file_info))

    @property
    def task_id(self):
        """
        Task id from the task information.
        :return:
        """
        return self._task_id

    @task_id.setter
    def task_id(self, value):
        self._task_id = value

    @property
    def task_file_num(self):
        """
        The file number to process of the task.
        :return:
        """
        return self._task_file_num

    @task_file_num.setter
    def task_file_num(self, value):
        self._task_file_num = value

    @property
    def task_success_num(self):
        """
        The number of successfully processed files of the task.
        :return:
        """
        return self._task_success_num

    @task_success_num.setter
    def task_success_num(self, value):
        self._task_success_num = value

    @property
    def task_fail_num(self):
        """
        The number of failed processed files of the task.
        :return:
        """
        return self._task_fail_num

    @task_fail_num.setter
    def task_fail_num(self, value):
        self._task_fail_num = value

    @property
    def task_status(self):
        """
        The status of the task. Returns "TaskStart", "TaskWaiting", "TaskProcessing", "TaskFinish" or "TaskOverdue".
        :return:
        """
        return self._task_status

    @task_status.setter
    def task_status(self, value):
        self._task_status = value

    @property
    def asset_type_id(self):
        """
        Use asset type ID.
        :return:
        """
        return self._asset_type_id

    @asset_type_id.setter
    def asset_type_id(self, value):
        self._asset_type_id = value

    @property
    def task_cost(self):
        """
        The cost of the task.
        :return:
        """
        return self._task_cost

    @task_cost.setter
    def task_cost(self, value):
        self._task_cost = value

    @property
    def task_time(self):
        """
        The time spent on task.
        :return:
        """
        return self._task_time

    @task_time.setter
    def task_time(self, value):
        self._task_time = value

    @property
    def source_type(self):
        """
        Source file format from the task information.
        :return:
        """
        return self._source_type

    @source_type.setter
    def source_type(self, value):
        self._source_type = value

    @property
    def target_type(self):
        """
        Target file format from the task information.
        :return:
        """
        return self._target_type

    @target_type.setter
    def target_type(self, value):
        self._target_type = value

    @property
    def callback_url(self):
        """
        The callback url of the task.
        :return:
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, value):
        self._callback_url = value

    @property
    def cpdf_file_info_list(self):
        """
        Task file information list.
        :return:
        """
        return self._cpdf_file_info_list

    @cpdf_file_info_list.setter
    def cpdf_file_info_list(self, value):
        self._cpdf_file_info_list = value

    def __str__(self):
        result_str = (f"QueryTaskInfoResult{{taskId='{self._task_id}', taskFileNum={self._task_file_num}, " +
                      f"taskSuccessNum='{self._task_success_num}', taskFailNum='{self._task_fail_num}', " +
                      f"taskStatus='{self._task_status}', assetTypeId='{self._asset_type_id}', " +
                      f"taskCost='{self._task_cost}', taskTime={self._task_time}, sourceType='{self._source_type}', " +
                      f"targetType='{self._target_type}', callbackUrl='{self._callback_url}', fileInfoList=[")

        for index in range(len(self._cpdf_file_info_list)):
            if index == len(self._cpdf_file_info_list) - 1:
                result_str += f"{self._cpdf_file_info_list[index]}]}}"
            else:
                result_str += f"{self._cpdf_file_info_list[index]}, "

        return result_str


class CPDFTaskRecordsResult:
    """
    CPDFTaskRecordsResult class

    This class defines the task records returned by the ComPDFKit API.
    """

    def __init__(self, total, current, pages, size, optimize_count_sql, records, max_limit, search_count, orders, count_id):
        self._total = total
        self._current = current
        self._pages = pages
        self._size = size
        self._optimize_count_sql = optimize_count_sql
        self._records = records
        self._max_limit = max_limit
        self._search_count = search_count
        self._orders = orders
        self._count_id = count_id

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    @property
    def current(self):
        return self._current

    @current.setter
    def current(self, value):
        self._current = value

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        self._pages = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        self._size = value

    @property
    def optimize_count_sql(self):
        return self._optimize_count_sql

    @optimize_count_sql.setter
    def optimize_count_sql(self, value):
        self._optimize_count_sql = value

    @property
    def records(self):
        return self._records

    @records.setter
    def records(self, value):
        self._records = value

    @property
    def max_limit(self):
        return self._max_limit

    @max_limit.setter
    def max_limit(self, value):
        self._max_limit = value

    @property
    def search_count(self):
        return self._search_count

    @search_count.setter
    def search_count(self, value):
        self._search_count = value

    @property
    def orders(self):
        return self._orders

    @orders.setter
    def orders(self, value):
        self._orders = value

    @property
    def count_id(self):
        return self._count_id

    @count_id.setter
    def count_id(self, value):
        self._count_id = value

    def __str__(self):
        return (f"QueryTaskRecordsResult{{total={self._total}, current={self._current}, pages={self._pages}, " +
                f"size={self._size}, optimizeCountSql={self._optimize_count_sql}, records={self._records}, " +
                f"maxLimit={self._max_limit}, searchCount={self._search_count}, orders={self._orders}, " +
                f"countId={self._count_id}}}")


class CPDFTenantAssetItem:
    def __init__(self, asset_type_name, withholding_asset, asset):
        self._asset_type_name = asset_type_name
        self._withholding_asset = withholding_asset
        self._asset = asset

    @property
    def asset_type_name(self):
        return self._asset_type_name

    @asset_type_name.setter
    def asset_type_name(self, value):
        self._asset_type_name = value

    @property
    def withholding_asset(self):
        return self.withholding_asset

    @withholding_asset.setter
    def withholding_asset(self, value):
        self._withholding_asset = value

    @property
    def asset(self):
        return self.asset

    @asset.setter
    def asset(self, value):
        self._asset = value

    def __str__(self):
        return "TenantAssetItem{" + \
            "asset_type_name='" + self._asset_type_name + '\'' + \
            ", withholding_asset=" + str(self._withholding_asset) + \
            ", asset=" + str(self._asset) + \
            '}'


class CPDFTenantAssetResult:
    def __init__(self, tenant_asset=None):
        self._tenant_asset = tenant_asset

    @property
    def tenant_asset(self):
        return self._tenant_asset

    @tenant_asset.setter
    def tenant_asset(self, value):
        self._tenant_asset = value

    def __str__(self):
        return f'QueryTenantAssetResult{{tenantAsset={self._tenant_asset}}}'


class CPDFTool:
    """
    This class represents an enable tool in the compdfkit.
    """

    def __init__(self, json):
        self._source_type_name = json['sourceTypeName']
        self._target_type_name = json['targetTypeName']
        self._execute_type_url = json['executeTypeUrl']

    @property
    def source_type_name(self):
        """
        Source file format.
        :return:
        """
        return self._source_type_name

    @source_type_name.setter
    def source_type_name(self, value):
        self._source_type_name = value

    @property
    def target_type_name(self):
        """
        Target file format.
        :return:
        """
        return self._target_type_name

    @target_type_name.setter
    def target_type_name(self, value):
        self._target_type_name = value

    @property
    def execute_type_url(self):
        """
        The url to execute the tool.
        :return:
        """
        return self._execute_type_url

    @execute_type_url.setter
    def execute_type_url(self, value):
        self._execute_type_url = value

    def __str__(self):
        return (f"Tool{{sourceTypeName='{self._source_type_name}', targetTypeName='{self._target_type_name}', "
                f"executeTypeUrl='{self._execute_type_url}'}}")


class CPDFToolResultItem:
    def __init__(self, source_type_name, execute_type_url, target_type_name):
        self._source_type_name = source_type_name
        self._execute_type_url = execute_type_url
        self._target_type_name = target_type_name

    @property
    def source_type_name(self):
        return self._source_type_name

    @source_type_name.setter
    def source_type_name(self, value):
        self._source_type_name = value

    @property
    def execute_type_url(self):
        return self._execute_type_url

    @execute_type_url.setter
    def execute_type_url(self, value):
        self._execute_type_url = value

    @property
    def target_type_name(self):
        return self._target_type_name

    @target_type_name.setter
    def target_type_name(self, value):
        self._target_type_name = value

    def __str__(self):
        return (f"QueryToolResultItem{{sourceTypeName='{self._source_type_name}', " +
                f"executeTypeUrl='{self._execute_type_url}', targetTypeName='{self._target_type_name}'}}")


class CPDFUploadFileResult:
    def __init__(self, json):
        self._file_key = json["fileKey"]
        self._file_url = json["fileUrl"]

    @property
    def file_key(self):
        """
        File key from the upload result.
        :return:
        """
        return self._file_key

    @file_key.setter
    def file_key(self, value):
        self._file_key = value

    @property
    def file_url(self):
        """
        File url from the upload result.
        :return:
        """
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        self._file_url = value

    def __str__(self):
        return f"UploadFileResult{{file_key='{self._file_key}', file_url='{self._file_url}'}}"
