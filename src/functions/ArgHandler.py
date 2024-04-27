import sys
from .modules import parser


def all_arg(*kwargs):
    
    all_argumments = []
    for _list in kwargs:
        all_argumments.extend(_list)

    return all_argumments

def ArgHandler():
    uploader_folder = None
    rangue_ip = None
    port = None


    allowed_arg = ["filename", "lone"]
    upload_folder_arg = ["--upload-path", "-up"]
    rangue_ip_arg = ["--host","-H"]
    port_arg = ["--port", "-p"]


    arguments_extract = parser()
    for _arg , _val in arguments_extract.items():
        
        if _arg not in all_arg(allowed_arg, upload_folder_arg, rangue_ip_arg, port_arg):
            sys.exit()

        elif _arg in upload_folder_arg:
            uploader_folder = _val
        
        elif _arg in rangue_ip_arg:
            rangue_ip = _val

        elif _arg in port_arg:
            port =  _val

    return uploader_folder, rangue_ip, port

