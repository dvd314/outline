from outline.renderers.tree import (
    TreeRenderer,
)

from outline.renderers.json import (
    JsonRenderer,
)


RENDERERS = {
    "tree": {
        "flag": None,
        "help": "Render graph as tree",
        "renderer": TreeRenderer,
    },

    "json": {
        "flag": "--json",
        "help": "Render graph as JSON",
        "renderer": JsonRenderer,
    },
}
