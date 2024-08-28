`wecom_bot_msg` is a simple wrapper for WeCom (Worker Wechat ) group bot API, to send text, image, audio, files etc in groups, check [official docs](https://developer.work.weixin.qq.com/document/path/91770) for more information.

`wecom_bot_msg` 是给企业微信群机器人 API 的封装，用作发送文本、图片、语音、文件等各类消息，更多信息可以查看[官方文档](https://developer.work.weixin.qq.com/document/path/91770)

# Installation

Install `wecom_bot_msg` using pip

```bash
pip install wecom_bot_msg
```

## Usage

Simple usage to send text or image

```python

from wecom_bot_msg import WecomBot

bot = WecomBot(api_key='YOUR_API_KEY')

# send text
success, err_msg = bot.send_text('hello')

# send image
success, err_msg = bot.send_image('/LOCAL/PATH/IMAGE')
```

More examples

```python
# sent text with mentioned list (or mentioned_mobile_list)
bot.send_text('hello', mentioned_list=['kim','kttiy'])
bot.send_text('hello', mentioned_mobile_list=['18688888888','15688888888'])
```

## TODO

- [x] send text
- [x] send image
- [ ] send markdown
- [ ] upload file
- [ ] send audio
- [ ] send news
- [ ] send template card
