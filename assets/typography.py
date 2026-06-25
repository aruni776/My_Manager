def typography(theme):

    return f"""
    <style>

    h1 {{

        color: {theme['text']};

        font-weight: 700;
    }}

    h2 {{

        color: {theme['text']};
    }}

    h3 {{

        color: {theme['text']};
    }}

    </style>
    """