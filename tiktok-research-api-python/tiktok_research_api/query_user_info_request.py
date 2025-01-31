# Copyright 2024 TikTok Pte. Ltd.
#
# This source code is licensed under the MIT license found in
# the LICENSE file in the root directory of this source tree.

__all__ = ["QueryUserInfoRequest"]


class QueryUserInfoRequest:
    def __init__(self, username, fields=None):
        self.username = username
        self.fields = (
            "display_name,bio_description,avatar_url,is_verified,follower_count,following_count,likes_count,video_count,bio_url"
            if not fields
            else fields
        )
