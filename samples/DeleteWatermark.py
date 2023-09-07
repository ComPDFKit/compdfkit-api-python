from compdfkit.client import CPDFClient
from compdfkit.enums import CPDFDocumentEditorEnum
from compdfkit.param import CPDFDeleteWatermarkParameter
from compdfkit.constant import CPDFConstant

public_key = ""
secret_key = ""
client = CPDFClient(public_key, secret_key)


def delete_watermark():
    try:
        # create Task
        create_task_result = client.create_task(CPDFDocumentEditorEnum.DEL_WATERMARK)
        # taskId
        task_id = create_task_result.task_id
        # upload File
        file = "sample/test.pdf"
        file_password = ""
        file_parameter = CPDFDeleteWatermarkParameter()
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
    except Exception as e:
        print(e)


if __name__ == '__main__':
    delete_watermark()
