# OSUNGSCHOOL

강릉오성학교 교사를 위한 **AI 활용·바이브코딩 연수** 자료 제작 저장소이다.

- 주강사: **서정완**
- 대상: 전문 개발자가 아닌 강릉오성학교 교사
- 방향: 생활·수업의 작은 불편을 AI와 함께 실제 도구로 만들어 보는 초보자 중심 바이브코딩 연수

## 저장소 구성

```text
OSUNGSCHOOL/
├─ README.md
├─ AGENTS.md
├─ DESIGN.md
├─ docs/
│  ├─ 00_course_overview.md
│  ├─ 02_slide_outline.md
│  ├─ 03_speaker_script.md
│  ├─ 04_sources.md
│  └─ revision notes
├─ slides/
│  ├─ source/
│  └─ pdf/
└─ references/
   └─ source/
```

## 강의 구성 원칙

- 추상적인 개발 용어보다 **생활 속 예시를 먼저** 보여준다.
- 예약 종료 같은 작은 기능에서 시작해 사용자·환경·기술 선택을 설명한다.
- Harness, Skill, MCP 등은 학교 업무에 빗댄 쉬운 설명과 실제 작업 흐름을 함께 제시한다.
- Everything Claude Code(ECC)는 Anthropic 해커톤 우승자의 공개 하네스 사례로 분석하되, 전부 복사하지 않고 초보자에게 필요한 구조만 가져온다.
- 해커톤 우승 사례에서는 직업보다 **현장 문제와 도메인 지식을 어떻게 구조화했는지**를 본다.
- DESIGN.md → 이미지 도안 → Claude Design / Stitch / Figma → 개발 Agent 연결 흐름을 다룬다.
- 특수교육 교사의 도메인 지식을 사용자 흐름과 UX 설계로 연결한다.
- PDF는 16:9로 제작하고 전 페이지 렌더링 검수한다.

## 현재 개편 방향

초기 자료보다 초보 교사 중심으로 다음 내용을 강화했다.

1. 컴퓨터 예약 종료 예시
2. 초보자가 알아둘 최소 개발 지식
3. CPU/RAM보다 사용 조건을 먼저 보는 기술 선택
4. ECC에서 초보자가 가져올 핵심 20%
5. Claude Code 해커톤 우승자들의 다양한 전문 배경과 도메인 지식 사례
6. ChatGPT Plugin/App, Claude Connector, MCP의 관계
7. Figma ↔ Claude Code/Codex 연결
8. Stitch → Google Antigravity 인계
9. DESIGN.md를 여러 도구가 공유하는 디자인 기준으로 활용
