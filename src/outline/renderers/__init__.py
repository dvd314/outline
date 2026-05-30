from outline.renderers.tree import (
    TreeRenderer,
)

from outline.renderers.source import (
    SourceRenderer,
)

from outline.renderers.json import (
    JsonRenderer,
)


RENDERERS = {
    "tree": {
        "help": "Render graph as tree",
        "renderer": TreeRenderer,
    },

    "json": {
        "help": "Render graph as JSON",
        "renderer": JsonRenderer,
    },

    "source": {
        "help": "Show graph as source code",
        "renderer": SourceRenderer
    }
}
