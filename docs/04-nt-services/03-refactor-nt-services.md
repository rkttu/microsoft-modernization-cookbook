# 코드 수정을 거쳐 NT 서비스를 Windows 컨테이너로 현대화

## 요약

이 레시피는 NT Service를 `main()` 메서드를 포함하는 일반적인 콘솔 애플리케이션으로 수정하는 방안을 담고 있습니다.

## 샘플 애플리케이션

[Windows NT Service Containerisation Examples](https://gist.github.com/rkttu/865889fa4b1065ff4ca53af10dbd310d#file-build-cmd)

위의 샘플 애플리케이션은 Windows OS에 빌트인된 .NET Framework 4.8을 이용하여 간단한 웹 서버를 구동하는 두 가지 버전의 샘플을 담고 있습니다.

- `ServiceMain.cs`: Windows NT 서비스 버전으로 작성된 간단한 웹 서버 구동 애플리케이션 샘플입니다.
- `SimpleMain.cs`: ServiceMain.cs의 핵심 로직을 콘솔 애플리케이션으로 변환하고, `docker run` 명령어 실행 시 TTY (Teletype Writer) 디바이스 지정 스위치 `-t` 를 지정하지 않아도 서비스가 계속 실행될 수 있도록 구현한 Windows 컨테이너용 애플리케이션 샘플입니다.

## 컨테이너로 변환 시 고려할 사항

이 레시피는 약간의 수정으로 기존 서비스 로직에 거의 영향을 주지 않고 컨테이너화를 할 수 있어서 추천할 수 있는 방법입니다. 코드를 수정할 수 있다면 수정 없이 리호스팅을 하는 것보다 장점이 많습니다.

다음은 컨테이너로 변환할 때 코드 구현 상 고려할 사항들입니다.

- 이벤트 로그나 로그 파일 기록 관련 로직 대신, STDOUT에 모든 로그를 기록하도록 변경합니다.
- 도커 컨테이너 종료 시 CTRL_CLOSE_EVENT, CTRL_SHUTDOWN_EVENT를 수신하여 서비스 종료 전 처리를 진행해야 합니다. [^1]
- 보안을 강화하기 위하여, 시스템 계정이나 관리자 계정으로 맵핑한 상태가 아니어도 정상적으로 애플리케이션이 실행될 수 있도록 수정하는 것이 좋습니다.
  - 단, `http.sys` 를 사용하여 HTTP 요청을 처리하는 애플리케이션인 경우, `ContainerUser` 계정으로 URL ACL 등록을 처리하기 어려운 점이 있어, 계속해서 `ContainerAdministrator` 계정으로 사용해야 할 수 있습니다.

## 코드 구현 핵심 사항

### SetConsoleCtrlHandler API를 통한 Grafeful Shutdown 구현

Windows 컨테이너에 종료 요청이 접수되면, 유닉스 계열 OS와는 달리 Windows에서는 `SetConsoleCtrlHandler` Win32 API로 등록한 콜백을 통해 종료 알림이 도착합니다.

여기서 실행 중인 서버 스레드를 종료하고, 뒷정리 작업을 진행하도록 합니다.

- 만약 종료 작업에 시간이 오래 걸리는 경우, 별도의 종료 메커니즘을 구현하여 컨테이너가 정상적으로 실행 중일 때 별도 종료 절차를 실행하도록 만드는 것을 고려할 수 있습니다.

---

[^1]: [참고 자료](https://github.com/moby/moby/issues/25982#issuecomment-1954826596)
