# tofu-hostinger — Codex CLI 가이드

Codex CLI 는 Claude Code 전용 SKILL.md 프론트매터(자동 트리거)를 읽지 않는다. 대신 Codex 세션은 이 스킬의 매니페스트를 **직접 Read** 해서 같은 절차를 안내한다 — 별도 코드 경로를 새로 만들지 않는다.

## 사용법

0. 사용자가 ":help" 를 요청하면 — **또는 「전체를 한 번에 보고 싶다」·「읽으면서 따라하겠다」는 취지면** — `help.md` 를 Read 해서 그대로 제시한다. 이 루트만은 **판정 왕복이 없다**(아래 계약 2·3은 적용 대상 밖). 서버 구입부터 봇 24시간 상시화까지가 한 편으로 이어져 있고, 명령마다 「이렇게 나오면 성공」이 붙어 있다.
1. 사용자가 ":vps" / ":cc" / ":bot" / ":std-bot" 을 요청하면, 해당 route 의 `manifest/<route>.yaml` 을 이 스킬 폴더에서 직접 Read 한다 — `manifest/vps.yaml` / `manifest/cc.yaml` / `manifest/bot.yaml` / `manifest/std-bot.yaml`.
   - 🔴 `:bot`(수업용 미니 봇 · python + `bot.py`)과 `:std-bot`(표준 봇 · Claude Code 본체 + bun)은 **다른 루트다.** 토큰 변수명(`DISCORD_TOKEN` vs `DISCORD_BOT_TOKEN`)·토큰 경로·접근 제어 유무가 전부 다르므로 한 흐름에 섞지 않는다. 대조표 = SKILL.md 「`:bot` 과 `:std-bot` 은 다른 루트다」 절.
2. 매니페스트의 각 entry(`id · title · action · observation · expected · mismatch · verified · source`)를 순서대로 사람에게 제시한다: `action` 을 안내 → 사람이 실행 → `observation` 명령을 사람이 실행하고 결과를 붙여넣음 → `expected` 와 대조해 판정.
3. `bot.yaml` b3(코드 3파일) 단계에서는 `assets/bot.py` 를 Read 해 heredoc 명령 본문(`<assets/bot.py 전문>` 자리)에 채워 제시한다 — 출처 맥락 흔적이 제거된 범용판이며, 코드 로직은 가이드 STEP 6 원문과 동일하다.

## 판정 계약 — SKILL.md 「코파일럿 계약」 6항 그대로 적용(재정의 없음)

계약 전문 = SKILL.md §계약(특히 「축 한정 measured 주의」·「화면 공유·녹화 중 토큰 구간 일시정지」 2조항 포함) — 이 문서는 재정의하지 않는다.

## 진행 표시

Claude Code 경로와 동일하게 단계마다 `[:route 단계 id — 제목] n/전체` 한 줄을 머리에 붙인다. 세션이 끊겨 재개하면, 마지막 PASS 단계의 확인 명령부터 다시 통과시키고 이어간다.

## Codex 하네스 한정 차이점

- SKILL.md 프론트매터 자동 트리거가 없다 — 사용자가 본 문서를 직접 지목하거나 ":help"/":vps"/":cc"/":bot"/":std-bot" 요청이 왔을 때 Codex 오퍼레이터가 수동으로 `help.md` 또는 `manifest/` 를 연다.
- 그 외 라우팅 표(`:help` 단독 통독 / 단계 경로 = `:vps → :cc(선택) → :bot` 또는 `:std-bot`)·판정 계약·매니페스트 스키마·`assets/bot.py` 는 Claude Code 경로와 100% 동일한 파일을 그대로 공유한다(포크·복제본 없음).
