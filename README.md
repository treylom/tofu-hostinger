# tofu-hostinger — VPS 설치 코파일럿

Hostinger VPS 에 서버를 만들고, Claude Code 를 깔고, Discord 봇을 24시간 돌게 올리는 과정을 **한 단계씩 안내·판정**해 주는 스킬입니다. 자동 설치가 아니라, 사람이 명령을 실행하면 스킬이 결과를 읽고 다음 단계를 알려주는 방식입니다.

- 4개 루트: `:vps`(서버 만들기) · `:cc`(Claude Code 설치) · `:bot`(수업용 미니 봇) · `:std-bot`(표준 봇 상시 운영)
- 전 단계 = 라이브 VPS 실측 기반. 「조용히 안 되는」 함정 목록 동봉
- 시작: 설치 후 Claude Code 에서 `/tofu-hostinger:help`

## 설치

```bash
# 방법 1 — tofukyung-plugins 마켓플레이스 경유
claude plugin marketplace add treylom/tofukyung-plugins
claude plugin install tofu-hostinger@tofukyung-plugins

# 방법 2 — 이 레포 직접
claude plugin marketplace add treylom/tofu-hostinger
claude plugin install tofu-hostinger@tofu-hostinger
```

## 주의

- 토큰·비밀번호 값은 화면에 출력하지 않는 방식으로 확인합니다(스킬 내 계약).
- root 상시 운영의 위험 고지·비-root 정석 경로가 문서에 포함돼 있습니다.

## License

MIT
