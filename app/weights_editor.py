"""Local Streamlit app for adjusting campaign weights.

Planned behavior:
- load a campaign YAML
- sliders per aspect and per term
- preview: re-score a cached sample using the new weights (no LLM calls) and show before/after
- save: write YAML back with version + 1
"""
