# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class RulesEngineRule(Model):
    """Contains a list of match conditions, and an action on how to modify the
    request/response. If multiple rules match, the actions from one rule that
    conflict with a previous rule overwrite for a singular action, or append in
    the case of headers manipulation.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. A name to refer to this specific rule.
    :type name: str
    :param priority: Required. A priority assigned to this rule.
    :type priority: int
    :param action: Required. Actions to perform on the request and response if
     all of the match conditions are met.
    :type action: ~azure.mgmt.frontdoor.models.RulesEngineAction
    :param match_conditions: A list of match conditions that must meet in
     order for the actions of this rule to run. Having no match conditions
     means the actions will always run.
    :type match_conditions:
     list[~azure.mgmt.frontdoor.models.RulesEngineMatchCondition]
    :param match_processing_behavior: If this rule is a match should the rules
     engine continue running the remaining rules or stop. If not present,
     defaults to Continue. Possible values include: 'Continue', 'Stop'
    :type match_processing_behavior: str or
     ~azure.mgmt.frontdoor.models.MatchProcessingBehavior
    """

    _validation = {
        'name': {'required': True},
        'priority': {'required': True},
        'action': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'priority': {'key': 'priority', 'type': 'int'},
        'action': {'key': 'action', 'type': 'RulesEngineAction'},
        'match_conditions': {'key': 'matchConditions', 'type': '[RulesEngineMatchCondition]'},
        'match_processing_behavior': {'key': 'matchProcessingBehavior', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(RulesEngineRule, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.priority = kwargs.get('priority', None)
        self.action = kwargs.get('action', None)
        self.match_conditions = kwargs.get('match_conditions', None)
        self.match_processing_behavior = kwargs.get('match_processing_behavior', None)
