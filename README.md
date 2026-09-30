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
| 2부 | 4. AI·디지털 문제해결 실무 과정 | 2부. UX/UI 설계와 구현·검증 실습 | UX/UI, DESIGN.md, 디자인 도구, knollab-001 사례, 구현·검증·배포, 오성학교 실습 |

현재 발표 파일은 v23이다(1부 42쪽, 2부 35쪽). 별도 마스터 파일 없이 1부·2부 원본(`slides/build/part1.html`, `part2.html`)이 기준이다. 참석자에게 나눠 줄 인쇄용 안내문과 복사용 요청문은 `practice/`에 있다.

## 최신 강의자료 다운로드 (v23)

- [전체 강의자료 ZIP](practice/downloads/osung_course_materials_v23_20260930.zip)
- [1부 발표 PDF · 42쪽](slides/pdf/osung_ai_digital_problem_solving_part1_workspace_v23_20260930.pdf)
- [2부 발표 PDF · 35쪽](slides/pdf/osung_ai_digital_problem_solving_part2_ux_implementation_v23_20260930.pdf)
- [활동 안내·활동지 PDF · A4 양면](practice/osung_ai_digital_problem_solving_handout_a4_v23_20260930.pdf)
- [발표 대본 PDF](docs/osung_speaker_script_v23_20260930.pdf) · [편집 가능한 대본](docs/03_speaker_script.md)
- [복사용 요청문](practice/README.md) · [자유 메모 활동 안내](practice/activity_guide.md)

기본 흐름은 유지하며 참고 질문·자유 메모로 시작한다. 미정은 제작 중 보완한다. v21·v22는 이전 버전이고, 실제 발표·배포에는 위 v23 파일을 쓴다. ZIP은 위 PDF 네 개와 편집용 대본, 활동 안내, 요청문, 출처, 검수 기록을 포함한다.

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
├─ DESIGN.md                      # Google DESIGN.md 형식의 화면 기준
├─ CONTENT_STYLE_GUIDE.md
├─ SPEAKER_SCRIPT_GUIDE.md
├─ docs/
│  ├─ 00_course_overview.md
│  ├─ 02_slide_outline.md         # 쪽별 목적과 말할 핵심 (v23)
│  ├─ 03_speaker_script.md        # 발표 대본 + 예상 질문 (v23, 1부 42쪽·2부 35쪽)
│  ├─ 04_sources.md               # 출처 (v23)
│  ├─ v23_work_plan.md            # v23 개정 범위와 변경 이유
│  ├─ pdf_validation_v23.md       # v23 검수 기록
│  ├─ v21_revision_analysis.md    # v21 재제작 때의 문제 분석
│  ├─ lecture_flow_split_20260930.md
│  ├─ GUIDELINE_CHANGELOG.md
│  └─ 이전 버전 기록
├─ practice/
│  ├─ README.md                   # 복사용 요청문과 양식
│  └─ osung_ai_digital_problem_solving_handout_a4_v23_20260930.pdf   # 인쇄용 안내문 (A4 앞뒤)
└─ slides/
   ├─ build/                      # HTML 원본, 스타일, 자동 검사, PDF·캡처 스크립트
   └─ pdf/
      ├─ osung_ai_digital_problem_solving_part1_workspace_v23_20260930.pdf
      ├─ osung_ai_digital_problem_solving_part2_ux_implementation_v23_20260930.pdf
      └─ (이전 버전 v21 PDF)
```

---

## 강의 구성 원칙

- 용어는 이름만 외우지 않고 **기능·사용 장면·AI에게 요청하는 방법**까지 함께 익힌다.
- 작은 불편에서 출발해 사용 조건과 최소 개발 지식을 먼저 설명한다.
- 하네스, 규칙 파일, 스킬, MCP, 인계는 비유 → 실제 파일 → 사용 장면 순서로 한 번만 제대로 설명한다.
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

## 최신 정리 문서 (v23)

- `slides/pdf/*_v23_20260930.pdf`: 발표 자료 (1부 42쪽, 2부 35쪽)
- `practice/`: 인쇄용 안내문(A4 앞뒤)과 복사용 요청문·양식
- `docs/03_speaker_script.md`: 발표 대본과 예상 질문 16개
- `docs/02_slide_outline.md`: 쪽별 목적과 말할 핵심
- `docs/lecture_flow_split_20260930.md`: 1부·2부 강의 흐름
- `docs/pdf_validation_v23.md`: PDF 검수 기록
- `docs/04_sources.md`: 출처와 v20 대비 바로잡은 사실
- `docs/v23_work_plan.md`: v23 개정 범위와 변경 이유
- `docs/GUIDELINE_CHANGELOG.md`: 핵심 지침 변경 이유와 이력
