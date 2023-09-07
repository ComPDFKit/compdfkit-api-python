from compdfkit.client import CPDFClient
from compdfkit.enums import CPDFConversionEnum
from compdfkit.param import CCSVToPDFParameter
from compdfkit.constant import CPDFConstant

public_key = ""
secret_key = ""

client = CPDFClient(public_key, secret_key)


def csv_to_pdf():
    # create Task
    create_task_result = client.create_task(CPDFConversionEnum.CSV_TO_PDF)
    # taskId
    task_id = create_task_result.task_id
    # upload File
    file = "sample/test.csv"
    file_password = ""
    file_parameter = CCSVToPDFParameter()
    upload_file_result = client.upload_file(file, task_id, file_password, file_parameter)
    file_key = upload_file_result.file_key
    # perform tasks
    client.execute_task(task_id)
    # get task processing information
    task_info = client.get_task_info(task_id)
    # determine whether the task status is "TaskFinish"
    if task_info.task_status == CPDFConstant.TASK_FINISH:
        print(task_info)
        # get the final file processing information
        file_info = client.get_file_info(file_key)
        print(file_info)
        # if the task is finished, cancel the scheduled task
    else:
        print("Task incomplete processing")


if __name__ == "__main__":
    csv_to_pdf()
