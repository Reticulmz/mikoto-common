from common.ripple.webhookHandler import Webhook

def postWebhook(url, args=None):
    embed = Webhook(url, **args, footer="osu!Vipsu")
    embed.post()
	
def postWebhookRanked(url, args=None):
    embed = Webhook(url, **args, footer="Ranked on osu!Vipsu")
    embed.post()

def postWebhookRequest(url, args=None):
    embed = Webhook(url, **args, footer="Request on osu!Vipsu")
    embed.post()
	
def postWebhookLoved(url, args=None):
    embed = Webhook(url, **args, footer="Love on osu!Vipsu")
    embed.post()

def postWebhookUnranked(url, args=None):
    embed = Webhook(url, **args, footer="Unanked on osu!Vipsu")
    embed.post()	