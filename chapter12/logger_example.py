# 로깅 모듈 탑재
import logging

# 콘솔 출력용 핸들러 생성
handler = logging.StreamHandler()

# 포매터 생성
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)-8s - %(message)s')

# 핸들러에 포매터 설정
handler.setFormatter(formatter)

# 로거 생성 및 로그 레벨 설정, 핸들러 추가
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(handler)

# 로그 메세지 출력
logger.debug('이 메세지는 개발자만 이해')
logger.info('생각대로 동작 하고 있음')
logger.warn('곧 문제가 생길 가능성이 높음')
logger.error('문제가 생겼음. 기능이 동작하지 않음')
logger.critical('시스템이 다운됨')