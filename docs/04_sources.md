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
