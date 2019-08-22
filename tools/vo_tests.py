#!/usr/bin/env python
# Copyright European Organization for Nuclear Research (CERN)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# You may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Authors:
# - Vincent Garonne, <vincent.garonne@cern.ch>, 2013
# - Mario Lassnig, <mario.lassnig@cern.ch>, 2014
# - Martin Barisits, <martin.barisits@cern.ch>, 2017
# - Thomas Beermann, <thomas.beermann@cern.ch>, 2017
# - Cedric Serfon, <cedric.serfon@cern.ch>, 2019
#
# PY3K COMPATIBLE

from rucio.api.vo import add_vo, list_vos
from rucio.client import Client
from rucio.common.config import config_get_bool
from rucio.common.exception import Duplicate
from rucio.core.account import add_account_attribute
from rucio.common.types import InternalAccount


if __name__ == '__main__':
    if config_get_bool('common', 'multi_vo', raise_exception=False, default=False):

        voname = 'tst'
        vo = {'vo': voname}
        issuer='super_root'
        add_vo(new_vo=vo['vo'], issuer=issuer, password='vopassword', description='A VO to test multi-vo features', email='N/A', vo='def')
        print('Added VO tst OK')

        for eachvo in list_vos(issuer=issuer, vo = 'def'):
            if eachvo['vo'] != 'def':
                print ("vo = {vo}, description={description}".format(vo=eachvo['vo'] , description=eachvo['description']) )     
    else:
        vo = {}





