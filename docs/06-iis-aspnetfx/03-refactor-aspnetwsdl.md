# ASP.NET XML Web Service (WSDL)의 현대화

## 개요

WSDL (Web Service Description Language) 명세에 따른 웹 API를 구현할 수 있도록 만든 기술로 ASP.NET 초창기부터 지원되어오던 웹 API 기술입니다.

## ASP.NET XML Web Service의 특징

WSDL 기반 XML 웹 서비스는 TCP 통신을 사용하는 DCOM과 달리 HTTP 통신을 사용하면서 Java 기반의 클라이언트나 서버와 상호 운용할 수 있는 새로운 방안으로 WSDL 기반 XML 웹 서비스를 ASP.NET 안에 깊이 통합하려는 의도를 가지고 개발된 기술 스택이었습니다.

Visual Studio에서는 XML 웹 서비스 참조 기능을 이용하여 WSDL 기반 XML 웹 서비스 주소를 지정하면, 자동으로 메타데이터를 읽어 클라이언트 코드를 만들어주는 기능이 내장되어 있었습니다. 웹 API 개발에 대한 지식이 많지 않아도 손쉽게 개발할 수 있도록 돕는 기능이라 많은 인기가 있었습니다.

## 리눅스, 컨테이너 기반으로 모더나이제이션을 해야 할 경우 접근법

XML 웹 서비스는 Web Form과 마찬가지로 전면적인 재개발을 피할 수 없습니다. 특이한 점은, 서버 측의 변동 사항보다는 컨슈머/클라이언트 측의 변경 난이도가 높은 것이 특징입니다.

- 서버 구현 자체의 변경은 ASP.NET Web API로 이행하면 상대적으로 어렵지 않게 달성할 수 있습니다.
  - 자기 설명적 카탈로그 제공은 Swagger를 이용하여 쉽게 구현할 수 있습니다.
- Swagger가 만들어내는 JSON 메타데이터를 읽어 다양한 언어로 클라이언트 코드를 생성하는 Swagger-Codegen 유틸리티를 사용하면 클라이언트 라이브러리 제조가 가능합니다.
  - 단, Visual Studio에 이 기능이 직접 포함되어있지는 않으며, 별도의 Codegen 유틸리티를 찾아서 CI/CD 파이프라인 등에 통합하거나,
  - [REST API Client Code Generator for VS 2022](https://marketplace.visualstudio.com/items?itemName=ChristianResmaHelle.ApiClientCodeGenerator2022) 같은 써드파티 플러그인을 Visual Studio 확장으로 추가하여 사용할 수 있습니다.
