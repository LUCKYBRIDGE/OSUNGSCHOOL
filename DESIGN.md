---
version: alpha
name: OSUNGSCHOOL 연수 슬라이드
description: 강릉오성학교 교사 연수(2026. 9. 30.) 1부·2부 16:9 발표 PDF의 화면 기준
colors:
  primary: "#1D5FD1"
  navy: "#1B365D"
  ink: "#1F2933"
  muted: "#5B6878"
  background: "#FFFFFF"
  surface: "#F3F5F8"
  primary-tint: "#EDF3FD"
  accent: "#F2A33A"
  warn-tint: "#FFF4E0"
  warn-text: "#7A3A06"
  good: "#1E7B45"
  good-tint: "#EAF6EE"
  bad: "#B42318"
  bad-tint: "#FDEEEC"
  amber: "#B45309"
  border: "#D5DCE5"
typography:
  cover-title:
    fontFamily: Apple SD Gothic Neo
    fontSize: 60px
    fontWeight: 800
  section-title:
    fontFamily: Apple SD Gothic Neo
    fontSize: 54px
    fontWeight: 800
  slide-title:
    fontFamily: Apple SD Gothic Neo
    fontSize: 40px
    fontWeight: 800
  lead:
    fontFamily: Apple SD Gothic Neo
    fontSize: 25px
  body:
    fontFamily: Apple SD Gothic Neo
    fontSize: 27px
  card-title:
    fontFamily: Apple SD Gothic Neo
    fontSize: 28px
    fontWeight: 800
  card-body:
    fontFamily: Apple SD Gothic Neo
    fontSize: 24px
  label:
    fontFamily: Apple SD Gothic Neo
    fontSize: 20px
    fontWeight: 800
  code:
    fontFamily: Menlo
    fontSize: 21px
  prompt:
    fontFamily: Apple SD Gothic Neo
    fontSize: 23px
  table-body:
    fontFamily: Apple SD Gothic Neo
    fontSize: 23px
  small-body:
    fontFamily: Apple SD Gothic Neo
    fontSize: 22px
  refs:
    fontFamily: Apple SD Gothic Neo
    fontSize: 19px
  refs-url:
    fontFamily: Menlo
    fontSize: 17px
  footer:
    fontFamily: Apple SD Gothic Neo
    fontSize: 14px
rounded:
  sm: 14px
  md: 16px
spacing:
  margin: 72px
  gap: 22px
components:
  slide:
    backgroundColor: "{colors.background}"
    textColor: "{colors.ink}"
  section-slide:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.background}"
  card:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
  card-primary:
    backgroundColor: "{colors.primary-tint}"
    textColor: "{colors.ink}"
  card-good:
    backgroundColor: "{colors.good-tint}"
    textColor: "{colors.ink}"
  card-bad:
    backgroundColor: "{colors.bad-tint}"
    textColor: "{colors.ink}"
  chip:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.background}"
    typography: "{typography.label}"
  chip-good:
    backgroundColor: "{colors.good}"
    textColor: "{colors.background}"
  chip-bad:
    backgroundColor: "{colors.bad}"
    textColor: "{colors.background}"
  chip-muted:
    backgroundColor: "{colors.muted}"
    textColor: "{colors.background}"
  chip-amber:
    backgroundColor: "{colors.amber}"
    textColor: "{colors.background}"
  takeaway:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.background}"
    rounded: "{rounded.sm}"
  takeaway-warn:
    backgroundColor: "{colors.warn-tint}"
    textColor: "{colors.warn-text}"
  code-block:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.prompt}"
  code-block-mono:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    typography: "{typography.code}"
  section-number:
    backgroundColor: "{colors.navy}"
    textColor: "{colors.accent}"
  table-divider:
    backgroundColor: "{colors.border}"
    height: 2px
---

## Overview

강릉오성학교 교사(전문 개발자가 아닌 특수교육 교사)를 위한 연수 슬라이드다. 프로젝터 화면에서 뒷자리까지 읽히고, 한 장에 한 가지만 전하는 것이 목표다.

- 이 문서는 **어떻게 보여줄지**를 정한다. 무엇을 쓸지는 `CONTENT_STYLE_GUIDE.md`, 무엇을 말할지는 `SPEAKER_SCRIPT_GUIDE.md`가 정한다.
- 구현은 `slides/build/deck.css`다. 이 문서의 값과 CSS 값은 항상 같아야 하며, 한쪽을 바꾸면 다른 쪽도 함께 바꾼다.
- 형식은 Google DESIGN.md 명세(alpha)를 따른다. 위의 토큰은 정확한 값, 아래 글은 그 값을 쓰는 이유다.

## Colors

- **navy (#1B365D):** 제목, 표 머리, 핵심 한 줄 막대, 표지와 구분 슬라이드 배경.
- **primary (#1D5FD1):** 강조 칩, 번호, 목록 점. 한 장에서 강조색은 primary 하나를 기본으로 한다.
- **accent (#F2A33A):** 남색 배경 위의 구분 번호와 표지 부제에만 쓴다.
- **good / bad:** '좋은 예·피할 예' 비교에만 쓴다. 색만으로 뜻을 전하지 않도록 칩에 항상 글자('좋은 예', '피할 예')를 함께 쓴다.
- **warn-tint + warn-text:** 개인정보, 요금제, 권한처럼 주의가 필요한 한 줄에만 쓴다.
- **amber (#B45309):** '진행 중', '특별상'처럼 따로 표시할 칩에만 쓴다. 흰 글자와의 대비는 5.0:1이다.
- 배경은 흰색을 기본으로 한다. 어두운 배경은 표지와 구분 슬라이드에만 쓴다.

## Typography

- 한글 기본 글꼴은 Apple SD Gothic Neo(제작 환경 macOS), 대체 글꼴은 맑은 고딕 → Noto Sans KR이다. 경로·파일명과 DESIGN.md 같은 형식 예시(`code mono`)는 Menlo를 쓴다. 요청문과 파일 내용 예시(`code`)는 읽기 쉽게 본문 글꼴을 쓴다.
- 캔버스 1280×720px 기준 크기: 본문·카드 설명 **24px 이상**. 칸이 좁은 요소는 표 칸·코드 상자·되돌림 띠·정리 설명 23px, 표 머리·단계 설명·폴더 목록·캡션 22px까지 쓴다. 라벨·칩 **20px 이상**, 바닥글(출처·쪽 번호) 14px.
- 참고 자료 목록 슬라이드는 읽기용이므로 제목 19px, 주소 17px(Menlo)까지 허용한다.
- 목업(화면 예시) 안의 작은 글자는 '복잡함'을 보여주기 위한 그림이므로 크기 기준에서 제외한다.
- 한국어는 어절 단위로 줄을 바꾼다(`word-break: keep-all`). 어색한 줄바꿈은 글자를 줄이지 말고 문구를 줄이거나 `<br>`로 의미 단위에서 끊는다.
- 파일명·영어 단어가 중간에서 끊기면(예: `PROJECT_OVER / VIEW`) 실패로 본다. 한국어 표현으로 바꾸거나 칸을 넓힌다.

## Layout

- 16:9, 1280×720px(PDF 960×540pt). 좌우 여백 72px, 위 44px, 아래 24px.
- 기본 구조: **머리**(구역 라벨 → 제목 → 필요할 때만 보조 문장) → **본문** → **바닥글**(출처 또는 부 이름, 쪽 번호).
- 제목은 한 줄 원칙이다. 넘치면 제목 문구를 고친다.
- 본문은 세로 가운데 정렬한다. 내용이 적으면 여백을 그대로 둔다. 빈 곳을 카드나 장식으로 채우지 않는다.
- 레이아웃은 내용에 맞춰 고른다.

| 내용 | 레이아웃 |
|---|---|
| 두 개념·두 방식 비교 | 2열 카드 + 핵심 한 줄 |
| 같은 무게의 3~6개 항목 | 3열 카드(최대 2줄) |
| 순서·반복 | 단계 카드 3~5개 + 되돌림 띠 |
| 조건·대응 정리 | 표(2~4열) |
| 파일 예시·요청문 | 코드 상자(+ 오른쪽 설명 1~3개) |
| 폴더 구성 | 폴더 목록(이름 + 설명 두 칸) |
| 화면 사례 | 목업 + 오른쪽 목록 |

## Shapes

- 카드·코드 상자 모서리 16px, 핵심 한 줄 막대 14px, 칩은 알약 모양.
- 테두리는 흰 카드(`card line`)에만 2px로 쓴다. 그림자는 쓰지 않는다(목업 속 광고 팝업 제외).
- 단계 사이 화살표는 카드 밖의 좁은 칸에만 둔다. 화살표가 글자를 지나가지 않는다.

## Components

- **구역 라벨(kicker):** 제목 위 20px, primary. 지금 몇 번째 묶음인지 알려 준다. 사례 장처럼 성격을 덧붙일 때도 묶음 번호와 이름을 먼저 쓴다(예: '04 그림으로 먼저 확인하기 · 사례').
- **카드:** 제목 1줄 + 설명 1~2줄. 한 카드에 설명이 3줄을 넘으면 문구를 줄이거나 카드 수를 줄인다.
- **칩:** '예전/지금', '좋은 예/피할 예', 단계 이름처럼 카드의 성격을 한두 단어로 표시한다. 필요하면 '이름 · 짧은 설명'으로 쓰되 한 줄, 공백 포함 20자 이내로 쓴다. 더 긴 설명은 카드 제목이나 본문으로 옮긴다.
- **핵심 한 줄(take):** 슬라이드 맨 아래 한 줄로 결론을 준다. 주의 문장은 `take warn`을 쓴다.
- **되돌림 띠(back):** 단계 흐름에서 '틀리면 되돌아간다' 같은 반복 조건을 점선 띠로 보여 준다.
- **코드 상자:** 복사해서 쓰는 요청문과 파일 내용 예시(`code`, 본문 글꼴 23px). 파일 예시는 맨 위에 파일 경로(Menlo)를 적는다. 괄호 속 회색 글자는 채워 넣을 자리다. 형식 자체를 보여 줄 때만 `code mono`(Menlo 21px)를 쓴다.
- **구분 슬라이드:** 남색 배경, 주황 번호, 제목, 한 줄 설명.
- **화면 캡처(shot):** 실제 사이트의 전체 모습을 비교할 때 쓴다. 16:10으로 위쪽을 기준으로 자르고 테두리 2px를 둔다. 캡처 속 글자는 크기 기준에서 제외한다. knollab-001 캡처는 `slides/build/capture.sh`로 다시 만든다.
- **큰 숫자(big):** 결과 수치 비교(예: 74% → 81%)에 쓴다. 기본 110px, 두 칸 배치 안에서는 84px(`big sm`).

## Do's and Don'ts

- 한 장에 한 메시지. 제목은 분류명보다 결론 문장으로 쓴다.
- 용어는 목록으로 늘어놓지 않는다. 용어는 칩이나 괄호로 붙이고, 비유와 사용 장면을 함께 보여 준다.
- 강사가 AI에게 한 제작 요청(예: '카드 6개로', '비유 넣기')을 화면 문구로 옮기지 않는다.
- 글자 크기를 줄여 넘침을 해결하지 않는다. 순서: 중복 삭제 → 문구 축약 → 대본으로 이동 → 요소 줄이기 → 레이아웃 변경 → 슬라이드 분리.
- 색만으로 맞음·틀림을 구분하지 않는다.
- 도구 기능·요금처럼 바뀌는 정보는 바닥글에 출처와 확인 날짜를 적는다.
- 이모지와 장식용 아이콘에 의미를 맡기지 않는다.

## 제작과 검증

1. `slides/build/part1.html`, `part2.html`을 고친다(공통 스타일은 `deck.css`).
2. `slides/build/build.sh part1`(또는 `part2`)로 PDF를 만든다. Chrome headless가 `slides/pdf/`에 PDF를 쓰고, `qa.js` 자동 검사 결과를 출력한다.
3. 자동 검사는 넘침, 본문 영역 밖 글자, 최소 글자 크기 미달(그 밖의 글자 20px, 참고 자료 목록 17px, 바닥글 14px, 목업 제외), 안전영역 이탈, 상자 겹침을 찾는다. 결과가 `OK`가 아니면 고친 뒤 다시 만든다.
4. `python3 contact.py <pdf> <이름>`으로 6장씩 모은 검수 이미지를 만들어 눈으로 확인한다(어색한 줄바꿈, 정보 위계, 목업).
5. `pdffonts`로 글꼴이 모두 포함(emb yes)됐는지, `pdftotext`로 대체 문자(�)가 없는지 확인한다.
6. 같은 문제가 두 번 나오면 이 문서 또는 `CONTENT_STYLE_GUIDE.md`에 규칙을 더하고 `docs/GUIDELINE_CHANGELOG.md`에 이유를 적는다.

## 인쇄용 안내문 (A4)

- 원본 `slides/build/handout.html`, 스타일 `handout.css`, 검사 `handout-qa.js`. `./build.sh handout`으로 `practice/`에 PDF를 만든다.
- A4 세로, 여백 위 10mm·좌우 12mm·아래 8mm. 앞뒤 2쪽을 넘기지 않는다.
- 최소 글자: 본문·설명 9pt, 바닥글 8pt. 제목 17~20pt, 구역 제목 12pt.
- 흑백으로 인쇄해도 읽히게 만든다. 색 대신 선·굵기·위치로 구분하고, 확인 상자와 쓰는 줄은 선으로 그린다.
- 슬라이드 쪽 번호로 내용을 가리키지 않는다(쪽 번호는 바뀔 수 있다). 요청문은 `practice/README.md`와 같은 문장을 쓰고, 슬라이드와는 같은 요청을 쓴다. 채팅 AI용으로 줄이거나 바꾼 줄이 있으면 대본에 그 이유를 밝힌다.
- 확인: 자동 검사 결과 `OK`, `pdftoppm -gray`로 만든 흑백 이미지를 눈으로 본다.
