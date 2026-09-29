# slides

## 현재 발표용 파일 (v21)

```text
slides/
├─ build/                     # 편집 원본과 제작 도구
│  ├─ part1.html              # 1부 원본 (44쪽)
│  ├─ part2.html              # 2부 원본 (41쪽)
│  ├─ deck.css                # 공통 스타일 (DESIGN.md와 같은 값)
│  ├─ qa.js                   # 렌더링 자동 검사
│  ├─ build.sh                # PDF 생성 + 검사
│  └─ contact.py              # 검수 이미지 생성 (renders/는 git 제외)
└─ pdf/
   ├─ osung_ai_digital_problem_solving_part1_workspace_v21_20260930.pdf
   └─ osung_ai_digital_problem_solving_part2_ux_implementation_v21_20260930.pdf
```

- 표제는 1부·2부 모두 `4. AI·디지털 문제해결 실무 과정`, 부 이름은 부제로 둔다.
- v20 이전 PPTX/PDF는 이 저장소에 올라온 적이 없다. v21은 HTML 원본에서 다시 만들었다.

## 고치고 다시 만드는 법 (macOS)

```bash
cd slides/build
./build.sh part1            # 또는 part2 → ../pdf/에 PDF 생성, 'QA ... OK'가 나와야 한다
python3 contact.py ../pdf/<파일>.pdf p1    # renders/에 6쪽씩 검수 이미지
```

- 필요한 것: Google Chrome, poppler(`brew install poppler`), Python 3 + Pillow
- 글자가 넘치면 글자 크기를 줄이지 말고 `DESIGN.md`의 순서(중복 삭제 → 축약 → 대본 이동 → 요소 줄이기 → 레이아웃 변경 → 분리)를 따른다.
- 새 버전은 파일명의 `v21`과 날짜를 올리고, `docs/pdf_validation_v*.md`에 검수 결과를 남긴다.
