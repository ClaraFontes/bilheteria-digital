import qrcode

links_produtos = {
    "Google": "https://google.com.br",
    "Youtube": "https://youtube.com.br"
}

for produto in links_produtos:
    meu_qrcode = qrcode.make(links_produtos[produto])
    meu_qrcode.save(f"qrcode_{produto}.png")