from assets.layout import layout
from assets.sidebar import sidebar
from assets.typography import typography


def apply_theme(theme):

    return f"""
    <style>

    .stApp {{

        background:

        radial-gradient(
            circle at top right,
            {theme['accent1']}20,
            transparent 35%
        ),

        radial-gradient(
            circle at bottom left,
            {theme['accent2']}15,
            transparent 35%
        ),

        linear-gradient(
            135deg,
            {theme['bg']},
            #050816
        );

        color:{theme['text']};
    }}

    div[data-testid="stMetric"] {{

        background:
        rgba(20,28,45,0.60);

        border:
        1px solid rgba(255,255,255,0.08);

        border-radius:
        16px;

        padding:
        16px;
    }}

    div[data-testid="stVerticalBlockBorderWrapper"] {{

        border-radius:
        16px;

        background:
        rgba(20,28,45,0.40);
    }}

    hr {{

        border-color:
        rgba(255,255,255,0.08);
    }}

    </style>

    {layout()}

    {sidebar(theme)}

    {typography(theme)}
    """