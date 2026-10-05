# Compliance and responsible use

This is a checklist for a real deployment, not legal advice.

- **Voter files**: many states restrict use to political, election or governmental purposes and prohibit commercial use or redistribution. Confirm the rules for each state and each licence before ingesting. Keep voter-file data local; only tract/ZIP aggregates should reach outputs.
- **Social media and news**: check each platform's terms of service and API licence. Store what you are permitted to store; prefer IDs and derived features where raw text redistribution is restricted.
- **Privacy**: no individual-level inference. Suppress small cells. No profiling of private individuals.
- **Place attributes**: take demographics from sourced aggregate data (ACS, voter-file aggregates) with provenance. Do not hand-assign group labels to neighborhoods.
- **LLM scoring**: keep prompt version and model id with every score; validate against a hand-labeled sample; report uncertainty.
- **Causal claims**: market/news analyses show association and timing, not proof of cause.
- **Disclosure**: check campaign finance and political advertising rules where outputs feed messaging.
