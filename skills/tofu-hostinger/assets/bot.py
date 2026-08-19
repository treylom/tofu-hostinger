# 최소 디스코드 봇 예제 — VPS 설치 확인용
# 기능 2개뿐: ①@봇 핑 → pong  ②@봇 검색 <질의> → VPS 검색서버 상위 3건 회신
import asyncio
import json
import os
import urllib.parse
import urllib.request

import discord


def load_env(path=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")):
    # .env 파일(DISCORD_TOKEN=... 형식)을 읽어 환경변수로 올린다 — 별도 라이브러리 불필요
    try:
        for line in open(path, encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())
    except FileNotFoundError:
        pass


load_env()
TOKEN = os.environ.get("DISCORD_TOKEN")
if not TOKEN:
    raise SystemExit("DISCORD_TOKEN 이 없습니다 — /opt/bot/.env 파일을 확인하세요")
SEARCH_URL = os.environ.get("SEARCH_URL", "http://127.0.0.1:8410/api/search")

# 멘션(@봇) 기반 명령만 쓰므로 특권 인텐트(포털 토글) 불필요 — 설치 단계 최소화
client = discord.Client(intents=discord.Intents.default())


def search(query):
    url = f"{SEARCH_URL}?{urllib.parse.urlencode({'q': query})}"
    with urllib.request.urlopen(url, timeout=10) as r:
        data = json.load(r)
    return data.get("results", [])[:3]


@client.event
async def on_ready():
    print(f"봇 로그인 성공: {client.user} — 터미널을 닫아도 tmux 방 안에서 계속 돕니다")


@client.event
async def on_message(msg):
    # 자기 자신 메시지만 무시 — 다른 봇의 멘션에는 응답한다(봇 간 협업이 이 봇의 존재 이유)
    if msg.author.id == client.user.id or client.user not in msg.mentions:
        return
    # 멘션 토큰을 걷어내고 명령만 남긴다
    text = msg.content
    for m in (f"<@{client.user.id}>", f"<@!{client.user.id}>"):
        text = text.replace(m, "")
    text = text.strip()
    if text in ("핑", "ping", "!ping"):
        await msg.reply("pong — VPS 서버에서 응답했습니다 🛰️")
    elif text.startswith(("검색 ", "!검색 ")):
        q = text.split(" ", 1)[1].strip()
        try:
            hits = await asyncio.to_thread(search, q)
        except Exception as e:
            await msg.reply(f"검색 실패: {e}")
            return
        if not hits:
            await msg.reply(f"「{q}」 — VPS 검색 결과 없음")
            return
        lines = [
            f"{i}. {h.get('entity') or h.get('source_note') or '(무제)'}"
            for i, h in enumerate(hits, 1)
        ]
        await msg.reply(f"「{q}」 VPS 검색 상위 {len(lines)}건:\n" + "\n".join(lines))
    else:
        # 명령을 못 알아들었을 때도 침묵하지 않는다 — 살아 있음 + 사용법 안내
        await msg.reply("명령은 두 가지입니다: `@봇이름 핑` · `@봇이름 검색 <찾을 말>`")


client.run(TOKEN)
