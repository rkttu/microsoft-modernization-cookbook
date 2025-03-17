# 코드 수정 없이 NT 서비스 컨테이너화하기

## 요약

이 레시피는 컨테이너화할 Windows 애플리케이션의 코드를 수정하지 않고 컨테이너로 리호스팅할 수 있는 방법을 담고 있습니다.

## 샘플 애플리케이션

Windows에서 NT 서비스와 네트워크 기능이 정상적으로 작동하는지 확인하기 위한 목적으로 활용하기 좋은 기본 컴포넌트가 포함되어있습니다.

바로 Simple TCP Service이며, 이 서비스 안에는 현재 시스템의 시간을 조회해서 알려주거나, 오늘의 격언을 표시하거나, 임의의 문자열을 연결한 원격 클라이언트로 보내주는 기능이 들어있습니다.

이 레시피에서는 Simple TCP Service를 컨테이너로 리호스팅하는 과정을 살펴봅니다.

## 고려할 사항

NT 서비스를 코드 수정 없이 컨테이너로 리호스팅할 때 고려할 사항이 몇 가지 있습니다.

### 생명 주기 일치시키기

Windows 컨테이너는 NT 서비스를 컨테이너로 곧바로 변환할 수 있는 기능을 직접 제공하지 않습니다. 항상 실행의 주체가 되는 일반 애플리케이션이 필요하며, 이 애플리케이션의 시작과 끝을 추적하여 컨테이너의 생명 주기가 결정되도록 설계되어있습니다. 따라서 NT 서비스의 실행과 종료를 관장할 별도의 도우미 유틸리티가 필요합니다.

Docker의 시작 프로세스를 Microsoft의 ServiceMonitor로 지정해서 ServiceMonitor 프로세스가 시작되면 SCM을 통해 서비스 시작 명령을 보내고, 종료 시그널이 들어오면 SCM을 통해 서비스 종료 명령을 보내도록 만들어야 합니다.

### 컨테이너 내부 사용자 권한 지정

ServiceMonitor를 이용하여 컨테이너를 시작할 것이므로, 컨테이너의 사용자 권한은 반드시 `ContainerAdministartor`로 승격한 상태로 마무리해야 합니다. 그렇지 않을 경우, 권한 없음 오류가 발생하여 컨테이너가 정상적으로 시작되지 않습니다.

## Dockerfile 예제 만들어보기

아래 예제 Dockerfile은 오늘의 격언 (QOTD) 서비스를 컨테이너로 패키징하는 예시입니다. 다음의 Dockerfile 스크립트를 `Dockerfile_QOTD` 라고 저장하겠습니다.

```docker
# 베이스 이미지 선택
FROM mcr.microsoft.com/windows/servercore:ltsc2022

# PowerShell 명령어를 기본으로 사용하도록 명령줄 인터프리터 변경
SHELL ["powershell.exe", "-Command", "$ErrorActionPreference = 'Stop'; $ProgressPreference = 'Continue'; $VerbosePreference='Continue';"]

# Simple TCP 서비스 추가
RUN Enable-WindowsOptionalFeature -Online -FeatureName SimpleTCP

# ServiceMonitor 실행 파일 추가
ADD https://dotnetbinaries.blob.core.windows.net/servicemonitor/2.0.1.10/ServiceMonitor.exe /

# 오늘의 격언 (QOTD) 포트 공개
# 기타 다른 서비스: Echo - 7/tcp, Discard - 9/tcp, Daytime - 13/tcp, chargen - 19/tcp
EXPOSE 17/tcp

# 컨테이너 기본 사용자를 관리자로 변경
# ServiceMonitor 프로세스가 NT 서비스를 시작하기 위해서는 반드시 관리자 권한이 필요
USER ContainerAdministrator

# 서비스 모니터와 함께 SimpTcp 서비스를 시작/종료하도록 구성
ENTRYPOINT C:\ServiceMonitor.exe SimpTcp
```

## 컨테이너 빌드하고 실행하기

컨테이너를 빌드하기 위하여 다음 명령어를 PowerShell에서 실행합니다.

```powershell
docker.exe build -t qotd:latest -f Dockerfile_QOTD .
```

컨테이너를 실행하기 위하여 다음 명령어를 PowerShell에서 실행합니다.

```powershell
docker.exe run -dt -p 17:17 --name qotd qotd:latest
```

메시지가 정상적으로 수신되는지 확인하기 위하여 `telnet` 유틸리티를 설치 후 사용하거나, `ncat` 과 비슷한 유틸리티를 사용할 수 있습니다. 여기서는 `telnet` 유틸리티를 사용하겠습니다.

```powershell
Enable-WindowsOptionalFeature -Online -FeatureName TelnetClient
```

텔넷 클라이언트를 이용하여 TCP 17번 포트로 접속합니다.

```powershell
telnet.exe localhost 17
```

잠시 기다리면 다음과 같이 오늘의 격언 메시지가 표시될 것입니다. Enter 키를 누르면 연결이 끊어지고 자동으로 텔넷 세션이 종료됩니다.

```text
"Man can climb to the highest summits, but he cannot dwell there long."
 George Bernard Shaw (1856-1950)
```
