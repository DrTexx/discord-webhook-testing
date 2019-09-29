#!/home/denver/github/discord-webhook-testing/venv/bin/python3 -E

from discord_webhook import DiscordWebhook

webhook = DiscordWebhook(
    url='https://discordapp.com/api/webhooks/627311410187337729/unOVLsNiU2humAjzGNkXRv4FleUiML8da1omzxG-6hqmQvlCxeA8RbDtxQzXFWtu2SRw',
    content='<@&627106537030287380> Bin icon test <:bingo:627299655742652443> | <:binin:627299781038833684> | <:binout:627299839734185995>'
)

webhook.execute()
