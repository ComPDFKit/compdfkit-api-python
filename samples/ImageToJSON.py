from compdfkit.client import CPDFClient
from compdfkit.enums import CPDFConversionEnum
from compdfkit.param import ImageToJSONParameter
from compdfkit.constant import CPDFConstant


public_key = ""
secret_key = ""
client = CPDFClient(public_key, secret_key)


def image_to_json():
    # Create Task
    create_task_result = client.create_task(CPDFConversionEnum.IMAGE_TO_JSON)
    # TaskId
    task_id = create_task_result.task_id
    # Upload File
    file = "/samples/test.png"
    file_password = ""
    file_parameter = ImageToJSONParameter()
    file_parameter.is_allow_ocr = file_parameter.ALLOW_OCR
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
    image_to_json()
