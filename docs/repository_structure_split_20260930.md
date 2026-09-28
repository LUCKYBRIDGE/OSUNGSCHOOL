# OSUNGSCHOOL 저장소 정리 기준

이 저장소는 2026 찾아가는 학교 컨설팅 `4. AI·디지털 문제해결 실무 과정`의 기준 저장소이다.

GitHub 저장소의 핵심 지침 파일을 **단일 진실 공급원(SSOT)** 으로 사용한다.

## 역할별 구조

```text
OSUNGSCHOOL/
├─ README.md                     # 저장소 목적과 현재 기준 안내
├─ AGENTS.md                     # 최상위 AI/사람 작업 규칙
├─ DESIGN.md                     # 16:9 PPTX/PDF 시각·공간·overflow 기준
├─ CONTENT_STYLE_GUIDE.md        # 화면 문구·용어·텍스트 예산 기준
├─ SPEAKER_SCRIPT_GUIDE.md       # 발표 대본 작성 기준
├─ docs/
│  ├─ 00_course_overview.md      # 강의의 큰 목적
│  ├─ 02_slide_outline.md        # 슬라이드별 목적
│  ├─ 03_speaker_script.md       # 실제 발표 대본
│  ├─ 04_sources.md              # 주요 근거·출처
│  ├─ GUIDELINE_CHANGELOG.md     # 핵심 지침 변경 이력
│  ├─ lecture_flow_split_20260930.md
│  ├─ pdf_validation_split_20260930.md
│  ├─ copy_paste_prompts_v*.md
│  └─ revision notes
└─ slides/
   ├─ source/                    # 편집 가능한 PPTX 원본
   └─ pdf/                       # 발표용 PDF
```

## 지침 역할 분담

- `AGENTS.md`: 작업 우선순위, 확인 순서, 변경·검증 절차
- `DESIGN.md`: 레이아웃, 여백, 글자 크기, 카드/표/도식, overflow
- `CONTENT_STYLE_GUIDE.md`: 문구, 표준 용어, 제목, 텍스트 정보량
- `SPEAKER_SCRIPT_GUIDE.md`: 발표 설명, 사례, 전환, 대본 중복 방지

같은 규칙을 여러 파일에 복제하지 않는다.

## ChatGPT 프로젝트 소스

ChatGPT 프로젝트에서 장기적으로 작업할 때는 다음 파일을 프로젝트 소스로 등록하는 것을 권장한다.

- `AGENTS.md`
- `DESIGN.md`
- `CONTENT_STYLE_GUIDE.md`
- `SPEAKER_SCRIPT_GUIDE.md`

프로젝트 소스는 GitHub 원본의 작업용 사본으로 본다. GitHub 핵심 지침을 변경하면 프로젝트 소스도 최신본으로 교체한다.

## 운영 원칙

- 실제 발표는 1부·2부 분할본을 사용한다.
- 마스터 PPTX는 전체 흐름 보존용으로 유지한다.
- PDF/PPTX는 버전명과 날짜를 포함한다.
- 중요한 수정은 docs/에 변경 기록으로 남긴다.
- 반복되는 문제는 현재 파일만 수정하지 않고 관련 지침의 보강 여부를 검토한다.
- GitHub에 바이너리 직접 업로드가 어려운 경우 README와 manifest에 파일명을 남기고 별도 산출물로 제공한다.
