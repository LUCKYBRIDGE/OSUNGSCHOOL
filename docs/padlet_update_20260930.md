# Padlet 정리·검수 기록

확인일: 2026.9.30 · 강릉오성학교 연수

[수정한 Padlet](https://padlet.com/lucky20220528/260930-jhtj91ryy8mwbvog) · [재사용할 안내문 원본](../practice/ai_setup_and_install_20260930.md)

## 섹션 구성과 게시글 배치

기존 13개 섹션을 9개로 통합했다. 출석 → 강의·실습 → AI 준비 → 필요한 연결 → 화면 설계·공유 → 시연 순서로 읽는다. 이전 연수 자료와 보조 도구는 뒤쪽에 두었다.

| 섹션 | 남긴 자료와 읽는 순서 |
|---|---|
| 01 · 출석·만족도 | 기존 출석 QR·만족도 조사 |
| 02 · 강의·실습 자료 | 고정한 읽는 순서 → v22 1부·2부 PDF·인쇄 안내문 → AI 하나로 실습 시작 |
| 03 · AI 선택·환경 준비 | 고정한 환경 준비 팁 → OpenCode·ChatGPT/Codex·Claude 안내 → 비용 비교·리셋 확인. Kiro·Aside는 선택 도구 |
| 04 · MCP·Skill 설치 | 고정한 개념 안내 → 쓰는 앱의 설치 글 하나 → handoff·teacher 요청문. 플러그인의 역할과 로그인도 이곳에서 설명 |
| 05 · 화면 설계·공유 | 고정한 시연 허브 → 화면 기준·선택 시안·Figma → 카페 주문 비교 → GitHub 보관·Pages 공유 → 완료 확인 |
| 06 · 화면 시연·단축키 | Windows 창 정리·작업 보기·캡처와 ZoomIt 설치·확대·판서·저장 |
| 07 · 퀴즈 제작·공유 (이전 연수) | 예전 교안 → 활동지·문항 생성·CSV·공유의 네 단계 → 도구별 무료 범위·제작 팁·예제 |
| 08 · 바이브코딩 예제 (이전 연수) | 예전 코드 교안·공개 예제·참여자 결과·웹 시작 파일 설명 |
| 09 · 문서·PDF 도구 (참고) | TXT 병합 링크·PDF24 공식 설치 안내와 이전 첨부 |

‘도구 설치 및 활용 1’, Windows 단축키, AI 퀴즈 제작, 퀴즈 링크 공유 섹션은 게시물을 해당 목적의 섹션으로 이동한 뒤 비운 섹션만 정리했다. 기존 게시글을 삭제하거나 첨부를 교체하지 않았다. 제목은 ‘파일 보관’, ‘화면 공유’, ‘비교 실습’처럼 할 일이 보이는 말로 바꿨다. 화면에서 끝 글자만 다음 줄로 밀리던 섹션 제목은 축약했다.

새 글 8개: 읽는 순서, 환경 준비 분담, 비용 비교, 사용량 리셋, Codex·Antigravity·Claude Code 설치 안내 3개, 학생이 쓸 화면의 완료 확인.

## 최신 사실과 강사의 사용 경험 구분

| 내용 | 반영한 판단과 근거 |
|---|---|
| Claude 모델 | Sonnet 5.5(9/28), Opus 5.5(9/22)의 공식 발표와 API 요금을 확인했다. 강사의 최근 만족도는 사용 경험으로 적고 모든 과제의 압도적 우위로 일반화하지 않았다. [Sonnet](https://www.anthropic.com/claude-sonnet-5-5) · [Opus](https://www.anthropic.com/claude-opus-5-5) |
| 가격 비교 | 표준 API의 입력·출력 단가를 비교하고 짧은 컨텍스트 조건을 표시했다. 월 구독의 가성비나 사용량과 혼동하지 않도록 설명했다. [OpenAI 공식 가격](https://developers.openai.com/api/docs/pricing) |
| 환경 준비 | 준비 담당과 본 작업 담당을 나누고 인계 문서로 재사용하도록 했다. Muse Spark 1.3 Contributor Free·Space Bunny Free의 제공 조건과 Gemini의 공급자별 요금 차이를 설명했다. 숨겨진 모델 정체를 추측하지 않았다. [OpenCode Zen](https://opencode.ai/docs/zen/) · [Gemini 3.8 Flash](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash) |
| 사용량 리셋 | [When Codex Reset](https://whencodexreset.com/)과 [Codex Reset Tracker](https://codex-reset-tracker.com/)를 비공식 기록 사이트로 추가했다. 공지 링크의 대상과 날짜를 확인하도록 하고, 공통 리셋과 저장한 리셋을 구분했다. 정기 혜택이나 모든 계정의 초기화로 보장하지 않았다. [저장한 Codex 리셋 공식 안내](https://help.openai.com/en/articles/20001498-how-banked-codex-resets-work) |
| 설치·Skill | 앱별 프로젝트 범위·경로·명령·호출 확인 방법을 넣었다. handoff·teacher는 사용자 정의 이름이며 공식 패키지 이름으로 다운로드 주소를 추측하지 않도록 했다. [Codex MCP](https://learn.chatgpt.com/docs/extend/mcp) · [Codex Skill](https://learn.chatgpt.com/docs/build-skills) · [Antigravity MCP](https://antigravity.google/docs/mcp) · [Antigravity Skill](https://antigravity.google/docs/skills?pubdate=20251130) · [Claude Code MCP](https://code.claude.com/docs/en/mcp) · [Claude Code Skill](https://code.claude.com/docs/de/skills) |
| Figma 교육용 | 학교 이메일만으로 자동 승인되거나 모든 AI 기능이 열리는 것으로 쓰지 않았다. K–12의 AI 기능 범위와 교육용 신청 절차를 구분했다. [교육용 공식 안내](https://help.figma.com/hc/en-us/articles/360041061214-Figma-for-Education) |
| 예전 퀴즈 안내 | 특정 옛 모델을 반드시 선택하는 지시와 여러 계정으로 사용량을 늘리는 팁을 정리했다. 문항·정답·CSV·한글을 실제로 확인하도록 바꿨다. [Blooket 무료 범위](https://help.blooket.com/hc/en-us/articles/17351034967959-Is-Blooket-Free) · [Gimkit 참가 한도](https://help.gimkit.com/en/article/player-maximums-18mbcz0/) · [Kahoot 참가 한도](https://support.kahoot.com/hc/en-us/articles/115003072287-How-many-participants-can-play-a-kahoot) |
| 보조 도구·웹 설명 | ZoomIt의 현재 공식 다운로드와 단축키를 연결했다. PDF24의 이전 첨부가 최신 파일을 보장하지 않는다고 표시했다. ‘시작 파일은 무조건 index.html’이라는 설명과 시대에 맞지 않는 웹 역사 비유를 수정했다. [ZoomIt](https://learn.microsoft.com/en-gb/sysinternals/downloads/zoomit) · [PDF24](https://tools.pdf24.org/en/creator) · [GitHub Pages 시작 파일](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site) |

## 검수 결과

- Padlet의 전체 마크다운 내보내기에서 최종 **9개 섹션·63개 게시물**을 확인했다. 작업 시작 시 기존 게시물은 55개였다. 정리 직전 전체 백업은 환경 팁을 먼저 추가한 뒤라 56개이며, 이후 7개를 추가했다.
- 정리 직전·후 내보내기의 **첨부 항목 43개, 첨부 대상 경로 41개, 댓글 3개**를 비교했다. 기존 첨부 경로와 댓글 내용의 누락은 0건이다. 만료 토큰은 비교에서 제외했다.
- 추가·수정 안내문 14개의 제목이 모두 최종 내보내기에 존재한다. 화면 기준·GitHub·ZoomIt 제목도 저장 후 확인했다.
- `.md` 파일명이 `http://HANDOFF.md` 같은 웹주소로 자동 연결된 부분을 코드 형식으로 고쳤다. 최종 내보내기에서 해당 잘못된 링크는 0건이다.
- 좁은 열에서 섹션 제목과 고정 안내문을 실제 화면으로 확인했다. 읽는 순서·환경 팁·개념 안내·시연 허브를 해당 섹션 맨 위에 고정했다.
- 앱별 설치 안내는 공식 문서와 대조했다. 이번 요청은 설명문 작성이므로 사용자 PC에 MCP·Skill을 실제 설치하지 않았으며, 실제 설치 성공으로 기록하지 않는다. 안내문에 연결 상태·문서 검색·Skill 경로 확인 절차를 포함했다.
- 본 작업은 Padlet의 보조 안내·참고자료 정리다. 현재 발표용 v22 PDF·HTML과 대본의 강의 순서를 변경하지 않았다. 기본 실습을 AI 하나로 시작하는 흐름과 일치하는지 확인했다.
- 전체 원본 내보내기·작업 중 백업·화면 캡처는 `.local/padlet_20260930/`에 보관하고 Git에서 제외한다. 작성자 정보·만료 토큰이 포함된 원본을 저장소 안내문으로 복제하지 않는다.
- 저장소 문서의 공백 오류, 설정 JSON 예제, 로컬 링크, 원본 토큰의 혼입 여부를 확인했다. 반복된 게시판 검수·자동 링크 문제는 `AGENTS.md`와 지침 변경 기록에 반영했다.
