You score a document for a public-affairs analysis.

Aspects to look for (with aliases):
{{ aspects_block }}

For each aspect that the document actually discusses, return JSON:
{"aspect": "<name>", "sentiment": <-1..1>, "relevance": <0..1>, "evidence": "<short quote from the text>"}

Rules:
- Only include aspects the text addresses. Do not infer from the author's identity or location.
- Sentiment is the stance or tone of the text toward the aspect, accounting for negation and context.
- Do not apply any importance weighting. Return raw sentiment and relevance only.
- Return a JSON list, empty if nothing applies.

Document:
{{ text }}
