# .NET 생태계 지형의 변화

2025년 3월 기준, .NET 생태계는 다음과 같이 큰 구획을 나눌 수 있게 재편되었습니다.

- .NET 5 및 그 이후의 최신 .NET 기술: 기술적으로는 .NET Core를 기반으로 계속해서 최신 버전이 출시되고 있고, 지금의 .NET 기술은 이 분기의 기술을 가리킵니다. Windows는 물론, Linux, macOS, Android, iOS, WebAssembly 등 매우 다양한 플랫폼을 골고루 지원하는 크로스 플랫폼 기술입니다,
- .NET Framework 4.7 이상: Windows 운영 체제에 내장되어 같이 배포되는 레거시 버전의 .NET 기술로, 최신 기능 제공 없이 보안 업데이트와 버그 수정만 반영됩니다. 특별한 목적이나 의도가 없는 한, .NET Framework 기술은 선택하는 것은 권장하지 않습니다.
- Unity: …

그리고 다음의 기술들은 더 이상 사용되지 않는 기술들입니다.

- Microsoft Silverlight: …
  - Silverlight for Windows Phone:
- Mono Framework: .NET Framework가 처음 출시되었을 때, Windows 전용이던 .NET Framework를 리눅스, 유닉스, macOS 환경 등에서도 사용할 수 있게 만들기 위한 오픈 소스 개발자 커뮤니티의 노력으로 시작된 프로젝트였으나, 2024년 11월을 기점으로 프로젝트의 성격이 바뀌어 일반적인 개발자 프레임워크의 역할이 종료되었습니다.
  - Xamarin: Mono Framework를 기반으로 iOS, Android 등의 모바일 플랫폼을 지원하기 위해 만들어진 상용 솔루션입니다. 현재는 .NET MAUI로 흡수 발전되었습니다.
  - Moonlight Runtime: Microsoft Silverlight의 오픈 소스 버전 대체 구현체로 개발되었습니다. 직접적인 계보에 해당되지는 않으나, Blazor Web Assembly가 가장 유사한 기술 구현체이며, Microsoft Silverlight 기반의 애플리케이션 개발 기술을 최신 웹 기술에서 다시 사용할 수 있도록 만들기 위한 OpenSilver 프로젝트가 후신 기술로 평가됩니다.
- .NET Compact Framework: …
- .NET Micro Framework: …
