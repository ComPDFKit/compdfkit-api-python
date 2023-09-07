from compdfkit.client import CPDFClient
from compdfkit.enums import CPDFDocumentEditorEnum
from compdfkit.param import CPDFAddWatermarkParameter
from compdfkit.constant import CPDFConstant

public_key = ""
secret_key = ""

client = CPDFClient(public_key, secret_key)


def add_watermark_text():
    try:
        test = CPDFDocumentEditorEnum.ADD_WATERMARK
        # create Task
        create_task_result = client.create_task(CPDFDocumentEditorEnum.ADD_WATERMARK)
        # taskId
        task_id = create_task_result.task_id
        # upload File
        file = "sample/test.pdf"
        file_password = ""
        file_parameter = CPDFAddWatermarkParameter()
        file_parameter.type = "text"
        file_parameter.scale = "1"
        file_parameter.opacity = "0.5"
        file_parameter.rotation = "0.785"
        file_parameter.target_pages = "1-2"
        file_parameter.vertalign = "center"
        file_parameter.horizalign = "left"
        file_parameter.xoffset = "100"
        file_parameter.yoffset = "100"
        file_parameter.content = "test"
        file_parameter.text_color = "#59c5bb"
        file_parameter.full_screen = "1"
        file_parameter.horizontal_space = "10"
        file_parameter.vertical_space = "10"
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


def add_watermark_image():
    try:
        # create Task
        create_task_result = client.create_task(CPDFDocumentEditorEnum.ADD_WATERMARK)
        # taskId
        task_id = create_task_result.task_id
        # upload File
        file = "sample/test.pdf"
        file_password = ""
        file_parameter = CPDFAddWatermarkParameter()
        file_parameter.type = "image"
        file_parameter.scale = "0.5"
        file_parameter.opacity = "0.5"
        file_parameter.rotation = "45"
        file_parameter.target_pages = "1-2"
        file_parameter.vertalign = "center"
        file_parameter.horizalign = "left"
        file_parameter.xoffset = "50"
        file_parameter.yoffset = "50"
        file_parameter.full_screen = "1"
        file_parameter.horizontal_space = "100"
        file_parameter.vertical_space = "100"
        file_parameter.front = "1"
        upload_file_result = client.upload_file(file, task_id, file_password, file_parameter, image="sample/test.png")
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
    add_watermark_text()
    # add_watermark_image()
