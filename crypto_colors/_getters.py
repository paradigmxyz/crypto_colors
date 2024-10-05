from __future__ import annotations


def get_topics() -> list[str]:
    return [
        'networks',
        'stablecoins',
    ]


def get_colors(topic: str) -> dict[str, str]:
    if topic == 'networks':
        from ._color_sets import networks

        return networks.get_network_colors()
    elif topic == 'stablecoins':
        from ._color_sets import stablecoins

        return stablecoins.get_stablecoin_colors()
    else:
        raise Exception('invalid topic: ' + str(topic))
