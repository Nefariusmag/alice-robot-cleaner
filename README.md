# alice-robot-cleaner
Try to connect Yandex Alice and Robot cleaner

## Docs

Python miio lib to work with Xiaomi Mi Robot Vacuum - 
https://github.com/rytilahti/python-miio

###For Yandex-Alica
Manual - https://tech.yandex.ru/dialogs/alice/doc/deploy-azure-docpage/

Example of code - https://github.com/yandex/alice-skills/tree/master/python/buy-elephant/azure

---

## How To Use
- Install requirements to python
- Add in env `TOKEN` and `IP` of your Xiaomi Mi Robot Vacuum

### Using ngrok 
- Start `python3 main.py`
- Use ngrok https://ngrok.com/ for create proxy sever `ngrok http 5000`
- Use this URL to yandex-dialog

### Using Azure
Doc - https://docs.microsoft.com/ru-ru/azure/app-service/containers/quickstart-python

- Delete app.run() in main.py
- Install az and login in Azure
- Deploy `az webapp up -n your-name -g your-group`
- Add env in app in Azure
- Add URL ti yandex-dialog