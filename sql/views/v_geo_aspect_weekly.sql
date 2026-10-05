-- Weekly weighted sentiment by tract and aspect, joined to place-level demographics.
CREATE OR REPLACE VIEW v_geo_aspect_weekly AS
SELECT
    date_trunc('week', v.published_at) AS week,
    v.geo_id,
    v.campaign_id,
    v.aspect,
    count(*)                 AS n_docs,
    avg(v.weighted_score)    AS mean_weighted_score
FROM v_weighted_scores v
GROUP BY ALL;
