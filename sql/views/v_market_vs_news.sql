-- Market price vs. weekly news sentiment on a shared time grid (input to analysis/lead_lag.py).
CREATE OR REPLACE VIEW v_market_vs_news AS
SELECT
    date_trunc('day', m.ts)  AS day,
    m.market_id,
    avg(m.price)             AS price,
    avg(v.weighted_score)    AS news_score
FROM market_series m
LEFT JOIN v_weighted_scores v
  ON date_trunc('day', v.published_at) = date_trunc('day', m.ts)
GROUP BY ALL;
