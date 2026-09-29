# OSUNGSCHOOL 저장소 정리 기준 (v22)

이 저장소는 2026 찾아가는 학교 컨설팅 `4. AI·디지털 문제해결 실무 과정`의 기준 저장소이며, GitHub 원본을 단일 진실 공급원(SSOT)으로 본다.

## 역할별 구조

```text
OSUNGSCHOOL/
├─ README.md                     # 저장소 목적과 현재 기준 안내
├─ AGENTS.md                     # 최상위 작업 규칙
├─ DESIGN.md                     # 화면 기준 (Google DESIGN.md 형식)
├─ CONTENT_STYLE_GUIDE.md        # 화면 문구·용어·텍스트 예산
├─ SPEAKER_SCRIPT_GUIDE.md       # 발표 대본 작성 기준
├─ docs/
│  ├─ 00_course_overview.md      # 강의 목적과 큰 흐름
│  ├─ 02_slide_outline.md        # 쪽별 목적과 말할 핵심
│  ├─ 03_speaker_script.md       # 발표 대본과 예상 질문
│  ├─ 04_sources.md              # 출처
│  ├─ lecture_flow_split_20260930.md
│  ├─ v22_work_plan.md           # v22 작업 목록과 v21 쪽 번호 대응
│  ├─ pdf_validation_v22.md      # 최신 검수 기록
│  ├─ GUIDELINE_CHANGELOG.md     # 지침 변경 이력
│  └─ 05~10, *_v19·v20·v21 등     # 이전 버전 기록 (참고용)
├─ practice/                     # 인쇄용 안내문 PDF, 복사용 요청문·양식(README.md)
└─ slides/
   ├─ build/                     # HTML 원본, 스타일, 자동 검사, PDF·캡처 스크립트
   └─ pdf/                       # 발표용 PDF (현재 v22, 이전 v21)
```

## 지침 역할 분담

- `AGENTS.md`: 작업 우선순위, 확인 순서, 변경·검증 절차
- `DESIGN.md`: 레이아웃, 여백, 글자 크기, 카드·표·도식, 인쇄용 안내문, 제작·검증 절차
- `CONTENT_STYLE_GUIDE.md`: 문구, 표준 용어, 제목, 텍스트 정보량, 여러 장에 걸친 중복 방지
- `SPEAKER_SCRIPT_GUIDE.md`: 발표 설명, 사례, 전환, 대본 중복 방지

같은 규칙을 여러 파일에 복제하지 않는다.

## 운영 원칙

- 실제 발표는 1부·2부 PDF를 사용하고, 참석자에게 `practice/`의 인쇄용 안내문을 나눠 준다.
- 별도 마스터 파일은 없고 `slides/build/part1.html`, `part2.html`, `handout.html`이 원본이다.
- PDF 파일명에는 버전과 날짜를 넣는다(`*_v22_20260930.pdf`).
- 슬라이드를 고치면 `slides/build/build.sh`의 자동 검사(`OK`)와 검수 이미지를 확인하고 `docs/pdf_validation_v*.md`에 남긴다.
- 쪽을 더하거나 합치면 대본과 개요의 쪽 번호를 함께 고친다.
- 반복되는 문제는 현재 파일만 고치지 않고 관련 지침의 보강 여부를 검토한다.
- ChatGPT 프로젝트 소스로 등록한 사본이 있다면 GitHub 최신본으로 교체한다.
