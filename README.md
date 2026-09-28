# OSUNGSCHOOL

강릉오성학교 교사를 위한 **2026 찾아가는 학교 컨설팅 - 4. AI·디지털 문제해결 실무 과정** 자료 제작 저장소이다.

- 일시: **2026. 9. 30.**
- 장소: **강릉오성학교**
- 주강사: **서정완**
- 대상: 전문 개발자가 아닌 학교 교사
- 방향: 생활·수업·업무의 문제를 AI와 디지털 도구로 실제 해결해 보는 실무형 연수

## 표제와 부제 운영 원칙

발표 파일을 1부·2부로 나누더라도 표제는 항상 다음으로 통일한다.

> **4. AI·디지털 문제해결 실무 과정**

1부와 2부의 이름은 표제가 아니라 **부제**로 둔다.

| 구분 | 표제 | 부제 | 핵심 내용 |
|---|---|---|---|
| 1부 | 4. AI·디지털 문제해결 실무 과정 | 1부. 문제 정의와 AI 작업환경 | 문제 찾기, 사용 조건, 최소 개발 지식, 하네스, ECC, 작업공간, Handoff |
| 2부 | 4. AI·디지털 문제해결 실무 과정 | 2부. UX/UI 설계와 구현·검증 실습 | UX/UI, DESIGN.md, 디자인 도구, 구현, 검증, 배포, 오성학교 실습 |
| MASTER | 4. AI·디지털 문제해결 실무 과정 | 전체 흐름 보존용 | 1부와 2부를 합친 전체 편집 기준 |

---

## 핵심 지침 체계

이 저장소의 반복 작업은 다음 네 파일을 중심으로 운영한다.

| 파일 | 역할 |
|---|---|
| `AGENTS.md` | 프로젝트 최상위 작업 규칙과 작업 순서 |
| `DESIGN.md` | PPT/PDF의 레이아웃, 여백, 글자 크기, overflow, 검증 기준 |
| `CONTENT_STYLE_GUIDE.md` | 슬라이드 문구, 용어, 제목, 텍스트 예산 |
| `SPEAKER_SCRIPT_GUIDE.md` | 발표 대본의 설명 방식, 사례, 전환, 중복 방지 기준 |

지침 간 역할을 중복하지 않는다.

- **AGENTS.md** = 어떻게 작업할 것인가
- **DESIGN.md** = 어떻게 보여줄 것인가
- **CONTENT_STYLE_GUIDE.md** = 무엇을 어떤 말로 얼마나 보여줄 것인가
- **SPEAKER_SCRIPT_GUIDE.md** = 무엇을 어떻게 말할 것인가

중요한 지침 변경 이유는 `docs/GUIDELINE_CHANGELOG.md`에 기록한다.

---

## ChatGPT 프로젝트 소스 운영

GitHub 저장소의 핵심 지침 파일을 **단일 진실 공급원(SSOT)** 으로 사용한다.

ChatGPT 프로젝트에서 계속 작업할 경우 다음 네 파일을 프로젝트 소스로 등록해 두는 것을 권장한다.

- `AGENTS.md`
- `DESIGN.md`
- `CONTENT_STYLE_GUIDE.md`
- `SPEAKER_SCRIPT_GUIDE.md`

프로젝트 소스에 등록된 파일은 GitHub 원본의 작업용 참조본으로 본다.

GitHub 지침이 변경되면 프로젝트 소스 사본도 가능한 한 최신본으로 교체한다.

---

## 저장소 구성

```text
OSUNGSCHOOL/
├─ README.md
├─ AGENTS.md
├─ DESIGN.md
├─ CONTENT_STYLE_GUIDE.md
├─ SPEAKER_SCRIPT_GUIDE.md
├─ docs/
│  ├─ 00_course_overview.md
│  ├─ 02_slide_outline.md
│  ├─ 03_speaker_script.md
│  ├─ 04_sources.md
│  ├─ GUIDELINE_CHANGELOG.md
│  ├─ lecture_flow_split_20260930.md
│  ├─ pdf_validation_split_20260930.md
│  ├─ repository_structure_split_20260930.md
│  └─ revision notes
└─ slides/
   ├─ source/
   │  ├─ osung_ai_digital_problem_solving_master_v17_20260930.pptx
   │  ├─ osung_ai_digital_problem_solving_part1_workspace_20260930_titlefixed.pptx
   │  └─ osung_ai_digital_problem_solving_part2_ux_implementation_20260930_titlefixed.pptx
   └─ pdf/
      ├─ osung_ai_digital_problem_solving_part1_workspace_20260930_titlefixed.pdf
      └─ osung_ai_digital_problem_solving_part2_ux_implementation_20260930_titlefixed.pdf
```

---

## 강의 구성 원칙

- 용어는 이름만 외우지 않고 **기능·사용 장면·AI에게 요청하는 방법**까지 함께 익힌다.
- 작은 불편에서 출발해 사용 조건과 최소 개발 지식을 먼저 설명한다.
- Harness, Loop, Graph, Skill, MCP, Handoff는 정확한 개념과 이해를 돕는 비유를 함께 사용한다.
- Everything Claude Code(ECC)는 공개 하네스 사례로 분석하되 학교 현장에 필요한 구조만 가져온다.
- DESIGN.md는 화면 기준을 정리하는 문서이며 이미지 도안은 필요할 때 활용하는 선택지로 설명한다.
- 특수교육 교사의 도메인 지식을 사용자 흐름과 UX 설계로 연결한다.
- PDF는 16:9로 제작하고 전 페이지 렌더링 검수한다.
- 빈 공간을 억지로 채우지 않으며 글자 크기를 줄여 내용을 밀어 넣지 않는다.
- 슬라이드 문구와 발표 대본의 역할을 분리한다.

---

## 반복 개선 원칙

이 저장소의 지침은 고정된 완성본이 아니다.

슬라이드, PDF, 대본, 실습자료를 계속 개선하면서 같은 문제가 반복되면 현재 산출물만 수정하지 않고 **해당 지침 파일에 재발 방지 규칙을 반영**한다.

예:

- 텍스트 잘림·겹침 반복 → `DESIGN.md`
- 같은 용어가 여러 방식으로 사용됨 → `CONTENT_STYLE_GUIDE.md`
- 대본이 화면 낭독문처럼 변함 → `SPEAKER_SCRIPT_GUIDE.md`
- 작업 절차나 문서 역할이 혼란스러움 → `AGENTS.md`

중요한 변경은 `docs/GUIDELINE_CHANGELOG.md`에 기록한다.

---

## 최신 정리 문서

- `docs/lecture_flow_split_20260930.md`: 1부·2부 강의 흐름 및 슬라이드 목록
- `docs/pdf_validation_split_20260930.md`: 분할본 PDF 검수 기록
- `docs/repository_structure_split_20260930.md`: 저장소 정리 기준
- `docs/GUIDELINE_CHANGELOG.md`: 핵심 지침 변경 이유와 이력
