from compdfkit.client import CPDFClient
from compdfkit.enums import CPDFConversionEnum
from compdfkit.param import PDFToJSONParameter
from compdfkit.constant import CPDFConstant


public_key = ""
secret_key = ""
client = CPDFClient(public_key, secret_key)


def pdf_to_json():
    # Create Task
    create_task_result = client.create_task(CPDFConversionEnum.PDF_TO_JSON)
    # TaskId
    task_id = create_task_result.task_id
    # Upload File
    file = "sample/test.pdf"
    file_password = ""
    file_parameter = PDFToJSONParameter()
    file_parameter.is_allow_ocr = file_parameter.ALLOW_OCR
    file_parameter.type = file_parameter.TYPE_TEXT
    if file_parameter:
     parameter_json = file_parameter.to_cpdf_json_str()
    upload_file_result = client.upload_file(file, task_id, file_password, file_parameter)
    file_key = upload_file_result.file_key
    # Perform tasks
    client.execute_task(task_id)
    # Get task processing information
    task_info = client.get_task_info(task_id)
    # Determine whether the task status is "TaskFinish"
    if task_info.task_status == CPDFConstant.TASK_FINISH:
        print(task_info)
        # Get the final file processing information
        file_info = client.get_file_info(file_key)
        print(file_info)
        # If the task is finished, cancel the scheduled task
    else:
        print("Task incomplete processing")


if __name__ == "__main__":
    pdf_to_json()
