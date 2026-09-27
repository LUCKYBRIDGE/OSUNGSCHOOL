# 강의자료 수정 기록 v2

## 반영 요청

1. Everything Claude Code(ECC)는 Claude Code 해커톤 우승자의 GitHub 공개 자료라는 점을 강의에서 명확히 설명한다.
2. AGENTS.md, Docs, Skills, Agents, Hooks, Commands/Workflows, Memory/Handoff, MCP/Tools가 각각 따로 존재하는 목록이 아니라 실제 작업 흐름 안에서 어떻게 유기적으로 연결되는지 설명한다.

## 반영 방식

### 1. ECC 설명 보강

기존 “실제 하네스 사례: Everything Claude Code” 슬라이드의 핵심 메시지를 다음 방향으로 수정한다.

- ECC는 GitHub에 공개된 Claude Code 설정·하네스 모음이다.
- README에서 Anthropic Hackathon Winner 사례로 소개된다.
- Rules, Skills, Agents, Hooks, Commands, MCP, Memory, Verification이 함께 구성된 공개 사례로 설명한다.
- 강의에서는 설치 방법보다 “각 구성요소가 어떤 문제를 해결하는가”를 보는 사례로 다룬다.

### 2. 하네스 구성요소의 유기적 흐름 슬라이드 추가

“MCP / Tools” 뒤에 새 슬라이드 **「하네스 구성요소는 이렇게 함께 움직인다」**를 추가한다.

화면 핵심 문장은 다음과 같다.

> 지침-지식-작업법-담당자-자동화-기억-도구가 연결된다.

화면에는 다음 순서를 넣는다.

1. AGENTS.md가 항상 지킬 원칙을 고정한다.
2. Docs가 대상·문제·설계 배경을 제공한다.
3. Command/Workflow가 반복 작업을 짧게 호출한다.
4. Agent가 역할을 맡고 Skill 순서대로 수행한다.
5. MCP/Tools로 파일·GitHub·Figma 등을 실제로 다룬다.
6. Hooks가 자동 점검하고 Memory/Handoff가 상태를 남긴다.

강의 설명은 다음 구조로 한다.

- “카페 키오스크 연습 웹자료를 만들어라”라는 요청이 들어온 상황을 예로 든다.
- AGENTS.md는 개인정보, 범위 제한, 검증 수준 같은 항상 지킬 원칙을 잡는다.
- Docs는 대상 학생, 화면 원칙, 데이터 구조, 배포 방식을 알려 준다.
- 사용자는 `/plan`, `/review`, Workflow 같은 짧은 입구로 반복 작업을 호출한다.
- Planner, UI/UX Designer, Implementer, Reviewer 같은 Agent가 역할을 나누어 맡는다.
- 각 Agent는 필요한 Skill을 따라 설계·구현·검토를 진행한다.
- GitHub, Figma, Browser, File system 같은 Tool/MCP가 실제 파일과 디자인을 다룰 수 있게 한다.
- Hooks는 포매팅, 위험 명령 확인, 상태 저장, 검증 실행 같은 반복 작업을 자동화한다.
- Memory/Handoff는 다음 세션이나 다음 Agent가 이어받을 현재 상태, 완료 작업, 실패한 접근, 다음 작업을 남긴다.

## v2 산출물 기준

- 슬라이드 수: 55장 → 56장
- PDF 페이지 수: 56쪽
- 검수 결과: 한글 대체문자 0건, 검은 사각형 0건, 주요 텍스트 잘림 없음

## 주의

현재 연결된 GitHub 작업 도구는 텍스트 파일 작업에는 적합하지만 PDF/PPTX 바이너리 파일을 직접 커밋하는 기능은 제공하지 않는다. 따라서 최종 PDF/PPTX는 별도 다운로드 산출물로 관리하고, 저장소에는 설계 기준·개요·대본·수정 기록을 중심으로 보관한다.
