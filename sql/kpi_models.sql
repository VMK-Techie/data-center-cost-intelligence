-- ANSI-style SQL illustrative models; adapt date functions to your warehouse dialect.
-- Expected tables (synthetic): projects(project_id, approved_budget_usd, commissioned_it_mw)
-- po_lines(po_line_id, project_id, vendor_id, equipment_type, unit_price_usd,
--          baseline_unit_price_usd, quantity, po_total_usd, invoiced_usd)
-- project_actuals(project_id, actual_cost_usd) and project_etc(project_id, uncommitted_etc_usd)
-- Assumption: invoices booked in project_actuals; PO 'open' is net of invoices.
WITH po_exposure AS (
  SELECT project_id,
         SUM(po_total_usd - invoiced_usd) AS open_commitments_usd,
         SUM((unit_price_usd - baseline_unit_price_usd) * quantity) AS ppv_usd
  FROM po_lines
  GROUP BY project_id
), actuals AS (
  SELECT project_id, SUM(actual_cost_usd) AS actual_usd
  FROM project_actuals GROUP BY project_id
), etc AS (
  SELECT project_id, SUM(uncommitted_etc_usd) AS uncommitted_etc_usd
  FROM project_etc GROUP BY project_id
)
SELECT p.project_id, p.approved_budget_usd, p.commissioned_it_mw,
       COALESCE(a.actual_usd,0) AS actual_usd,
       COALESCE(po.open_commitments_usd,0) AS open_commitments_usd,
       COALESCE(e.uncommitted_etc_usd,0) AS uncommitted_etc_usd,
       COALESCE(a.actual_usd,0) + COALESCE(po.open_commitments_usd,0)
         + COALESCE(e.uncommitted_etc_usd,0) AS eac_usd,
       p.approved_budget_usd - (COALESCE(a.actual_usd,0)
         + COALESCE(po.open_commitments_usd,0) + COALESCE(e.uncommitted_etc_usd,0)) AS vac_usd,
       (COALESCE(a.actual_usd,0) + COALESCE(po.open_commitments_usd,0)
         + COALESCE(e.uncommitted_etc_usd,0)) / NULLIF(p.commissioned_it_mw,0) AS eac_usd_per_it_mw,
       COALESCE(po.ppv_usd,0) AS purchase_price_variance_usd
FROM projects p
LEFT JOIN actuals a ON a.project_id=p.project_id
LEFT JOIN po_exposure po ON po.project_id=p.project_id
LEFT JOIN etc e ON e.project_id=p.project_id;

-- Production model warning: invoices can be accrued before cash payment;
-- do not equate booked actual cost with cash flow. Validate PO-line payment matching.
