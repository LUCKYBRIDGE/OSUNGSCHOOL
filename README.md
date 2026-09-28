# OSUNGSCHOOL

강릉오성학교 교사를 위한 **2026 찾아가는 학교 컨설팅 - 4. AI·디지털 문제해결 실무 과정** 자료 제작 저장소이다.

- 일시: **2026. 9. 30.**
- 장소: **강릉오성학교**
- 주강사: **서정완**
- 대상: 전문 개발자가 아닌 학교 교사
- 방향: 생활·수업·업무의 문제를 AI와 디지털 도구로 실제 해결해 보는 실무형 연수

## 현재 발표 자료 운영 방식

자료가 길어졌기 때문에 실제 발표용은 **1부·2부 분할본**으로 운영한다.

| 구분 | 파일 성격 | 핵심 내용 |
|---|---|---|
| 1부 | 문제 정의와 AI 작업환경 | 문제 찾기, 사용 조건, 최소 개발 지식, 하네스, ECC, 작업공간, Handoff |
| 2부 | UX/UI 설계와 구현·검증 실습 | UX/UI, DESIGN.md, 디자인 도구, 구현, 검증, 배포, 오성학교 실습 |
| MASTER | 전체 흐름 보존용 | 1부와 2부를 합친 전체 편집 기준 |

## 저장소 구성

```text
OSUNGSCHOOL/
├─ README.md
├─ AGENTS.md
├─ DESIGN.md
├─ docs/
│  ├─ 00_course_overview.md
│  ├─ lecture_flow_split_20260930.md
│  ├─ pdf_validation_split_20260930.md
│  ├─ repository_structure_split_20260930.md
│  └─ revision notes
└─ slides/
   ├─ source/
   │  ├─ osung_ai_digital_problem_solving_master_v17_20260930.pptx
   │  ├─ osung_ai_digital_problem_solving_part1_workspace_20260930.pptx
   │  └─ osung_ai_digital_problem_solving_part2_ux_implementation_20260930.pptx
   └─ pdf/
      ├─ osung_ai_digital_problem_solving_part1_workspace_20260930.pdf
      └─ osung_ai_digital_problem_solving_part2_ux_implementation_20260930.pdf
```

## 강의 구성 원칙

- 용어는 외우되, 이름만 외우지 않고 **기능·사용 장면·AI에게 요청하는 방법**까지 함께 익힌다.
- 작은 불편에서 출발해 사용 조건과 최소 개발 지식을 먼저 설명한다.
- Harness, Loop, Graph, Skill, MCP, Handoff는 기능을 정확히 이해할 수 있는 설명과 비유를 함께 사용한다.
- Everything Claude Code(ECC)는 Anthropic 해커톤 우승자의 공개 하네스 사례로 분석하되, 학교 현장에 필요한 구조만 가져온다.
- DESIGN.md는 화면 기준을 정리하는 문서이며, 이미지 도안은 필수가 아니라 필요할 때 쓰는 선택지로 설명한다.
- 특수교육 교사의 도메인 지식을 사용자 흐름과 UX 설계로 연결한다.
- PDF는 16:9로 제작하고 전 페이지 렌더링 검수한다.

## 최신 정리 문서

- `docs/lecture_flow_split_20260930.md`: 1부·2부 강의 흐름 및 슬라이드 목록
- `docs/pdf_validation_split_20260930.md`: 분할본 PDF 검수 기록
- `docs/repository_structure_split_20260930.md`: 저장소 정리 기준
