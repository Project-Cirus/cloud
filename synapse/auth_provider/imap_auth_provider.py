# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import logging
import imaplib

from collections import namedtuple
from twisted.internet import defer

logger = logging.getLogger(__name__)



class IMAPAuthProvider:
    def __init__(self, config, account_handler):
        self.account_handler = account_handler
        self.create_users = config.create_users
        self.server = config.server
        self.port = config.port

    @defer.inlineCallbacks
    def check_password(self, user_id, password):
        """ Attempt to authenticate a user against IMAP
            and register an account if none exists.
            Returns:
                True if authentication against IMAP was successful
        """
        # if not password:
        #     defer.returnValue(False)

        # user_id is of the form @foo:bar.com
        logger.info("inside check_password")
        logger.info("got user_id: %s", user_id)

        localpart = user_id.split(":", 1)[0][1:]
        domain = user_id[1:].split(':')[1] # e.g. synapse.domain.com
        mailDomain = ".".join(domain.split(".")[1:]) # domain.com
        email = '@'.join([localpart, mailDomain])

        logger.info("Trying to login as %s on %s:%d via IMAP", email, self.server, self.port)

        try:
            M = imaplib.IMAP4(self.server, self.port)
            r = M.login(email, password)
            if r[0] == 'OK':
                logger.info("imap login successful!")
                M.logout()
        except:
            logger.info("exception on imap login")
            defer.returnValue(False)

        if r[0] != 'OK':
            logger.info("no exception but return value was: %s", r[0])
            defer.returnValue(False)

        # From here on, the user is authenticated   

        # Bail if we don't want to create users in Matrix
        if not self.create_users:
            defer.returnValue(False)

        # Create the user in Matrix if it doesn't exist yet
        if not (yield self.account_handler.check_user_exists(user_id)):
            yield self.account_handler.register_user(localpart=localpart, emails=[email])

        defer.returnValue(True)

    @staticmethod
    def parse_config(config):
        imap_config = namedtuple('_Config', 'create_users')
        imap_config.create_users = config.get('create_users', True)
        imap_config.server = config.get('server', '')
        imap_config.port = config.get('port', 143)
        return imap_config
