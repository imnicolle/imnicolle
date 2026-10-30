"""Lê o contador do tally.yuki.sh e regenera assets/views.svg (mesmo estilo dos botões)."""
import json, pathlib, sys, urllib.request

URL = "https://tally.yuki.sh/hits/imnicolle/profile.json?mode=read"   # mode=read: só lê, não incrementa
root = pathlib.Path(__file__).resolve().parent.parent
try:
    req = urllib.request.Request(URL, headers={"User-Agent": "imnicolle-profile-views"})
    count = int(json.load(urllib.request.urlopen(req, timeout=20))["visit"])
except Exception as e:                                                   # falhou? mantém o SVG atual
    print("contador indisponível:", e); sys.exit(0)
tpl = (root / "scripts" / "views.template.svg").read_text(encoding="utf-8")
(root / "assets" / "views.svg").write_text(tpl.replace("{{COUNT}}", f"{count:,}"), encoding="utf-8")
print("views:", count)
