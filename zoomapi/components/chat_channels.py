"""Zoom.us REST API Python Client -- Chat Messages component"""
import json

from zoomapi import util
from zoomapi.components import base


class ChatChannelsComponentV2(base.BaseComponent):
    """Component dealing with all chat channels related matters"""

    def list(self, **kwargs):
        return self.get_request("/chat/users/me/channels")

    def create(self, **kwargs):
        util.require_keys(kwargs, ["name", "type", "members"])
        return self.post_request("/chat/users/me/channels", data=kwargs)

    def get(self, **kwargs):
        util.require_keys(kwargs, "channelId")
        return self.get_request(
            "/chat/channels/{channelId}".format(channelId=kwargs.get("channelId")))

    def update(self, **kwargs):
        util.require_keys(kwargs, ["channelId", "name"])
        return self.patch_request(
            "/chat/channels/{channelId}".format(channelId=kwargs.get("channelId")), data=kwargs)

    def delete(self, **kwargs):
        util.require_keys(kwargs, "channelId")
        return self.delete_request(
            "/chat/channels/{channelId}".format(channelId=kwargs.get("channelId")))

    def list_members(self, **kwargs):
        util.require_keys(kwargs, "channelId")
        return self.get_request(
            "/chat/channels/{channelId}/members".format(channelId=kwargs.get("channelId")))

    def invite(self, **kwargs):
        util.require_keys(kwargs, ["channelId", "members"])
        return self.post_request(
            "/chat/channels/{channelId}/members".format(channelId=kwargs.get("channelId")), data=kwargs)

    def join(self, **kwargs):
        util.require_keys(kwargs, "channelId")
        return self.post_request(
            "/chat/channels/{channelId}/members/me".format(channelId=kwargs.get("channelId")))

    def leave(self, **kwargs):
        util.require_keys(kwargs, "channelId")
        return self.delete_request(
            "/chat/channels/{channelId}/members/me".format(channelId=kwargs.get("channelId")))

    def remove(self, **kwargs):
        util.require_keys(kwargs, ["channelId", "memberId"])
        return self.delete_request(
            "/chat/channels/{channelId}/members/{memberId}".format(channelId=kwargs.get("channelId"),
                                                                   memberId=kwargs.get("memberId")))