---
description: 표준 봇 올리기 (:std-bot — bun → 플러그인 → 토큰 → 온보딩 → 기동 → 접근 허용 → 왕복)
---
먼저 **반드시 Skill 도구로 `tofu-hostinger:tofu-hostinger` 스킬을 호출**한다. 그 스킬이 로드하는 `SKILL.md` + `manifest/std-bot.yaml`(필요 시 `help.md`)의 내용대로만 안내하며 **임의 지식으로 지어내지 않는다** — 코파일럿 계약 준수(자동 설치 ❌·사람이 명령 실행·매 단계 관측→기대값 판정·시크릿 무출력). 이 명령은 그 스킬의 `:std-bot` 라우트 진입점이다. 표준 봇(Claude Code 본체 + 공식 discord 플러그인)을 bun → 플러그인 → 토큰(DISCORD_BOT_TOKEN) → 온보딩 → 기동 → 접근 허용 → 왕복 순으로. 「죽지 않고 조용히 안 되는」 무징후 함정을 각 단계에서 고지한다.
