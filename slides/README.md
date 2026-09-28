# slides

강의용 편집 원본과 최종 발표 PDF를 분리해 관리한다.

## 표제 규칙

1부와 2부 파일의 표제는 모두 동일하게 유지한다.

> **4. AI·디지털 문제해결 실무 과정**

1부와 2부의 구분명은 표제가 아니라 부제로 넣는다.

## 현재 발표용 파일

```text
slides/
├─ source/
│  ├─ osung_ai_digital_problem_solving_master_v17_20260930.pptx
│  ├─ osung_ai_digital_problem_solving_part1_workspace_v19_final2_20260930.pptx
│  └─ osung_ai_digital_problem_solving_part2_ux_implementation_v19_final2_20260930.pptx
└─ pdf/
   ├─ osung_ai_digital_problem_solving_part1_workspace_v19_final2_20260930.pdf
   └─ osung_ai_digital_problem_solving_part2_ux_implementation_v19_final2_20260930.pdf
```

## 파일 역할

- `master`: 전체 흐름 보존 및 통합 편집 기준
- `part1`: 표제는 `4. AI·디지털 문제해결 실무 과정`, 부제는 `1부. 문제 정의와 AI 작업환경`
- `part2`: 표제는 `4. AI·디지털 문제해결 실무 과정`, 부제는 `2부. UX/UI 설계와 구현·검증 실습`

## v19 정리 내용

- 도형과 화살표가 맞지 않던 도식을 카드형 흐름으로 재배치했다.
- 2부에 잘못 들어간 개발 기초 중복 슬라이드를 제거하고, `Figma`, `Figma MCP`, `Stitch → Antigravity` 설명을 복원했다.
- 1부·2부 표지에서 본 표제와 부제를 구분했다.
- PDF 렌더링 후 contact sheet와 spotcheck 이미지로 검수했다.

## 관리 원칙

- 실제 발표는 1부·2부 분할본을 사용한다.
- 원본 수정 전 `../DESIGN.md`를 확인한다.
- 화면 비율은 16:9를 유지한다.
- PDF 생성 후 전 페이지 렌더링 검수를 수행한다.
- 새 버전은 기존 파일을 덮어쓰기보다 버전명과 날짜를 명확히 적는다.
- GitHub에서 바이너리 업로드가 어려운 경우, 이 README와 docs의 manifest를 기준으로 산출물명을 관리한다.
