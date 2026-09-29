# 참고 출처 (v21, 2026-09-29 확인)

도구·요금·기능은 빠르게 바뀌므로 발표 직전에 공식 문서를 다시 확인한다. 괄호 속 쪽 번호는 v21 슬라이드 위치다.

## 하네스와 작업환경

1. OpenAI, *Harness engineering: leveraging Codex in an agent-first world* (2026. 2.) — https://openai.com/index/harness-engineering/
   - 사람이 코드를 직접 쓰지 않고 Codex 에이전트로 제품을 만든 경험. "Humans steer. Agents execute." 사람의 일이 환경 설계·의도 명시·피드백 루프 구축으로 바뀌었다는 내용. 실패 시 '더 열심히'가 아니라 빠진 능력을 찾아 채웠다는 교훈. (1부 20·21)
2. OpenAI Developers, *Rethinking skills and prompts for GPT-6 Astra* (2026. 9. 11.) — https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
   - 스킬 설명은 짧게, 필요할 때만 읽게(점진적 공개), AGENTS.md는 자주 다시 보고 필요 없는 지시를 지우기, 완료 기준을 먼저 정하기. (1부 27·33)
3. OpenAI Codex Docs, *Custom instructions with AGENTS.md* — https://developers.openai.com/codex/guides/agents-md
   - 전역 파일 + 저장소 루트부터 현재 폴더까지 합쳐 읽고, 가까운 파일이 뒤에 온다. (1부 28·37)
4. OpenAI Codex Docs, *Agent Skills* — https://developers.openai.com/codex/skills
   - `.agents/skills`(저장소), `$HOME/.agents/skills`(사용자), `$이름`·`/skills`로 호출. (1부 28·30)
5. Claude Code Docs, *How Claude remembers your project* — https://code.claude.com/docs/en/memory
   - CLAUDE.md 위치와 적재 순서, CLAUDE.md가 없으면 AGENTS.md를 읽음(v2.1.277 이상), 200줄 이하 권장. (1부 27·28)
6. Google Antigravity Docs, *Rules* · *Skills* — https://antigravity.google/docs/rules · https://antigravity.google/docs/skills
   - AGENTS.md 또는 GEMINI.md, `.agents/rules/`, 전역 `~/.gemini/`; 스킬은 `.agents/skills/`, `/이름`으로 호출. (1부 28)
7. Model Context Protocol, *Introduction* — https://modelcontextprotocol.io/docs/getting-started/intro
   - AI 앱과 외부 시스템을 잇는 오픈 표준, 'AI용 USB-C 포트' 비유. (1부 13)
8. OpenAI Help, *Apps in ChatGPT* · Claude Help, *Connectors* — https://help.openai.com/en/articles/11487775 · https://claude.com/docs/connectors/getting-started (1부 32)

## 공개 사례

9. Everything Claude Code(ECC) 저장소 — https://github.com/affaan-m/ECC (구 주소 `affaan-m/everything-claude-code`)
   - 저장소 생성 2026-01-18, 별표 26만 개 이상(2026-09-29 GitHub API 확인). 작성자 소개 페이지와 저장소 안내 문서에 Anthropic x Forum Ventures 해커톤 우승(zenith.chat) 기록. 해커톤 연도 2025는 작성자 글과 2차 자료로 확인. (1부 22)
10. Claude 블로그, *Meet the winners of the Built with Opus 4.7 Claude Code hackathon* (2026. 6.) — https://claude.com/blog/meet-the-winners-of-built-with-opus-4-7-claude-code-hackathon
   - 1위 Medkit(의사 출신 개발자), 2위 Wrench Board(전자제품 수리 경력자), 3위 Maieutic(대학 컴퓨터과학 교육자·AI 박사과정), Keep Thinking 상 MaestrIA(코딩 경험 없는 20세, 목수 아버지 인터뷰로 만든 JSON 파일: 진단 규칙 17·목재 7·현장 용어 16·기준 가격 19·흔한 실수 9, 평가 74%→81%). (1부 23·24)

## 디자인 도구

11. Google Labs, *Introducing "vibe design" with Stitch* (2026. 3. 18.) — https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-ai-ui-design/ (2부 22)
12. Google Labs, *Stitch's DESIGN.md format is now open-source* (2026. 4. 21.) — https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-design-md/ (2부 15)
13. DESIGN.md 명세(alpha) — https://github.com/google-labs-code/design.md (2부 15·16, 저장소 `DESIGN.md`)
14. Anthropic, *Introducing Claude Design by Anthropic Labs* (2026. 4.) — https://www.anthropic.com/news/claude-design-anthropic-labs
   - Pro·Max·Team·Enterprise 대상 연구 프리뷰, 대화·인라인 댓글·직접 수정, 디자인 시스템 적용, Canva·PDF·PPTX·HTML 내보내기, Claude Code 핸드오프. (2부 22)
15. Figma Developer Docs, *Figma MCP server* · *Write to canvas* · *Code to canvas* — https://developers.figma.com/docs/figma-mcp-server/ (2부 23)

## 배포와 접근성

16. GitHub Docs, *About GitHub Pages* — https://docs.github.com/pages
   - GitHub Free는 공개 저장소에서 Pages 사용, Pages 사이트는 인터넷에 공개됨. (1부 14, 2부 30)
17. W3C, *WCAG 2.2* — https://www.w3.org/TR/WCAG22/ (누르는 대상 크기, 색에만 의존하지 않기) (2부 11·13)

## v20 대비 바로잡은 내용

- ECC 해커톤 시점: '2026년 2월경' → 2025년 해커톤, 2026년 1월 저장소 공개
- Claude Design: '베타' → 유료 플랜 연구 프리뷰(2026. 4. 출시)
- 기존 [9] `developers.openai.com/api/docs/guides/latest-model`은 모델 안내 문서이며 AGENTS.md 적재 방식 근거가 아니므로 Codex AGENTS.md 문서로 교체

## v22 추가 출처 (2026-09-30 확인)

18. OpenAI Help, *Projects in ChatGPT* — https://help.openai.com/en/articles/10169521
   - 프로젝트는 무료·유료 모든 요금제에서 쓸 수 있고, 프로젝트 설정에서 지침을 넣는다. (2부 실습 도구)
19. OpenAI Help, *Working with writing blocks and code blocks in ChatGPT* — https://help.openai.com/en/articles/20001246
   - 코드 블록에서 Preview를 누르면 HTML 페이지 등을 ChatGPT 안에서 미리 본다. 쓸 수 있는 기능은 요금제·기기·설정에 따라 다르다. (2부 실습 도구)
20. Gemini Apps Help, *Create docs, apps & more with Canvas* · *Use Gems in Gemini Apps* — https://support.google.com/gemini/answer/16047321 · https://support.google.com/gemini/answer/15146780
   - Canvas에서 만든 앱을 Preview로 본다. Gem은 지침과 Knowledge 파일을 가진다. 개인 계정 Gem은 2026년 11월부터 스킬로 자동 전환된다. Gem 사용은 13세 이상. (2부 실습 도구, 1부 스킬 정리)
21. Claude Help, *What are artifacts and how do I use them?* · *What are projects?* — https://support.claude.com/en/articles/17153992 · https://support.claude.com/en/articles/9517075
   - 아티팩트(한 쪽짜리 웹사이트·작은 도구 등)는 무료 요금제에서도 대화 안에서 만든다. 프로젝트는 지침과 지식 파일을 가진다. (2부 실습 도구)
22. 워크플로·커맨드에서 스킬로의 변화 — https://developers.openai.com/codex/custom-prompts · https://code.claude.com/docs/en/skills · https://antigravity.google/docs/skills · https://www.anthropic.com/engineering/building-effective-agents
   - Codex 커스텀 프롬프트는 사용 중단 예정(deprecated), 스킬 사용 권장. Claude Code의 `.claude/commands/`는 예전 형식이지만 동작한다. Antigravity 문서는 스킬을 `/이름`으로 부르도록 안내한다. Anthropic은 정해진 코드 경로로 움직이는 시스템을 workflow, 스스로 과정을 정하는 시스템을 agent로 구분한다. (1부 스킬 정리)
23. knollab-001 비교 실험 (강사 자료) — https://github.com/LUCKYBRIDGE/knollab-001
   - 실험 사이트: https://luckybridge.github.io/knollab-001-a-ai-only/ · `…/knollab-001-b-design-md/` · `…/knollab-001-c-design-figma-mcp/` · `…/knollab-001-d-design-figma-mcp-actively/`
   - 특수학교 학생용 카페 주문 연습 사이트(순수 HTML/CSS/JavaScript)를 같은 목표로 네 조건에서 제작. A·B·C는 같은 단계별 요청문(버전 1→2→3), 서로 다른 ChatGPT 프로젝트와 프로젝트 전용 메모리. B·C의 DESIGN.md는 동일(blob `c91e3a4`). C는 고정한 Figma 설계 + Figma MCP. D는 Figma 적극 활용, 버전 2 작업 중(2026-09-30 확인). (2부 사례)
24. Claude Code Docs, *Automate workflows with hooks* — https://code.claude.com/docs/en/hooks-guide
   - 훅은 Claude Code가 정해진 시점(예: 파일을 고친 뒤, 명령 실행 전)에 실행하는 사용자 정의 명령이다. 모델이 실행 여부를 고르지 않고 반드시 실행되는 결정적(deterministic) 제어를 준다. 판단이 필요한 경우를 위한 prompt·agent 방식 훅도 있다. 프로젝트 훅은 `.claude/settings.json`에 둔다. (1부 규칙·스킬·훅 비교)
