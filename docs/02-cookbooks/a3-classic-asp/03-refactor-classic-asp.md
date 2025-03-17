# 클래식 ASP를 Razor Web Pages로 재개발

## 개요

Classic ASP는 대개 VBScript를 프로그래밍 언어로 사용하여 비즈니스 로직을 구현하는 경우가 많습니다. 이 점을 착안하여, Visual Basic .NET으로 [ASP.NET](http://ASP.NET) Core 페이지를 만들고, Classic ASP와 가장 가까운 형태의 문법을 제공하면서도 모던 웹 개발 기술을 지원하는 Razor Web Pages로 마이그레이션하는 것을 검토해볼 수 있습니다.

## 고려 사항

마이그레이션을 진행할 때 고려할 사항이 몇 가지 있습니다.

- 32비트 COM 서버에 비즈니스 로직을 맡기거나 의존하는 부분이 있다면, 최적의 성능을 위해 가능한 전체 비즈니스 로직을 OS와 관계 없이 사용할 수 있도록 .NET Standard 기반의 C#과 [VB.NET](http://VB.NET) 코드로 재개발하는 것이 좋습니다.
  - 만약 이 작업이 어려울 경우, [클래식 ASP를 Windows 컨테이너로 리호스팅](./02-lift-and-shift-classic-asp.md) 레시피를 참고하여 Windows 플랫폼을 계속 유지하면서 사용하는 것이 필요할 수 있습니다.
  - 당장 대체할 수 없더라도, 머지 않은 미래에 대체할 가능성과 투자 여건이 마련된다고 생각한다면, 중간 단계로서 COM Interop을 활용하는 방법을 고려할 수도 있습니다.
  - Classic ASP와 함께 쓰이는 COM 서버는 일반적으로 스크립팅 언어 지원이 활성화된 COM 컴포넌트들을 제공하므로, .NET Core에서는 `Activator.CreateInstance` 메서드와 `dynamic` 키워드로 DLR (Dynamic Language Runtime) 기능을 이용하여 이들 COM 컴포넌트를 쉽게 수용할 수 있습니다.
  - 혹은 강 타이핑이 필요한 경우, `tlbimp.exe` 같은 도구를 이용하여 타입 라이브러리 데이터를 읽어 .NET 런타임용 바인딩을 직접 제조할 수 있습니다. (참고: [타입 라이브러리를 .NET 어셈블리로 참조하기](https://learn.microsoft.com/en-us/dotnet/framework/interop/importing-a-type-library-as-an-assembly))
- Clasic ASP에서 사용하던 문법을 1:1로 완전히 매칭하지 못할 수 있습니다.
  - 특히 VBScript에서 관습적으로 사용하던 언어 수준의 방언이나 스크립트 언어 특유의 Duck Typing이 VB.NET으로 전환되면 컴파일 언어 형태로 기본 틀이 바뀌어 코드 수정이 불가피할 수 있습니다.
- Microsoft Jet, OLE DB, ADO, ODBC 같은 레거시 데이터 액세스 코드를 [ADO.NET](http://ADO.NET) 또는 Entity Framework Core로 업데이트하는 과정이 필요합니다.

## 참고 자료

- [타입 라이브러리를 .NET 어셈블리로 참조하기](https://learn.microsoft.com/en-us/dotnet/framework/interop/importing-a-type-library-as-an-assembly)
- [클래식 ASP를 Razor 웹 페이지로 마이그레이션하기, 파트 1](https://www.mikesdotnetting.com/article/225/migrating-classic-asp-to-asp-net-razor-web-pages-part-one-razor-syntax-and-visua)
