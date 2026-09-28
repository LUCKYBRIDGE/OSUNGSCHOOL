# slides

강의용 편집 원본과 최종 발표 PDF를 분리해 관리한다.

## 현재 발표용 파일

```text
slides/
├─ source/
│  ├─ osung_ai_digital_problem_solving_master_v17_20260930.pptx
│  ├─ osung_ai_digital_problem_solving_part1_workspace_20260930.pptx
│  └─ osung_ai_digital_problem_solving_part2_ux_implementation_20260930.pptx
└─ pdf/
   ├─ osung_ai_digital_problem_solving_part1_workspace_20260930.pdf
   └─ osung_ai_digital_problem_solving_part2_ux_implementation_20260930.pdf
```

## 파일 역할

- `master`: 전체 흐름 보존 및 통합 편집 기준
- `part1`: 문제 정의, 최소 개발 지식, 하네스, 작업공간, Handoff
- `part2`: UX/UI, DESIGN.md, 디자인 도구, 구현·검증·배포, 실습

## 관리 원칙

- 실제 발표는 1부·2부 분할본을 사용한다.
- 원본 수정 전 `../DESIGN.md`를 확인한다.
- 화면 비율은 16:9를 유지한다.
- PDF 생성 후 전 페이지 렌더링 검수를 수행한다.
- 새 버전은 기존 파일을 덮어쓰기보다 버전명과 날짜를 명확히 적는다.
- GitHub에서 바이너리 업로드가 어려운 경우, 이 README와 docs의 manifest를 기준으로 산출물명을 관리한다.
