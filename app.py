# from signLanguage.logger import logger
import sys
from signLanguage.exception import AppException
try:
     a  = 3/"s"

except Exception as e:
     
     raise AppException(e, sys)