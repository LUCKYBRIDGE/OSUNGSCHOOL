# 참고 출처 (v22, 2026-09-30 확인)

도구·요금·기능·나이 기준은 빠르게 바뀌므로 발표 직전에 공식 문서를 다시 확인한다.

- 괄호 속 쪽 번호는 v22 슬라이드 위치다(1부 42쪽, 2부 35쪽). 'Q'는 대본 끝 '예상 질문과 답변' 번호다.
- 번호 [n]은 발표 대본(`docs/03_speaker_script.md`)의 근거 번호와 같다.
- v21 쪽 번호와의 대응은 `docs/v22_work_plan.md`에 있다.
- OpenAI Codex 문서 주소(`developers.openai.com/codex/…`)는 2026-09-30 기준 `learn.chatgpt.com/docs/…`로 넘어간다(연결은 된다). 다음 버전에서 새 주소로 바꾼다.

## 하네스와 작업환경

1. OpenAI, *Harness engineering: leveraging Codex in an agent-first world* (2026. 2.) — https://openai.com/index/harness-engineering/
   - 사람이 코드를 직접 쓰지 않고 Codex 에이전트로 제품을 만든 경험. "Humans steer. Agents execute." 사람의 일이 환경 설계·의도 명시·피드백 루프 구축으로 바뀌었다는 내용. 실패 시 '더 열심히'가 아니라 빠진 능력을 찾아 채웠다는 교훈. (1부 19·20)
2. OpenAI Developers, *Rethinking skills and prompts for GPT-6 Astra* (2026. 9. 11.) — https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
   - 스킬 설명은 짧게, 필요할 때만 읽게(점진적 공개), AGENTS.md는 자주 다시 보고 필요 없는 지시를 지우기, 완료 기준을 먼저 정하기. (1부 25·28·32, Q10)
3. OpenAI Codex Docs, *Custom instructions with AGENTS.md* — https://developers.openai.com/codex/guides/agents-md
   - 전역 파일 + 저장소 루트부터 현재 폴더까지 합쳐 읽고, 가까운 파일이 뒤에 온다. (1부 26·36)
4. OpenAI Codex Docs, *Agent Skills* — https://developers.openai.com/codex/skills
   - `.agents/skills`(저장소), `$HOME/.agents/skills`(사용자), `$이름`·`/skills`로 호출. (1부 26·28)
5. Claude Code Docs, *How Claude remembers your project* — https://code.claude.com/docs/en/memory
   - CLAUDE.md 위치와 적재 순서, CLAUDE.md가 없으면 AGENTS.md를 읽음(v2.1.277 이상), 200줄 이하 권장. (1부 25·26, Q10)
6. Google Antigravity Docs, *Rules* · *Skills* — https://antigravity.google/docs/rules · https://antigravity.google/docs/skills
   - AGENTS.md 또는 GEMINI.md, `.agents/rules/`, 전역 `~/.gemini/`; 스킬은 `.agents/skills/`, `/이름`으로 호출. (1부 26·28)
7. Model Context Protocol, *Introduction* — https://modelcontextprotocol.io/docs/getting-started/intro
   - AI 앱과 외부 시스템을 잇는 오픈 표준, 'AI용 USB-C 포트' 비유. (1부 12)
8. OpenAI Help, *Apps in ChatGPT* · Claude Help, *Connectors* — https://help.openai.com/en/articles/11487775 · https://claude.com/docs/connectors/getting-started (1부 31)
22. 워크플로·커맨드에서 스킬로의 변화 — https://developers.openai.com/codex/custom-prompts · https://code.claude.com/docs/en/skills · https://antigravity.google/docs/skills · https://antigravity.google/docs/migration/workflows-to-skills/ · https://www.anthropic.com/engineering/building-effective-agents
   - Codex 커스텀 프롬프트는 사용 중단 예정(deprecated), 스킬 사용 권장. Claude Code의 `.claude/commands/`는 예전 형식이지만 동작한다. Antigravity 문서는 스킬을 `/이름`으로 부르도록 안내하고, 워크플로는 2026. 11. 1.까지만 동작하며 그 뒤에는 인식·실행되지 않는다고 적는다(`/migrate-workflows`로 옮김). Anthropic은 정해진 코드 경로로 움직이는 시스템을 workflow, 스스로 과정을 정하는 시스템을 agent로 구분한다. (1부 29, Q12)
24. Claude Code Docs, *Automate workflows with hooks* — https://code.claude.com/docs/en/hooks-guide
   - 훅은 Claude Code가 정해진 시점(예: 파일을 고친 뒤, 명령 실행 전)에 실행하는 사용자 정의 명령이다. 모델이 실행 여부를 고르지 않고 반드시 실행되는 결정적(deterministic) 제어를 준다. 판단이 필요한 경우를 위한 prompt·agent 방식 훅도 있다. 프로젝트 훅은 `.claude/settings.json`에 둔다. (1부 29, Q12)

## 공개 사례

9. Everything Claude Code(ECC) 저장소 — https://github.com/affaan-m/ECC (구 주소 `affaan-m/everything-claude-code`)
   - 저장소 생성 2026-01-18, 별표 26만 개 이상(2026-09-29 GitHub API 확인). 작성자 소개 페이지와 저장소 안내 문서에 Anthropic x Forum Ventures 해커톤 우승(zenith.chat) 기록. 해커톤: 2025. 9. 12. 뉴욕(행사 페이지 https://www.forumvc.com/forum-ventures-x-anthropic-ai-hackathon), 저장소 안내 문서에는 'Sep 2025'. 설정 수: 스킬 292·에이전트 68·명령 94·규칙 폴더 22개(언어별, 2026-09-30 GitHub API). (1부 21·33)
10. Claude 블로그, *Meet the winners of the Built with Opus 4.7 Claude Code hackathon* (2026. 6.) — https://claude.com/blog/meet-the-winners-of-built-with-opus-4-7-claude-code-hackathon
   - 1위 Medkit(의사 출신 개발자), 2위 Wrench Board(전자제품 수리 경력자), 3위 Maieutic(대학 컴퓨터과학 교육자·AI 박사과정), Keep Thinking 상 MaestrIA(코딩 경험 없는 20세, 목수 아버지 인터뷰로 만든 JSON 파일: 진단 규칙 17·목재 7·현장 용어 16·기준 가격 19·흔한 실수 9, 평가 74%→81%). (1부 22)
23. knollab-001 비교 실험 (강사 자료) — 실험 사이트 네 곳:
   - A https://luckybridge.github.io/knollab-001-a-ai-only/ · B https://luckybridge.github.io/knollab-001-b-design-md/ · C https://luckybridge.github.io/knollab-001-c-design-figma-mcp/ · D https://luckybridge.github.io/knollab-001-d-design-figma-mcp-actively/
   - 실험 설계 저장소 https://github.com/LUCKYBRIDGE/knollab-001 에는 A·B·C 설계만 있고 D와 사이트 주소는 없다(2026-09-29 이후 갱신 없음). 주소는 이 문서를 기준으로 안내한다.
   - 특수학교 학생용 카페 주문 연습 사이트(순수 HTML/CSS/JavaScript)를 같은 목표로 네 조건에서 제작. A·B·C는 같은 단계별 요청문(버전 1→2→3), 서로 다른 ChatGPT 프로젝트와 프로젝트 전용 메모리. B·C의 DESIGN.md는 동일(blob `c91e3a4`). C는 고정한 Figma 설계 + Figma MCP. D는 Figma 적극 활용: 버전 1은 B·C와 같은 DESIGN.md(커밋 `f05380c`), 버전 2에서 DESIGN.md를 다시 씀(커밋 `1dab112`, 현재 blob `e196548`). D는 버전 2 작업 중이고, A·B·C와 같은 요청문을 썼는지는 확인하지 못했다(2026-09-30 확인). (2부 20·34, Q4)

## 디자인 도구

11. Google Labs, *Introducing "vibe design" with Stitch* (2026. 3. 18.) — https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-ai-ui-design/ (2부 18)
12. Google Labs, *Stitch's DESIGN.md format is now open-source* (2026. 4. 21.) — https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-design-md/ (2부 14·18)
13. DESIGN.md 명세(alpha) — https://github.com/google-labs-code/design.md (2부 14, 저장소 `DESIGN.md`)
14. Anthropic, *Introducing Claude Design by Anthropic Labs* (2026. 4.) — https://www.anthropic.com/news/claude-design-anthropic-labs · Claude Help, *Get started with Claude Design* — https://support.claude.com/en/articles/14604416
   - 출시(2026. 4.): Pro·Max·Team·Enterprise 대상 연구 프리뷰, 대화·인라인 댓글·직접 수정, 디자인 시스템 적용, Canva·PDF·PPTX·HTML 내보내기, Claude Code 핸드오프.
   - 도움말(2026. 9. 확인): Pro·Max·Team·Enterprise에서 베타. 아티팩트 템플릿 가운데 하나로도 시작한다. (2부 18, Q1)
15. Figma Developer Docs, *Figma MCP server* · *Write to canvas* · *Code to canvas* — https://developers.figma.com/docs/figma-mcp-server/ (2부 18)

## 실습 도구 (설치 없이 브라우저에서)

18. OpenAI Help, *Projects in ChatGPT* — https://help.openai.com/en/articles/10169521
   - 프로젝트는 무료·유료 모든 요금제에서 쓸 수 있고, 프로젝트 설정에서 지침을 넣는다. (2부 26, Q1·Q2)
19. OpenAI Help, *Working with writing blocks and code blocks in ChatGPT* — https://help.openai.com/en/articles/20001246
   - 코드 블록에서 Preview를 누르면 HTML 페이지 등을 ChatGPT 안에서 미리 본다. 쓸 수 있는 기능은 요금제·기기·설정에 따라 다르다. (2부 26, Q2)
20. Gemini Apps Help, *Create docs, apps & more with Canvas* · *Use Gems in Gemini Apps* — https://support.google.com/gemini/answer/16047321 · https://support.google.com/gemini/answer/15146780
   - Canvas에서 만든 앱을 Preview로 본다. Gem은 지침과 Knowledge 파일을 가진다. 개인 계정 Gem은 2026년 11월부터 스킬로 자동 전환된다. Gem 사용은 만 13세(또는 나라별 기준) 이상이고, Google 계정 나이 기준표(https://support.google.com/accounts/answer/1350409)에서 한국은 만 14세 이상이다. (2부 26·27·34, 1부 29, Q6·Q12)
21. Claude Help, *What are artifacts and how do I use them?* · *What are projects?* — https://support.claude.com/en/articles/17153992 · https://support.claude.com/en/articles/9517075
   - 아티팩트(한 쪽짜리 웹사이트·작은 도구 등)는 무료 요금제에서도 대화 안에서 만든다. 프로젝트는 지침과 지식 파일을 가진다. (2부 26, Q1·Q2)

## 학교에서 쓸 때 (나이 기준·데이터)

25. OpenAI Help, *Is ChatGPT safe for all ages?* · OpenAI *Terms of Use* — https://help.openai.com/en/articles/8313401 · https://openai.com/policies/terms-of-use/
   - 이용약관: 만 13세 이상 또는 나라에서 정한 동의 가능 나이 이상이어야 하고, 만 18세 미만은 부모·법정대리인의 허락이 필요하다. 도움말: ChatGPT는 13세 미만을 위한 서비스가 아니다. (2부 27·34, Q6)
26. Claude Help, *Minimum age requirement access restriction* · *Age assurance on Claude* — https://support.claude.com/en/articles/13117299 · https://support.claude.com/en/articles/15171100
   - Claude 계정은 18세 이상만 만들고 쓸 수 있다. (2부 27·34, Q6)
27. Anthropic, *Updates to Consumer Terms and Privacy Policy* — https://www.anthropic.com/news/updates-to-our-consumer-terms
   - 사용자가 자기 데이터를 Claude 개선에 쓸지 선택할 수 있다. 서비스마다 대화 기록·학습 사용 설정이 다르므로 각 서비스 설정에서 확인한다. (2부 27, Q5)
28. 개인정보 보호법 제22조의2(아동의 개인정보 보호) — https://www.law.go.kr/법령/개인정보보호법 (영문 번역 확인: https://prighter.com/resources/laws/korean-pipa/main/articles/article-22-2)
   - 만 14세 미만 아동의 개인정보를 처리하려고 동의를 받아야 할 때에는 법정대리인의 동의를 받고 확인해야 한다. (Q6)

## 배포와 접근성

16. GitHub Docs, *About GitHub Pages* — https://docs.github.com/pages
   - GitHub Free는 공개 저장소에서 Pages 사용, Pages 사이트는 인터넷에 공개됨. (1부 13, 2부 24, Q1·Q7)
17. W3C, *WCAG 2.2* — https://www.w3.org/TR/WCAG22/ (누르는 대상 크기, 색에만 의존하지 않기) (2부 10)

## v20 대비 바로잡은 내용

- ECC 해커톤 시점: '2026년 2월경' → 2025년 해커톤, 2026년 1월 저장소 공개
- Claude Design: '베타' → 유료 플랜 연구 프리뷰(2026. 4. 출시)
- 기존 [9] `developers.openai.com/api/docs/guides/latest-model`은 모델 안내 문서이며 AGENTS.md 적재 방식 근거가 아니므로 Codex AGENTS.md 문서로 교체

## v22 독립 검토에서 바로잡은 내용 (2026-09-30)

- 이용 나이: 'Gem 13세 이상' → 한국은 만 14세 이상(Google 계정 기준). ChatGPT '13세 이상'에 '나라별 기준 우선'을 붙였다. 한국 개인정보 보호법의 만 14세 기준 [28]을 더했다.
- Claude Design: v21의 '연구 프리뷰'는 2026. 4. 출시 때 표현이다. 2026. 9. 도움말 기준 '유료 플랜 전용 베타'로 고쳤다.
- knollab-001 D: B·C와 같은 조건처럼 보이던 '+ Figma 규격화' 표기를 고치고, 버전 2에서 DESIGN.md를 다시 쓴 사실을 적었다. 사이트 주소의 기준 위치를 이 문서로 옮겼다(실험 설계 저장소에는 D와 주소가 없다).
- ECC 규칙 수: '규칙 23'은 `rules/`의 README.md까지 센 값이라 '규칙 폴더 22개'로 고쳤다. 해커톤 날짜의 1차 자료(행사 페이지)를 더했다.
- Antigravity 워크플로 종료일(2026. 11. 1.)과 이전 안내 문서를 [22]에 더했다.
