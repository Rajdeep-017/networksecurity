import sys
from networksecurity.logging import logger
class Networksecurity(Exception):
    def __init__(self,error_msg,error_detail:sys):
        self.error_msg=error_msg
        _,_,exc_tb=error_detail.exc_info()
        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename
    def __str__(self):
        return "error occured in python scritp name[{0}] line number [{1}] error msg[{2}]".format(
            self.file_name,self.lineno,str(self.error_msg))
    
# if __name__=='__main__':
#     try:
#         logger.logging.info("enter the try bloack")
#         a=1/0
#         print("this will not printed")
#     except Exception as e:
#         raise Networksecurity(e,sys)