# Microsoft Modernization Cookbook

Microsoft의 레거시 워크로드를 클라우드 네이티브로 전환하기까지의 다양한 방법을 소개하는 Cookbook 입니다.

## Microsoft 워크로드 현대화란?

이 Cookbook은 Windows Server, SQL Server, Exchange Server, SharePoint 등의 Microsoft 엔터프라이즈 소프트웨어를 기반으로 하는 비즈니스 서비스를 현대화하는 과정을 다룹니다. 레거시 시스템을 클라우드 네이티브 환경으로 전환할 때 발생하는 다음과 같은 도전 과제들에 대한 해결책을 제시합니다:

- **레거시 종속성**: COM 구성 요소, 32비트 라이브러리 등 현대적 환경과의 호환성 문제
- **상태 관리**: 싱글톤 패턴에 의존하는 애플리케이션의 분산 환경 적응
- **라이선스 및 비용**: 클라우드 환경에서의 Microsoft 라이선스 비용 관리
- **보안 모델 변경**: 클라우드 환경에서의 인증 및 권한 부여 메커니즘 재구성

## 로컬 환경에서 실행하기

### 필수 조건

- Python 3.8 이상
- pip (Python 패키지 관리자)

### 설치 및 실행 방법

1. 저장소 클론

   ```bash
   git clone https://github.com/rkttu/microsoft-modernization-cookbook.git
   cd microsoft-modernization-cookbook
   ```

1. 가상 환경 설정 (선택사항이지만 권장합니다.)

   Linux/macOS:

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

   Windows (PowerShell):

   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```

1. 의존성 패키지 설치

   ```bash
   pip install -r requirements.txt
   ```

1. 이미지 처리에 관련된 의존성을 추가로 설치합니다. 소셜 카드 이미지 렌더링에 필요한 의존성이 충족되어야 합니다.

   자세한 내용은 [이 문서](https://squidfunk.github.io/mkdocs-material/plugins/requirements/image-processing/)에서 확인할 수 있습니다.

   Windows의 경우, msys2 실행 환경을 설치해야 하며, `C:\msys64\ucrt64\bin` 디렉터리가 `PATH` 환경 변수에 등재되어 있어야 하며, 아래 명령어로 msys64 안의 ucrt64 셸에 필요한 패키지들을 설치해야 합니다.

   ```bash
   pacman -S mingw-w64-ucrt-x86_64-pngquant mingw-w64-ucrt-x86_64-cairo mingw-w64-ucrt-x86_64-ca-certificates
   ```

1. 로컬 서버 실행

   ```bash
   mkdocs serve
   ```

1. 웹 브라우저에서 `http://127.0.0.1:8000`로 접속하여 사이트 확인

### 빌드하기

정적 사이트로 빌드하려면 다음 명령어를 사용합니다:

```bash
mkdocs build
```

빌드된 파일은 `site` 디렉토리에 생성됩니다.

## 문제 해결

`mkdocs-material`을 비롯한 패키지들이 이미 설치되어있는 경우 제거해야 할 경우가 있습니다. 이 때 다음과 같이 명령어를 실행하여 문제를 해결할 수 있습니다.

```bash
pip uninstall -r ./requirements.txt
```

## 프로젝트 구조

```text
microsoft-modernization-cookbook/
├── .github/             # GitHub 관련 파일
│   └── prompts/         # Cursor Rule 및 Copilot 프롬프트
├── docs/                # 마크다운 문서 및 콘텐츠
│   ├── 01-start/        # 시작하기 문서
│   │   ├── index.md     # 시작하기 메인 페이지
│   │   └── 02-about-ms-workload.md # Microsoft 워크로드 소개
│   └── index.md         # 메인 페이지
├── ext/                 # 확장 기능
│   └── slugs/           # URL 슬러그 생성 확장
├── hooks/               # MkDocs 훅 스크립트
│   └── socialmedia.py   # 소셜 미디어 공유 기능
├── overrides/           # 테마 오버라이드
│   └── main.html        # 메인 HTML 오버라이드
├── .gitignore           # Git 제외 파일 목록
├── mkdocs.yml           # MkDocs 설정 파일
├── requirements.txt     # Python 의존성 패키지
└── settings.json        # VS Code 설정
```

## 주요 파일 설명

- `mkdocs.yml`: MkDocs 설정 파일로, 테마, 플러그인, 네비게이션 등의 구성이 정의됨
- `requirements.txt`: 필요한 Python 패키지 목록
- `docs/`: 문서가 저장되는 디렉토리
  - `01-start/`: Microsoft 워크로드 현대화 입문 문서
- `hooks/socialmedia.py`: 블로그 포스트에 소셜 미디어 공유 버튼을 추가하는 스크립트
- `ext/slugs/slugs.py`: URL 슬러그 생성을 위한 사용자 정의 확장
- `.github/prompts/`: AI 도구 사용을 위한 프롬프트 정의 파일

## 참고 사항

- MkDocs Material 테마를 사용합니다: [https://squidfunk.github.io/mkdocs-material/](https://squidfunk.github.io/mkdocs-material/)
- 문서를 추가하거나 수정하려면 `docs/` 디렉토리에 마크다운 파일을 작성하거나 수정하세요

## 라이선스

Copyright &copy; 2009 - 2025 Jung Hyun, Nam (rkttu), All Rights Reserved

## Attributions

[cookbook](https://icons8.com/icon/lrCJ7qYp9kta/cookbook) icon by [Icons8](https://icons8.com)
