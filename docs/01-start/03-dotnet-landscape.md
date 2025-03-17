# .NET 생태계 지형의 변화

2025년 3월 기준, .NET 생태계는 다음과 같이 큰 구획을 나눌 수 있게 재편되었습니다.

- .NET 5 및 그 이후의 최신 .NET 기술: 기술적으로는 .NET Core를 기반으로 계속해서 최신 버전이 출시되고 있고, 지금의 .NET 기술은 이 분기의 기술을 가리킵니다. Windows는 물론, Linux, macOS, Android, iOS, WebAssembly 등 매우 다양한 플랫폼을 골고루 지원하는 크로스 플랫폼 기술입니다,
- .NET Framework 4.7 이상: Windows 운영 체제에 내장되어 같이 배포되는 레거시 버전의 .NET 기술로, 최신 기능 제공 없이 보안 업데이트와 버그 수정만 반영됩니다. 특별한 목적이나 의도가 없는 한, .NET Framework 기술은 선택하는 것은 권장하지 않습니다.
- Unity: 게임 및 인터랙티브 3D 콘텐츠 개발을 위한 크로스 플랫폼 엔진으로, C#을 주요 스크립팅 언어로 사용합니다. 초기에는 Mono Framework를 기반으로 했으나, 현재는 IL2CPP(Intermediate Language to C++)와 같은 자체 기술과 함께 점진적으로 .NET의 최신 기능을 통합하고 있습니다. 게임뿐만 아니라 시뮬레이션, AR/VR, 자동차, 영화, 건축 등 다양한 산업 분야에서 널리 사용되고 있습니다.

그리고 다음의 기술들은 더 이상 사용되지 않는 기술들입니다.

- Microsoft Silverlight: 웹 브라우저를 위한 리치 인터넷 애플리케이션(RIA) 개발 플랫폼으로, Adobe Flash의 경쟁 기술이었습니다. XAML 기반 UI와 .NET 프로그래밍 모델을 웹에 제공했으나, HTML5의 부상과 모바일 플랫폼에서의 지원 부족으로 인해 2021년 10월에 공식 지원이 종료되었습니다. 웹 개발은 현재 ASP.NET Core, Blazor 등의 기술로 대체되었습니다.
  - Silverlight for Windows Phone: Windows Phone 플랫폼을 위한 Silverlight의 특수 버전으로, 모바일 애플리케이션 개발에 사용되었습니다. Windows Phone 플랫폼의 단종과 함께 수명이 종료되었으며, 현대적인 모바일 앱 개발은 .NET MAUI나 Xamarin.Forms로 전환되었습니다.
- Mono Framework: .NET Framework가 처음 출시되었을 때, Windows 전용이던 .NET Framework를 리눅스, 유닉스, macOS 환경 등에서도 사용할 수 있게 만들기 위한 오픈 소스 개발자 커뮤니티의 노력으로 시작된 프로젝트였으나, 2024년 11월을 기점으로 프로젝트의 성격이 바뀌어 일반적인 개발자 프레임워크의 역할이 종료되었습니다.
  - Xamarin: Mono Framework를 기반으로 iOS, Android 등의 모바일 플랫폼을 지원하기 위해 만들어진 상용 솔루션입니다. 현재는 .NET MAUI로 흡수 발전되었습니다.
  - Moonlight Runtime: Microsoft Silverlight의 오픈 소스 버전 대체 구현체로 개발되었습니다. 직접적인 계보에 해당되지는 않으나, Blazor Web Assembly가 가장 유사한 기술 구현체이며, Microsoft Silverlight 기반의 애플리케이션 개발 기술을 최신 웹 기술에서 다시 사용할 수 있도록 만들기 위한 OpenSilver 프로젝트가 후신 기술로 평가됩니다.
- .NET Compact Framework: 모바일 디바이스와 Windows CE, Windows Mobile과 같은 제한된 리소스 환경에서 운영되도록 설계된 .NET Framework의 축소 버전입니다. 메모리 사용량과 전력 소비를 최소화하기 위해 최적화되었으나, Windows Mobile과 Windows CE의 지원 종료와 함께 역할을 다했습니다. 현대의 임베디드 및 모바일 개발은 .NET IoT와 .NET MAUI로 이어지고 있습니다.
- .NET Micro Framework: 제한된 하드웨어 리소스를 가진 소형 임베디드 시스템을 위해 특별히 설계된 경량화된 .NET 런타임입니다. 2KB RAM에서도 동작할 수 있도록 최적화되었으며, 임베디드 시스템과 초기 IoT 디바이스에서 사용되었습니다. 현재는 .NET IoT와 같은 최신 기술로 대체되고 있으며, 오픈 소스 커뮤니티 주도의 nanoFramework가 그 역할을 일부 계승하고 있습니다.
