-- Weighted score per document and aspect. Weights are applied here, not stored,
-- so changing a campaign weight never requires re-running the LLM.
CREATE OR REPLACE VIEW v_weighted_scores AS
SELECT
    s.doc_id,
    s.campaign_id,
    s.aspect,
    s.sentiment,
    s.relevance,
    w.weight,
    s.sentiment * s.relevance * w.weight AS weighted_score,
    d.published_at,
    d.geo_id,
    d.source
FROM document_aspect_scores s
JOIN campaign_weights w
  ON w.campaign_id = s.campaign_id AND w.aspect = s.aspect
JOIN documents d USING (doc_id);
