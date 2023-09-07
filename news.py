# kakaotemplates.py

# ListCard
def listcard(news_title):
    data = []

    _boannews = crawling.newest_news(news_title)
    count = 1
    for bn in _boannews:
        if count == 6 : break
        _temp = dict()
        _temp["title"] = _boannews[bn]["title"]
        _temp["description"] = _boannews[bn]["date"] + " | " + _boannews[bn]["author"]
        _temp["link"] = {"web" : _boannews[bn]["link"]}
        data.append(_temp)
        count += 1

    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "listCard": {
                        "header": {
                            "title": news_title
                        },
                        "items": data
                    }
                }
            ]
        }
    }
    
def quickReplies():
    return {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "보안 관련 뉴스 사이트입니다."
                    }
                }
            ],
            "quickReplies": [
                {
                    "messageText": "보안뉴스",
                    "action": "message",
                    "label": "보안뉴스"
                },
                {
                    "messageText": "데일리시큐",
                    "action": "message",
                    "label": "데일리시큐"
                },
                {
                    "messageText": "wired",
                    "action": "message",
                    "label": "wired"
                },
                {
                    "messageText": "모아서 보기",
                    "action": "message",
                    "label": "모아서 보기"
                }
            ]
        }
    }