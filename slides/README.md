# slides

## 현재 발표용 파일 (v23)

```text
slides/
├─ build/                       # 편집 원본과 제작 도구
│  ├─ part1.html                # 1부 원본 (42쪽)
│  ├─ part2.html                # 2부 원본 (35쪽)
│  ├─ handout.html              # 인쇄용 안내문 원본 (A4 앞뒤)
│  ├─ deck.css · handout.css    # 스타일 (DESIGN.md와 같은 값)
│  ├─ qa.js · handout-qa.js     # 렌더링 자동 검사
│  ├─ build.sh                  # PDF 생성 + 검사
│  ├─ capture.sh                # knollab-001 사이트 첫 화면 캡처
│  ├─ assets/knollab-001/       # 캡처 이미지 (2부 20쪽)
│  └─ contact.py                # 검수 이미지 생성 (renders/는 git 제외)
└─ pdf/
   ├─ osung_ai_digital_problem_solving_part1_workspace_v23_20260930.pdf         # 현재
   ├─ osung_ai_digital_problem_solving_part2_ux_implementation_v23_20260930.pdf # 현재
   └─ *_v22_20260930.pdf · *_v21_20260930.pdf                                    # 이전 버전
```

- 인쇄용 안내문 PDF는 `practice/`에 만들어진다.
- 표제는 1부·2부 모두 `4. AI·디지털 문제해결 실무 과정`, 부 이름은 부제로 둔다.
- v20 이전 PPTX/PDF는 이 저장소에 올라온 적이 없다. v21부터 HTML 원본에서 만든다.

## 고치고 다시 만드는 법 (macOS)

```bash
cd slides/build
./build.sh part1            # 또는 part2, handout → PDF 생성, 'QA ... OK'가 나와야 한다
./capture.sh                # knollab-001 사이트가 바뀌었을 때만. 그다음 ./build.sh part2
python3 contact.py ../pdf/<파일>.pdf p1    # renders/에 6쪽씩 검수 이미지
```

- 필요한 것: Google Chrome, poppler(`brew install poppler`), Python 3 + Pillow
- 글자가 넘치면 글자 크기를 줄이지 말고 `DESIGN.md`의 순서(중복 삭제 → 축약 → 대본 이동 → 요소 줄이기 → 레이아웃 변경 → 분리)를 따른다.
- 쪽을 더하거나 합치면 `docs/03_speaker_script.md`와 `docs/02_slide_outline.md`의 쪽 번호도 함께 고친다.
- 새 버전은 파일명의 버전과 날짜를 올리고, `docs/pdf_validation_v*.md`에 검수 결과를 남긴다.

## Windows와 macOS 공통 제작

Playwright가 설치된 Node.js와 Chrome 또는 Edge를 사용한다. `CHROME_PATH`로 브라우저 실행 파일을 지정할 수 있다. 공통 스타일과 한글 글꼴의 실제 출력 차이를 자동 검사한다.

```text
node slides/build/build.cjs all
python slides/build/package_materials.py
```

두 번째 명령은 발표 대본 PDF와 강의자료 ZIP을 만든다. Python에 reportlab이 필요하다. Windows는 맑은 고딕을 사용하고, 다른 환경은 `KOREAN_FONT`·`KOREAN_BOLD_FONT`에 한글 TTF 경로를 지정한다. 모든 PDF의 시각 검수와 `docs/pdf_validation_v23.md` 기록을 마친 뒤 배포한다.
