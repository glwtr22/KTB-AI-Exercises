import logging

# 로깅 설정
logging.basicConfig(level = logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
'''
2024-07-05 12:34:56,789 - root - DEBUG - This is a debug message
'''

# 로깅 객체
logger = logging.getLogger(__name__)
'''
__name__은 Python에서 현재 모듈의 이름을 나타내는 특별한 변수

이 코드가 직접 실행되는 스크립트의 일부라면 __name__은 '__main__'
모듈로서 임포트된 경우, __name__은 해당 모듈의 이름
이를 통해 모듈마다 별도의 로거를 생성 -> 어떤 모듈에서 발생한 로그인지 쉽게 식별 가능
'''

def divide(a, b):
    try:
        result = a / b
        logger.info("Division successful")
        return result
    except ZeroDivisionError:
        logger.error("Division by zero error")
        return None

# 로깅 테스트
print("Division successful\n", divide(10, 2))
print("Division by zero error\n", divide(10, 0))



# 로그 레벨 설정
# logger.setLevel(logging.INFO)

logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")












