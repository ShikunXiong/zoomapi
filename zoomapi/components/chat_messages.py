"""Zoom.us REST API Python Client -- Chat Messages component"""

from zoomapi import util
from zoomapi.components import base
from zoomapi.util import Throttled


class ChatMessagesComponentV2(base.BaseComponent):
    """Component dealing with all chat messages related matters"""

    @Throttled
    def list(self, **kwargs):
        util.require_keys(kwargs, "user_id")
        return self.get_request(
                "/chat/users/{}/messages".format(kwargs.get("user_id")), params=kwargs
        )

    @Throttled
    def post(self, **kwargs):
        util.require_keys(kwargs, "message")
        return self.post_request("/chat/users/me/messages", data=kwargs)

    @Throttled
    def delete(self, **kwargs):
        util.require_keys(kwargs, "messageId")
        return self.delete_request("/chat/users/me/messages/{}".format(kwargs.get("messageId")), params=kwargs)

    @Throttled
    def update(self, messageID, **kwargs):
        util.require_keys(kwargs, "message")
        return self.put_request("/chat/users/me/messages/{}".format(messageID), data=kwargs)
