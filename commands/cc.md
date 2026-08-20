---
description: Claude Code 설치·인증 (:cc)
---
먼저 **반드시 Skill 도구로 `tofu-hostinger:tofu-hostinger` 스킬을 호출**한다. 그 스킬이 로드하는 `SKILL.md` + `manifest/cc.yaml`(필요 시 `help.md`)의 내용대로만 안내하며 **임의 지식으로 지어내지 않는다** — 코파일럿 계약 준수(자동 설치 ❌·사람이 명령 실행·매 단계 관측→기대값 판정·시크릿 무출력). 이 명령은 그 스킬의 `:cc` 라우트 진입점이다. Claude Code CLI 설치·인증(+선택 ThisCode 번들)을 단계별로 안내·판정한다.
