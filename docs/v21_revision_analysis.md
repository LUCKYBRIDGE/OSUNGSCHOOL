# v21 전면 재제작: 문제 분석과 변경 내용

- 작업일: 2026-09-29
- 대상: 1부·2부 발표 자료 전체
- 근거 자료: v20 PPTX/PDF 원본이 저장소에 없어서 `docs/02_slide_outline.md`(v1 55장), `docs/07_beginner_revision_plan.md`, `docs/08_beginner_v2_changes.md`, `docs/lecture_flow_split_20260930.md`, v19·v20 검수 기록으로 기존 구성을 분석했다.

## 1. 기존 자료의 문제

### 1) 제작 요청이 그대로 화면 문구가 됨

- `Harness Engineering`, `Loop Engineering`, `Graph Engineering`, `Rules / AGENTS.md / CLAUDE.md`, `Docs`, `Skills`, `Agents`, `Hooks`, `Commands / Workflows`, `Memory / Handoff`, `MCP / Tools`가 제목만 바뀐 채 9장 넘게 이어졌다. 각 장은 명사 목록이어서 교사에게는 용어 사전처럼 읽혔다.
- `Implementation-01 → HANDOFF.md → Implementation-02`, `/plan /review /verify`, `PROJECT_OVERVIEW.md / ARCHITECTURE.md / UX_SPEC.md / DATABASE.md / API_SPEC.md`처럼 개발자 작업 메모가 화면에 올라갔다.
- `Harness · Loop · Graph를 한 문장으로`, `조직 / 루틴 / 인계 흐름`처럼 강사의 정리 메모가 슬라이드 결론으로 쓰였다.

### 2) 사실과 표현의 문제

- 'Loop Engineering', 'Graph Engineering'은 널리 쓰이는 공식 용어가 아닌데 'Harness Engineering'과 같은 급의 분야처럼 제시됐다.
- ECC를 '2026년 2월경 해커톤 우승 사례'로 적었다. 확인 결과 해커톤은 2025년(뉴욕, Anthropic x Forum Ventures), 저장소 공개는 2026년 1월이다.
- Claude Design을 '베타'로 적었다. 공식 발표는 2026. 4. 출시된 유료 플랜 대상 '연구 프리뷰'다.
- `/plan`, `/review`, `/verify`를 여러 도구에 공통인 명령처럼 보여 줬다. 명령 이름은 도구와 설정마다 다르다.
- '문서 설계는 논리를, 이미지 도안은 사용성을 확인한다', '기술 선택 시 CPU/RAM 하나보다…'처럼 근거가 약하거나 맥락 없는 문장이 있었다.

### 3) 순서와 중복

- Loop가 네 번(구현 루프, 종료 조건, 개발 루프, 배포 후 루프), Handoff가 두 번 처음부터 다시 설명됐다.
- ECC 사례가 구성요소 설명보다 먼저 나오고, 'ECC에서 가져올 것'이 구성요소를 배우기 전에 나왔다.
- 디자인 도구 다섯 가지(ChatGPT/Gemini, Stitch, Claude Design, Figma, Figma MCP)가 한 장씩 이어져 도구 목록처럼 보였다.

### 4) 디자인

- 원형 아이콘 하나와 짧은 목록만 있는 장과 설명·도식이 과밀한 장이 섞여 밀도 차이가 컸다.
- 원형 Loop 도식, 교차 화살표 등은 v19·v20에서 이미 문제로 기록됐다.

## 2. 바꾼 원칙

1. 제목은 용어가 아니라 결론 문장으로 쓴다. 용어는 구역 라벨이나 괄호로만 붙인다.
2. 용어는 '비유 → 실제 모습 → 사용 장면'으로 한 번만 설명하고, 전체 지도(학교 업무 체계 비유 표)를 먼저 보여 준다.
3. 개념은 모두 하나의 예시(카페 주문 연습 자료)로 이어서 보여 준다.
4. 도구 소개는 '언제 무엇을 쓰나' 표 한 장과 사례 두 장으로 줄인다.
5. 바뀌는 정보(도구 기능·요금·경로)는 2026. 9. 공식 문서로 다시 확인하고 바닥글에 출처를 적는다.

## 3. 새 구성

- 1부 44쪽: 작은 불편 → 최소 개발 지식 → 질문에서 작업환경으로(하네스, 공개 사례) → 작업환경 구성 → 작업공간과 인계 → 요청문
- 2부 41쪽: 잘 쓰이는 화면 → 특수교육 화면 원칙 → DESIGN.md → 그림 시안과 도구 → 구현·검증·배포 → 실습
- 쪽별 목적과 말할 핵심: `docs/02_slide_outline.md`

## 4. 삭제·통합한 내용

| 기존 | 처리 |
|---|---|
| Harness / Loop / Graph Engineering 각 1장 + 한 문장 정리 | 하네스 정의 1장(OpenAI 근거) + 완료 기준 루프 1장 + 역할 나누기 1장으로 통합 |
| Rules·Docs·Skills·Agents·Hooks·Commands·Memory·MCP 개별 장 | 학교 비유 지도 1장 + 규칙·문서·스킬·에이전트·도구 연결·확인 6장(모두 같은 예시) |
| Commands / Workflows, Hooks | 초보 교사용 최소 구성에서 제외. 필요 시 대본에서만 언급 |
| 도구가 달라도 개념은 비슷하다(추상 비교) | 2026. 9. 공식 문서 기준 파일 위치 표로 교체 |
| 토큰을 아끼는 가장 좋은 방법 | '규칙은 짧게', '한 번에 하나', '인계 파일' 슬라이드로 흡수 |
| 디자인 도구 개별 5장 | 도구 선택 표 + Stitch·Claude Design 1장 + Figma 1장 + 공통 흐름 1장 |
| 이미지 자료 도구 통일 | 삭제(개인정보·저작권 주의는 배포 슬라이드로 이동) |

## 5. 새로 넣은 내용

- 문제를 한 문장으로 적는 틀, 사용 조건 표, 조건에 따라 만드는 방식이 바뀌는 예
- AI가 묻는 질문에 교사가 답하는 대화 예시
- OpenAI 하네스 엔지니어링의 교훈('더 잘해' 대신 빠진 것을 파일로)
- Built with Opus 4.7 해커톤 수상자와 '현장 지식 파일 하나로 74%→81%' 사례
- 틀렸을 때 도움을 단계적으로 늘리는 화면, 학생별 조절 설정
- 교사가 직접 하는 5분 확인, 배포 후 관찰 기록 방법, 막혔을 때 요청문
