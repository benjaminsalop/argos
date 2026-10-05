"""Campaign weights.

load_weights(campaign) -> table of (aspect, term, weight)
apply_weights(scores, weights) -> sentiment * relevance * weight(aspect)

Also exposes update_weight(campaign, aspect_or_term, value), which bumps the campaign
config version and writes the YAML back. Used by the CLI and the Streamlit editor.
"""
