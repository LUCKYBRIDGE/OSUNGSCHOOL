# AI 환경 준비·MCP·Skill 설치 안내

강릉오성학교 · 2026.9.30 확인

[연수 자료 Padlet](https://padlet.com/lucky20220528/260930-jhtj91ryy8mwbvog)의 추가 안내문 원본입니다. 기본 실습은 로그인된 AI 하나로 시작합니다. 환경 구축·외부 도구 연결·Skill은 필요한 경우에 선택합니다.

모델·요금·메뉴·제공 범위는 확인일 기준입니다. 공식 사실과 강사의 사용 경험을 구분하며, 설치한 것으로 간주하지 않고 각 앱에서 실제 연결을 확인합니다.

## 읽는 순서 · 오늘은 AI 하나와 연습 자료 하나

오늘의 목표는 우리 반에서 써 볼 연습 자료 하나를 만들고 직접 확인하는 것입니다.

1. 이 섹션의 1부·2부 PDF와 참석자용 안내문을 엽니다.
2. ‘오늘 실습 시작’의 요청문을 로그인된 AI 하나에 입력합니다. 여러 도구를 설치할 필요는 없습니다.
3. ‘AI 선택·환경 준비’는 모델 선택과 환경 구축이 필요할 때 읽습니다.
4. ‘MCP·Skill 설치’는 외부 서비스 연결이나 반복 작업이 필요할 때 읽습니다. 자신이 쓰는 앱의 글 하나만 따라 하세요.
5. ‘화면 설계·공유’에서 화면 기준과 시연을 보고, 만든 화면을 직접 눌러 확인합니다.
6. 확대·판서가 필요하면 ‘화면 시연·단축키’를 참고합니다.

문제·학생의 사용 조건 → 작업 규칙과 개요 → 화면 기준 → 한 화면 구현 → 직접 확인 → 수정 순서입니다. 실제 학생 이름·사진·진단명·개별 기록은 입력하지 않고 가상 사례로 연습합니다.

7. ‘07 · 과제 안내’에서 과제 1로 아이디어를 정리하고, 과제 2·3·4 중 하나를 선택합니다. 예시 개요·설계·요청문은 ZIP으로 받거나 GitHub에서 복사합니다.
8. ‘08 · 결과물 제출’에 새 글로 결과와 공통 문서를 올리고, 열어 보는 방법과 직접 확인한 내용을 적습니다.

9~11번 섹션은 이전 연수와 보조 도구의 참고자료입니다. 오늘 실습을 마친 뒤 필요한 내용만 살펴보세요.

모델·가격·설치 안내의 확인 기준일은 2026.9.30입니다. 강사의 사용 소감과 공식 확인 사실을 구분해 적었습니다.

## AI 사용 팁 · 환경 구축은 다른 AI에 맡겨도 됩니다

환경이 중요해도 매번 주력 AI의 사용량을 설치와 오류 해결에 쓸 필요는 없습니다. 환경 준비와 본 작업을 나눠 맡겨 보세요.

1. 준비 담당: OpenCode의 Space Bunny Free·Muse Spark 1.3 Contributor Free, 또는 Gemini 3.8 Flash 등 무료·저비용 후보로 환경과 실행 방법을 확인합니다. 실제 제공 모델·요금은 사용하는 공급자에서 확인합니다.
2. 본 작업 담당: Claude·Codex 등 자신에게 결과가 좋았던 AI로 수업 설계·구현·중요한 검증을 이어갑니다.
3. 인계: 같은 프로젝트 폴더의 규칙·개요·화면 기준·인계 문서를 읽히면 다시 설명하는 양이 줄어듭니다. 준비 담당의 결과도 본 작업 담당이 한 번 실행해 확인합니다.

준비 담당에게 복사할 문장
```text
이 프로젝트의 기존 규칙과 파일을 읽고 현재 환경을 먼저 점검해줘. 이미 되는 것은 다시 설치하지 말고 필요한 도구만 공식 설치법으로 준비해줘. 유료 모델·자동 결제를 새로 켜지 마. 실행과 확인까지 끝낸 뒤 버전, 재현 가능한 명령, 확인 결과, 미해결 문제를 HANDOFF.md에 기록해줘. 학생 개인정보와 비밀 키는 포함하지 마.
```

본 작업 담당에게 복사할 문장
```text
AGENTS.md, PROJECT_OVERVIEW.md, DESIGN.md, HANDOFF.md를 먼저 읽어줘. 인계된 실행 방법을 확인하고, 이번 목표에 필요한 한 화면부터 작업해줘. 기록과 실제 상태가 다르면 실제 확인 결과를 기준으로 인계 문서를 고쳐줘.
```

한 번 만든 환경은 문서·실행 명령으로 재사용하고 바뀐 부분만 점검하세요. 브라우저 채팅만으로 가능한 오늘 기본 실습에는 코딩 도구 설치가 필요하지 않습니다.

### OpenCode에서 준비 담당 고르기

OpenCode에서 `/connect`로 Zen을 연결하고 `/models`에서 실제 제공되는 Free 항목을 확인합니다. Space Bunny Free와 Muse Spark 1.3 Contributor Free의 무료 제공은 영구 보장이 아닙니다. Gemini 3.8 Flash는 공급자와 연결 방식에 따라 과금이 달라집니다. Space Bunny의 숨겨진 모델 정체나 특정 Claude 모델과의 동일성을 단정하지 않습니다.

[OpenCode Zen 공식 안내](https://opencode.ai/docs/zen/) · [Gemini 3.8 Flash 공식 모델 안내](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash)

## 가성비 비교 · 모델 가격과 구독 한도는 다릅니다

2026.9.30 기준 · “어느 AI가 가장 싸고 좋다”보다 같은 과제를 끝내는 데 든 비용·시간·수정 횟수를 비교하세요.

공식 API 표준 요금 / 각 100만 토큰 / 입력 → 출력
• Claude Sonnet 5.5: $2 → $10
• Claude Opus 5.5: $4 → $20
• GPT-6.1 Sol: $2 → $10 (짧은 컨텍스트 기준)
• GPT-6 Astra: $10 → $50 (짧은 컨텍스트 기준)

단가만 보면 Sonnet 5.5와 GPT-6.1 Sol은 같은 수준입니다. 추론 강도·답변 길이·재시도·캐시·긴 컨텍스트에 따라 실제 비용은 달라집니다. 이 표로 월 구독의 가성비나 모든 과제의 성능 순위를 판정할 수는 없습니다.

교사에게 권하는 비교: 같은 ‘카페 주문 연습 화면’ 요청, 같은 학생 조건, 같은 완료 기준으로 두 모델을 써 봅니다. 원하는 결과까지 몇 번 고쳤는지, 학생이 선택과 되돌아가기를 이해하는지 함께 확인합니다.

API는 사용량에 따른 별도 과금입니다. ChatGPT·Claude·Google 앱의 무료/구독 사용량은 각 서비스의 내 계정 화면에서 확인하세요. Gemini 3.8 Flash도 공급자에 따라 가격이 다릅니다.
공식 가격: [developers.openai.com](https://developers.openai.com/api/docs/pricing)
[www.anthropic.com](https://www.anthropic.com/claude-sonnet-5-5)
[www.anthropic.com](https://www.anthropic.com/claude-opus-5-5)
[ai.google.dev](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash)

## 사용량 리셋 · 기록 사이트와 내 계정 확인

Codex 추가 리셋 공지를 모아 보는 사이트입니다. OpenAI 공식 서비스가 아닌 커뮤니티 기록 사이트이며, 개인 계정의 잔여 사용량을 보여 주는 화면은 아닙니다.

Reset, yet? · 공지 기록·원문 링크
[whencodexreset.com](https://whencodexreset.com/)
Codex Reset Tracker · 적용 범위와 확인 시점이 표시된 기록
[codex-reset-tracker.com](https://codex-reset-tracker.com/)

각 기록의 Tibo(@thsottiaux) 원문 공지에서 대상 계정과 적용 범위를 확인하세요. 두 사이트의 기록 범위·갱신 시점이 달라 가장 최근 날짜가 다를 수 있습니다. 사이트의 ‘오늘 리셋’ 표시나 다음 리셋 예측은 내 계정 적용을 보장하지 않습니다.

구분해서 보기
• 정규 사용량 회복: 내 계정에 표시된 사용량 창과 회복 시간.
• global reset: 대상 계정에 바로 적용되는 추가 리셋.
• banked reset: 내 계정에 저장된 일회성 리셋. 사용 또는 만료 전까지 보관되며, 적용 버튼을 눌러 사용합니다.

banked reset은 영구적인 한도 증가나 API 크레딧이 아닙니다. 대상·만료일은 프로모션마다 다르고, 앞으로 리셋이 계속 제공된다는 보장은 없습니다. Codex Settings → Usage에서 남은 양, 사용 가능한 리셋, 만료일을 확인하세요.
공식 안내: [help.openai.com](https://help.openai.com/en/articles/20001498-how-banked-codex-resets-work)

### ChatGPT·Codex의 용도와 사용량 확인

2026.9.30 확인 · ChatGPT와 Codex는 용도와 사용량 화면을 나눠 확인하세요. 대화로 아이디어·문구를 다듬을 때와, 프로젝트 파일을 고치고 실행·검증할 때의 작업 방식이 다릅니다. 선택 가능한 모델은 앱·요금제·계정에 따라 달라집니다.

Codex의 GPT-6 Astra는 어려운 추론 작업 후보, GPT-6.1 Sol은 일상적인 구현·수정 후보입니다. “항상 무료·거의 무제한”이라는 안내 대신 내 계정의 사용량과 다음 회복 시간을 확인하세요. API 요금은 ChatGPT 구독료와 별도입니다.

강사의 9/30 사용 소감: 최근 Sonnet 5.5·Opus 5.5의 결과와 가성비를 높게 평가합니다. 다만 작업·설정에 따른 경험이며 모든 상황의 순위를 뜻하지 않습니다. ChatGPT의 이미지 생성과 Codex의 작업 환경도 필요한 기능을 기준으로 비교하세요.

추가 사용량 리셋이 제공된 사례는 실제로 있습니다. 계정에 저장해 나중에 쓰는 banked reset과 즉시 적용되는 global reset은 다릅니다. 앞으로 정기적으로 받을 수 있는 혜택으로 보장되지는 않습니다. 이 섹션의 ‘사용량 리셋’ 게시글에서 기록 사이트와 공식 안내를 확인하세요.

공식 요금·모델: [developers.openai.com](https://developers.openai.com/api/docs/pricing)
리셋 공식 안내: [help.openai.com](https://help.openai.com/en/articles/20001498-how-banked-codex-resets-work)

## Claude · Sonnet 5.5와 Opus 5.5 선택

2026.9.30 확인 · Sonnet 5.5는 9/28, Opus 5.5는 9/22 공식 발표되었습니다. 최근 성능·비용을 함께 비교할 만한 모델입니다.

Sonnet 5.5: 범위가 분명한 수정·일상적인 코딩·문서 작업부터 시도해 볼 후보.
Opus 5.5: 여러 조건을 함께 판단하거나 복잡한 문제를 오래 해결해야 할 때 비교할 후보.

강사의 사용 소감은 “최근 Claude의 결과와 가성비가 좋다”입니다. 공개 평가도 강점을 보여 주지만 모든 과제에서 다른 모델을 이긴다는 뜻은 아닙니다. 같은 요청과 완료 기준으로 직접 비교하세요.

추론 강도(effort)는 정답률뿐 아니라 시간·토큰·비용에 영향을 줍니다. “High 이상이면 성능이 저하된다”거나 “Low~Max는 시간만 달라진다”고 일반화할 수 없습니다. 기본 설정으로 시작하고, 복잡한 과제에서 한 단계 높여 실제 결과를 비교하세요.

API 표준 요금: Sonnet 5.5 입력 $2 / 출력 $10, Opus 5.5 입력 $4 / 출력 $20 (각 100만 토큰 기준). 구독 플랜의 사용량과는 별도입니다.
공식 발표: [www.anthropic.com](https://www.anthropic.com/claude-sonnet-5-5)
[www.anthropic.com](https://www.anthropic.com/claude-opus-5-5)

## 먼저 이해하기 · MCP·플러그인·Skill

MCP는 AI가 외부 서비스·자료·도구에 연결되는 통로, Skill은 반복 업무를 위한 작업 매뉴얼, 플러그인은 이런 기능을 묶어 설치하는 꾸러미입니다. 같은 말은 아닙니다.

처음에는 실제 작업에 필요한 것 하나만 연결하세요.
• GitHub: 저장소·이슈·변경 내역 확인. 공식 MCP: [github.com](https://github.com/github/github-mcp-server)
• Figma: 화면 설계 읽기·지원되는 환경에서 수정. 공식 안내: [developers.figma.com](https://developers.figma.com/docs/figma-mcp-server/)
• Playwright: 만든 웹 화면을 열고 버튼·흐름 확인. Microsoft 공식 MCP: [github.com](https://github.com/microsoft/playwright-mcp)
• OpenAI 문서: 설치 예제용 공개 문서 검색. [developers.openai.com](https://developers.openai.com/learn/docs-mcp)

MCP가 있다고 모든 앱에서 바로 쓸 수 있는 것은 아닙니다. 공식 설치 주소, 지원 클라이언트, 로그인·요금 조건을 확인하세요. Cloudflare처럼 배포에 쓰는 서비스는 필요해진 뒤 추가하면 됩니다. Padlet은 이 안내에서 공식 MCP 설치 주소를 확인하지 못해 설치 예시에서 제외했습니다.

아래의 Codex·Antigravity·Claude Code 중 자신이 쓰는 도구의 글 하나만 따라 하세요. 성공 기준은 목록에 이름이 생기는 것 + 연결 상태 정상 + 실제 도구 호출 성공입니다.

## Codex 설치 안내 · MCP와 Skill

2026.9.30 확인 · Codex 앱에서 프로젝트를 연 뒤 따라 하세요. ChatGPT 일반 대화창에 파일 설치 요청만 입력해서는 로컬 프로젝트에 설치되지 않습니다.

MCP 예제: 공개 문서 검색 (로그인 불필요)
Settings → MCP servers → Add server → 이름 openaiDeveloperDocs → Streamable HTTP → URL [developers.openai.com](https://developers.openai.com/mcp) → Save → 앱 재시작. 메뉴가 다른 버전이면 아래 요청문으로 현재 버전의 공식 설치법을 확인합니다.

터미널을 직접 쓰는 경우:
```shell
codex mcp add openaiDeveloperDocs --url https://developers.openai.com/mcp
codex mcp list
```

복사할 요청문
```text
현재 Codex 버전의 공식 문서를 확인하고 openaiDeveloperDocs MCP를 https://developers.openai.com/mcp 로 추가해줘. 기존 설정을 유지하고 같은 이름이 있으면 중복 추가하지 마. 등록 후 연결 상태를 확인하고, 공식 문서 검색 한 번으로 실제 호출을 검증해줘. 앱 재시작이 필요하면 알려줘.
```

Skill
프로젝트의 `.agents/skills/handoff/SKILL.md` 또는 .agents/skills/teacher/SKILL.md에 저장합니다. 이 섹션의 ‘Skill 만들기’ 요청문 끝에 “Codex 프로젝트의 .agents/skills에 만들어줘”를 붙이세요.
공개된 Skill을 가져오려면 $skill-installer에 정확한 GitHub 저장소·Skill 폴더 주소를 줍니다. 공식 목록에서는 실제 패키지 이름을 선택하세요. handoff/teacher라는 이름만으로 다운로드 주소를 추측하지 마세요.

완료 확인
새 채팅에서 $handoff 또는 이름을 지정해 요청하고, 읽은 Skill의 경로를 확인합니다. 감지되지 않으면 앱을 재시작하세요. GitHub·Figma 등은 플러그인 목록에서 공식 항목을 설치하고 별도 로그인·연결을 마쳐야 합니다.
공식 MCP: [learn.chatgpt.com](https://learn.chatgpt.com/docs/extend/mcp)
공식 Skill: [learn.chatgpt.com](https://learn.chatgpt.com/docs/build-skills)

## Antigravity 설치 안내 · MCP와 Skill

2026.9.30 확인 · 프로젝트 폴더를 Antigravity에서 열고 따라 하세요.

MCP 메뉴
Antigravity 2.0: 좌측 아래 Settings → Customizations → Installed MCP Servers → Add MCP → MCP Store에서 필요한 서버 선택 → Add.
Antigravity IDE: Agent 패널의 … → MCP Servers → 필요한 서버 Install. 직접 등록은 Manage MCP Servers → View raw config.

직접 등록 예제 (기존 mcpServers 안에 항목 추가)
```json
{
  "mcpServers": {
    "openaiDeveloperDocs": {
      "serverUrl": "https://developers.openai.com/mcp"
    }
  }
}
```
전체 설정 파일에는 이 항목을 감싼 "mcpServers" 객체가 있어야 합니다. 기존 설정을 통째로 덮어쓰지 마세요.

복사할 요청문
```text
현재 Antigravity 버전의 공식 MCP 안내를 확인하고, 이 프로젝트의 .agents/mcp_config.json에 openaiDeveloperDocs를 serverUrl https://developers.openai.com/mcp 로 추가해줘. 기존 설정은 유지하고 중복을 피하고, 연결 상태와 문서 검색 한 번으로 확인해줘. 사용자 설정이 필요한 경우 적용 범위를 먼저 설명해줘.
```

Skill
프로젝트: `.agents/skills/handoff/SKILL.md`
개인 공통: `~/.gemini/config/skills/handoff/SKILL.md`
teacher도 같은 방식입니다. ‘Skill 만들기’ 요청문 끝에 “Antigravity 프로젝트의 .agents/skills에 만들어줘”를 붙이세요. 프로젝트 폴더에 만들면 다른 프로젝트에 불필요하게 적용되지 않습니다.

완료 확인
새 대화에서 /handoff 또는 이름을 지정해 실행합니다. MCP는 목록·연결 상태·실제 호출을 확인하세요. OAuth가 필요한 서비스는 Settings의 Authenticate에서 브라우저 로그인까지 완료합니다.
공식 MCP: [antigravity.google](https://antigravity.google/docs/mcp)
공식 Skill: [antigravity.google](https://antigravity.google/docs/skills?pubdate=20251130)

## Claude Code 설치 안내 · MCP와 Skill

2026.9.30 확인 · Claude Code에서 프로젝트 폴더를 열고 따라 하세요. Claude 일반 채팅과 로컬 Claude Code의 설치 위치는 다릅니다.

MCP 예제: 공개 문서 검색
프로젝트 터미널에서:
```shell
claude mcp add --transport http --scope project openaiDeveloperDocs https://developers.openai.com/mcp
claude mcp list
```

Claude Code 안에서 /mcp를 입력해 연결 상태를 확인하고 “OpenAI 공식 문서에서 Responses API 시작 방법을 검색해줘”라고 요청합니다. 프로젝트 .mcp.json에 기록되는 설정은 사용 승인 절차가 나올 수 있습니다.

복사할 요청문
```text
현재 Claude Code 공식 문서를 확인하고 openaiDeveloperDocs MCP를 프로젝트 범위의 HTTP 서버 https://developers.openai.com/mcp 로 추가해줘. 기존 .mcp.json 설정을 보존하고 중복을 피하고, /mcp 연결 확인과 실제 문서 검색 방법을 알려줘. 필요한 명령은 실행해주고, 내 로그인이나 승인 단계가 필요하면 그 단계에서 안내해줘.
```

Skill
프로젝트: `.claude/skills/handoff/SKILL.md`
개인 공통: `~/.claude/skills/handoff/SKILL.md`
teacher도 같은 방식입니다. ‘Skill 만들기’ 요청문 끝에 “Claude Code 프로젝트의 .claude/skills에 만들어줘”를 붙이세요. SKILL.md에는 name, description과 본문을 넣습니다.

완료 확인
/skills 또는 / 메뉴에서 등록 여부를 보고 /handoff, /teacher로 실행합니다. 플러그인은 /plugin의 공식 마켓플레이스에서 선택할 수 있지만, 설치 후 MCP 로그인까지 확인해야 합니다.
공식 MCP: [code.claude.com](https://code.claude.com/docs/en/mcp)
공식 Skill: [code.claude.com](https://code.claude.com/docs/de/skills)
(영문 Skill 문서 접근이 되지 않아 확인 가능한 공식 독일어판을 연결했습니다.)

## Skill 만들기 · handoff와 teacher 요청문

handoff와 teacher는 여기서 제안하는 사용자 정의 Skill 이름입니다. 이름만 입력하면 모든 앱에 같은 공식 패키지가 설치되는 것은 아닙니다. 아래 문장을 자신의 코딩 AI에 복사하면 목적에 맞는 Skill 파일을 만들 수 있습니다.

① handoff 요청문
```text
이 프로젝트에 handoff Skill을 만들어줘. 역할은 다른 AI나 다음 채팅에 작업을 넘기는 것이야. 프로젝트 규칙을 읽고, 목표·환경과 버전·변경한 파일·실행 방법·실제로 확인한 결과·남은 문제·다음 할 일을 HANDOFF.md에 정리해줘. 확인하지 않은 내용은 미확인으로 표시하고, 비밀번호·API 키·학생 개인정보는 기록하지 마. 기존 인계 문서는 읽고 필요한 부분만 갱신해줘. SKILL.md에 name과 description을 포함하고, 등록된 이름과 사용 예를 알려줘.
```

② teacher 요청문
```text
이 프로젝트에 teacher Skill을 만들어줘. 교사의 수업 목표와 가상 학생의 수행 조건을 읽고 자료를 검토해줘. 선택지 수·시각 단서·문장 길이·실수 후 복구·반복 연습·실제 생활 연결을 확인하고, 관찰할 행동과 수정 우선순위를 제안해줘. 학생을 무조건 기능을 줄여야 하는 대상으로 보지 말고 교육적 이유를 설명해줘. 진단이나 학생 선발을 판단하지 마. 실제 학생 개인정보가 필요하면 가상 사례로 바꿔줘. SKILL.md에 name과 description을 포함하고, 사용 예를 알려줘.
```

저장 위치와 실행 방법은 아래 앱별 설치 글을 따르세요. 설치 후 “handoff Skill로 다음 작업에 필요한 인계를 작성해줘” 또는 “teacher Skill로 카페 주문 화면을 검토해줘”라고 요청하고, 어떤 Skill을 읽었는지 확인합니다.

## Figma 교육용 · 학교 이메일과 기능 범위

2026.9.30 확인 · Figma는 화면의 버튼·카드·색·간격을 함께 설계하고 검토하는 도구입니다. 오늘 기본 실습에서는 선택 사항입니다.

학교 이메일만으로 교육용 혜택이 자동 적용된다고 보장할 수 없습니다. 계정을 만든 뒤 Education 신청과 자격 확인 절차를 진행하세요. 학교 전체의 학생 사용은 K–12 학교 신청 안내를 확인하세요.

교육용 신청: [www.figma.com](https://www.figma.com/education/apply)
K–12 학교 안내: [www.figma.com](https://www.figma.com/education/k-12)

공식 안내상 K–12·고등학교 교육용 계정은 AI 도구·Figma Make·Figma Sites가 포함되지 않습니다. 교육용 승인과 모든 AI 기능 이용 권한은 같은 뜻이 아닙니다. 계정별 제공 기능·MCP 호출 한도도 따로 확인하세요.

Figma MCP는 AI가 설계 내용을 읽고, 지원되는 환경에서는 Figma 캔버스에 설계를 만들거나 수정하도록 연결합니다. 접속 가능한 클라이언트와 기능 범위는 공식 MCP 안내를 확인하세요.
공식 교육용 안내: [help.figma.com](https://help.figma.com/hc/en-us/articles/360041061214-Figma-for-Education)
MCP 안내: [developers.figma.com](https://developers.figma.com/docs/figma-mcp-server/)

## 완료 확인 · 학생이 쓸 화면을 직접 눌러 보기

AI가 “완료”라고 말하면 교사가 실제 사용 흐름을 확인합니다. 화면이 예쁜지와 수업에 쓸 수 있는지는 함께 살펴야 합니다.

카페 주문 연습 예
① 음료를 고른 상태가 글·테두리·아이콘 등으로 분명히 보이나요?
② 온도와 크기를 고르는 순서가 학생의 수행 조건에 맞나요?
③ 잘못 눌렀을 때 이전 단계로 돌아가거나 다시 선택할 수 있나요?
④ 도움말을 보고 다시 시도할 수 있나요?
⑤ 태블릿에서 버튼과 글자가 보이고, 시작·끝·다시 연습이 되나요?

복사할 요청문
```text
teacher Skill 또는 아래 기준으로 이 화면을 검토해줘. 선택 표시, 시각 단서, 문장 길이, 실수 후 복구, 반복 연습, 실제 생활 연결을 확인해줘. 실제로 눌러 확인한 것과 아직 확인하지 못한 것을 구분하고, 교사가 직접 점검할 순서를 알려줘. 한 번에 가장 중요한 문제 하나부터 고쳐줘.
```

검증 기록에는 ‘잘 된다’ 대신 ‘음료 변경 후 다음 화면에도 선택이 유지됨’처럼 관찰한 행동을 씁니다. 게시·공유 전에 공개 화면에 개인 정보가 없는지 확인하고, 실제 수업에서는 교사가 학생의 반응을 관찰해 다시 조정합니다.

## Kiro · 요구사항부터 작업을 나누는 도구 (선택)

2026.9.30 확인 · Kiro는 요구사항·설계·할 일 순서로 작업을 정리하고 구현을 돕는 AI 코딩 도구입니다. 오늘 실습에서 반드시 설치할 필요는 없습니다.

```text
누가 무엇을 왜 하게 할 것인가”를 먼저 적고, 작은 단계로 나눠 만드는 방식과 연결해 보세요. 제공 모델과 크레딧 비용은 선택한 플랜·모델에 따라 달라집니다.
```
공식 안내: [kiro.dev](https://kiro.dev/)

## Aside · 웹 작업을 돕는 AI 브라우저 (선택)

2026.9.30 확인 · Aside는 브라우저에서 검색·자료 정리와 웹 작업을 돕는 AI 도구입니다. “권한이 막강하다”보다 어떤 사이트에서 어떤 작업을 맡길지 먼저 정하세요.

오늘 실습의 필수 도구는 아닙니다. 가상 자료로 요약이나 비교부터 시험하고, 실제 게시·공유 전에는 내용과 대상을 확인하세요. 제공 기능과 요금은 공식 안내에서 확인합니다.
공식 안내: [aside.com](https://aside.com/)
