# 초보 교사 중심 강의 개편 v2

## 목적

이번 개편은 전문 개발자 중심 설명을 줄이고, 강릉오성학교 교사가 **생활·수업의 문제를 AI와 함께 작은 도구로 만드는 경험**을 이해하도록 흐름을 바꾸는 데 목적이 있다.

## 핵심 변경

### 1. 목차 중심 6개 장 구성

1. 작은 불편에서 시작
2. AI 작업환경
3. 좋은 UX/UI
4. 디자인 도구
5. 구현·검증
6. 오성학교 실습

### 2. 예약 종료 사례 추가

기존에는 인터넷에서 명령어를 검색해 `shutdown` 예약을 걸던 일을 예로 들어, 이제는 30분·1시간·2시간 버튼과 취소 기능을 가진 작은 프로그램을 직접 만들 수 있다는 흐름으로 바이브코딩을 설명한다.

### 3. 최소 개발 지식 추가

- Web App / Desktop App
- Frontend / Backend
- Database / Local Storage
- API / MCP
- GitHub / Deployment
- 기술 선택 시 CPU/RAM 하나보다 OS, 시작속도, 메모리, 설치, 배포, 유지보수를 함께 고려

### 4. Harness와 ECC 설명 개선

Everything Claude Code(ECC)는 공개 README에서 Anthropic hackathon winner의 Claude Code 하네스 사례로 소개된다. 강의에서는 전체 설정을 복사하지 않고 다음 정도를 먼저 가져오는 방향으로 설명한다.

- 규칙 파일 1개
- PROJECT_OVERVIEW.md + DESIGN.md
- 자주 쓰는 Skill 1~3개
- HANDOFF
- 꼭 필요한 MCP

### 5. 해커톤 우승자 사례 추가

Anthropic의 Built with Opus 4.7 Claude Code hackathon 공식 사례를 통해 다음 메시지를 강조한다.

- 의사 출신 소프트웨어 엔지니어: 의료 수련 도구
- 전자제품 수리 현장 경험자: 수리 진단 도구
- 컴퓨터과학 교수·AI 박사과정 연구자: 학습용 IDE
- 장인의 현장 규칙·용어·가격을 구조화해 AI 성능을 높인 사례

핵심은 “전문 개발자만 만들 수 있다”가 아니라 **문제를 가장 잘 아는 사람이 자신의 도메인 지식을 AI가 쓸 수 있게 구조화한다**는 점이다.

### 6. 외부 도구 연결 설명 추가

- ChatGPT / Codex: Plugin이 Skill·App 등을 묶을 수 있고 App이 외부 서비스와 연결
- Claude: Connector
- Claude Code / Codex / Antigravity: MCP 서버 연결 가능

### 7. 디자인 도구 연계 강화

- DESIGN.md
- ChatGPT / Gemini 이미지 도안
- Claude Design → Claude Code
- Figma MCP → Claude Code / Codex
- Stitch → Google Antigravity

## PDF 검수 기준

- 16:9
- 전 페이지 렌더링 확인
- 한글 대체문자·네모 글리프 없음
- 제목·본문·도식 겹침 없음
- 초보자가 읽기 어려운 지나치게 작은 설명 최소화
