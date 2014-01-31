# Copyright (c) 2014 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from neutron.common import constants
from neutron.extensions import portbindings
from neutron.plugins.ml2.drivers import mech_ryu
from neutron.tests.unit.ml2 import _test_mech_agent as base


class RyuMechanismBaseTestCase(base.AgentMechanismBaseTestCase):
    VIF_TYPE = portbindings.VIF_TYPE_OVS
    CAP_PORT_FILTER = True
    AGENT_TYPE = constants.AGENT_TYPE_RYU

    GOOD_MAPPINGS = {'fake_physical_network': 'fake_bridge'}
    GOOD_TUNNEL_TYPES = ['gre', 'vxlan']
    GOOD_CONFIGS = {'bridge_mappings': GOOD_MAPPINGS,
                    'tunnel_types': GOOD_TUNNEL_TYPES}

    BAD_MAPPINGS = {'wrong_physical_network': 'wrong_bridge'}
    BAD_TUNNEL_TYPES = ['bad_tunnel_type']
    BAD_CONFIGS = {'bridge_mappings': BAD_MAPPINGS,
                   'tunnel_types': BAD_TUNNEL_TYPES}

    AGENTS = [{'alive': True,
               'configurations': GOOD_CONFIGS}]
    AGENTS_DEAD = [{'alive': False,
                    'configurations': GOOD_CONFIGS}]
    AGENTS_BAD = [{'alive': False,
                   'configurations': GOOD_CONFIGS},
                  {'alive': True,
                   'configurations': BAD_CONFIGS}]

    def setUp(self):
        super(RyuMechanismBaseTestCase, self).setUp()
        self.driver = mech_ryu.RyuMechanismDriver()
        self.driver.initialize()


class RyuMechanismGenericTestCase(RyuMechanismBaseTestCase,
                                  base.AgentMechanismGenericTestCase):
    pass


class RyuMechanismLocalTestCase(RyuMechanismBaseTestCase,
                                base.AgentMechanismLocalTestCase):
    pass


class RyuMechanismFlatTestCase(RyuMechanismBaseTestCase,
                               base.AgentMechanismFlatTestCase):
    pass


class RyuMechanismVlanTestCase(RyuMechanismBaseTestCase,
                               base.AgentMechanismVlanTestCase):
    pass


class RyuMechanismGreTestCase(RyuMechanismBaseTestCase,
                              base.AgentMechanismGreTestCase):
    pass
