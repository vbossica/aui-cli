# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from aui_cli.common.services import get_client, get_custom_headers


def show_configuration(instance_id):
    """
    Show search configuration.

    :param instance_id: ID of the instance
    """

    client = get_client()

    return client.getsearchconfiguration(instance_id=instance_id,
                                         custom_headers=get_custom_headers())
