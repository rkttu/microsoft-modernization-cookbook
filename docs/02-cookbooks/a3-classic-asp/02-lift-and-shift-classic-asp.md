# 클래식 ASP를 Windows 컨테이너로 리호스팅

## 요약

Classic ASP 코드를 IIS를 사용하도록 만든 Windows 컨테이너를 이용해 리호스팅하는 방법을 소개합니다.

## 코드 샘플

(준비 중입니다.)

## 현대화 고려 사항

- SQL Server는 기존에 사용 중인 인스턴스를 그대로 사용하거나, 데이터베이스 수준에서 클라우드로 별도로 마이그레이션 진행
  - 데이터베이스 사용 패턴에 따라 공유형 RDBMS 사용이 부적절한 경우도 있을 수 있음. (예: 요청량에 따른 쓰로틀링 발생)
  - 호환성 유지를 위해 설치형 SQL Server를 사용하는 것이 권장됨.
  - SQL Server는 2024년 3월 현재 컨테이너화를 하려면 리눅스로 마이그레이션을 해야만 함.
- 각종 써드파티 COM 컴포넌트 (예: ABC, Site Galaxy Upload, DextUpload 등)
  - 32비트 COM/ActiveX 컴포넌트로 빌드된 경우가 많을 것.
  - IIS 애플리케이션 풀에서 32비트 모드로 실행될 수 있게 web.config 설정 조정 필요.
- 기타 32비트 전용 애플리케이션.
  - 안티 패턴이지만, C 드라이브 루트, Windows 시스템 디렉터리에 직접 파일을 기록하려는 행태를 보이는 애플리케이션이 존재할 수 있음.
  - 또한 C:\Windows\System32 폴더에 있는 시스템 애플리케이션을 직접 액세스하려는 행태를 보이는 애플리케이션이 있을 수 있음.
    - 32비트 모드 (Windows-on-Windows, 이하 WoW라고 부름)
- 스케일링 고려 사항
  - Classic ASP가 기본 제공하는 세션 서비스는 IIS에 커플링되어있어, Sticky 세션 사용이 필요할 수 있음
  - 자체 세션 서비스가 아닌 외부 세션 서비스를 사용하도록 변경하면 일반적인 로드 밸런싱을 구성할 수 있음
