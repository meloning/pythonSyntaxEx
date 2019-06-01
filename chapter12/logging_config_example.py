# 로깅 모듈 탑재
import logging
import logging.config

# 설정 파일 읽어오기
logging.config.fileConfig('logging.conf')

# 로거 생성
logger = logging.getLogger(__name__)

# 로그 메세지 출력
logger.debug('이 메세지는 개발자만 이해')
logger.info('생각대로 동작 하고 있음')
logger.warn('곧 문제가 생길 가능성이 높음')
logger.error('문제가 생겼음. 기능이 동작하지 않음')
logger.critical('시스템이 다운됨')