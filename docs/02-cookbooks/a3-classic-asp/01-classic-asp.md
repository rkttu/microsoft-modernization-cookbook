# 클래식 ASP 소개

## 개요

기존에 Classic ASP (.NET Framework나 .NET Core의 ASP.NET이 아님을 유의)에 맞추어 작성된 구형 웹 애플리케이션을 Windows 컨테이너로 현대화하기 위해서는, 반드시 Windows Server Core 이상의 베이스 이미지가 필요합니다. 또한, Classic ASP는 32비트 COM 서버와 상호 작용하는 경우가 많으므로, Windows-on-Windows (WOW) 모드에서 실행되도록 IIS 애플리케이션 풀 설정을 구성해야 합니다.

초기 설정이 까다롭고 난해할 수 있는 점이 있으며, 수평 확장에서는 다소 취약한 점이 있으나, 컨테이너로 패키징하여 배포하는 것이 성공하면 어렵지 않게 현대화를 달성할 수 있습니다.

## 참고 자료

- [NT 서비스](../a2-nt-services/index.md)
- [클래식 ASP 웹 사이트를 Windows 컨테이너에서 실행하기](https://www.phillipsj.net/posts/running-asp-classic-in-a-windows-container/)
