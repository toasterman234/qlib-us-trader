// Sample data for DEMO mode (VITE_DEMO=1).
//
// Lets the whole UI render with realistic US-equity numbers and no backend,
// so the dashboard can be explored — and screenshotted — without syncing data
// or training a model. Everything here is fabricated for illustration only.

const WEEKS = 52
const START_CAPITAL = 1_000_000

// Deterministic pseudo-random so the demo looks identical on every load.
function seeded(seed: number) {
  let s = seed % 2147483647
  if (s <= 0) s += 2147483646
  return () => {
    s = (s * 16807) % 2147483647
    return (s - 1) / 2147483646
  }
}

function weekId(i: number) {
  return `2024-W${String(i + 1).padStart(2, '0')}`
}

function weekDate(i: number) {
  // Fridays, weekly, starting 2024-01-05.
  const base = Date.UTC(2024, 0, 5)
  const d = new Date(base + i * 7 * 86400_000)
  return d.toISOString().slice(0, 10)
}

const rnd = seeded(42)

// Build the weekly walk-forward series once.
const weekly = (() => {
  let cumStrategy = 0
  let cumMarket = 0
  let equity = START_CAPITAL
  let benchmark = START_CAPITAL
  let peak = START_CAPITAL

  const points = []
  // A couple of stress windows so the equity curve has real drawdowns.
  const stress = new Set([8, 9, 21, 22, 23, 41])
  for (let i = 0; i < WEEKS; i++) {
    const liveIc = 0.045 + (rnd() - 0.45) * 0.11
    const validIc = liveIc + 0.012 + rnd() * 0.02
    const shock = stress.has(i) ? -3.4 : 0
    const weekReturn = 0.55 + (liveIc * 4) + (rnd() - 0.5) * 3.0 + shock // realistic weekly swings
    const marketReturn = 0.34 + (rnd() - 0.5) * 3.2 + (stress.has(i) ? -2.2 : 0)

    cumStrategy = (1 + cumStrategy / 100) * (1 + weekReturn / 100) * 100 - 100
    cumMarket = (1 + cumMarket / 100) * (1 + marketReturn / 100) * 100 - 100

    equity = equity * (1 + weekReturn / 100)
    benchmark = benchmark * (1 + marketReturn / 100)
    peak = Math.max(peak, equity)
    const drawdown = ((equity - peak) / peak) * 100

    const isFallback = i === 17 || i === 38
    const icDecay = ((validIc - liveIc) / validIc) * 100

    points.push({
      i,
      predict_week: weekId(i),
      model_week: weekId(Math.max(0, i - 1)),
      model_name: `usl_${weekId(Math.max(0, i - 1))}`,
      valid_ic: Number(validIc.toFixed(4)),
      live_ic: Number(liveIc.toFixed(4)),
      ic_decay: Number(icDecay.toFixed(1)),
      week_return: Number(weekReturn.toFixed(2)),
      market_return: Number(marketReturn.toFixed(2)),
      cumulative_return: Number(cumStrategy.toFixed(2)),
      cumulative_market: Number(cumMarket.toFixed(2)),
      is_fallback: isFallback,
      incremental_days: i % 4 === 0 ? 5 : null,
      equity: Math.round(equity),
      benchmark: Math.round(benchmark),
      drawdown: Number(drawdown.toFixed(2)),
    })
  }
  return points
})()

const last = weekly[weekly.length - 1]
const meanIc = Number((weekly.reduce((s, p) => s + p.live_ic, 0) / WEEKS).toFixed(4))
const stdIc = Math.sqrt(weekly.reduce((s, p) => s + (p.live_ic - meanIc) ** 2, 0) / WEEKS)
const icir = Number((meanIc / stdIc).toFixed(4))
const icPositiveRate = Number(((weekly.filter((p) => p.live_ic > 0).length / WEEKS) * 100).toFixed(1))
const maxDrawdown = Number(Math.abs(Math.min(...weekly.map((p) => p.drawdown))).toFixed(1))
const winRate = Number(((weekly.filter((p) => p.week_return > 0).length / WEEKS) * 100).toFixed(1))

const FACTORS = [
  { name: 'mom_21d', display: '21-Day Momentum', category: 'technical', formula: 'Ref($close,-21)/$close-1', rate: 0.91, sel: 41, ev: 45 },
  { name: 'rsi_14', display: 'RSI (14)', category: 'technical', formula: 'RSI($close,14)', rate: 0.84, sel: 38, ev: 45 },
  { name: 'vol_ratio_20', display: 'Volume Ratio 20d', category: 'volume', formula: '$volume/Mean($volume,20)', rate: 0.80, sel: 36, ev: 45 },
  { name: 'turnover_z', display: 'Turnover Z-Score', category: 'volume', formula: 'Zscore($turnover,60)', rate: 0.78, sel: 35, ev: 45 },
  { name: 'earnings_yield', display: 'Earnings Yield', category: 'fundamental', formula: '$eps_ttm/$close', rate: 0.76, sel: 34, ev: 45 },
  { name: 'beta_60d', display: '60-Day Beta', category: 'technical', formula: 'Beta($return,$spy_return,60)', rate: 0.71, sel: 32, ev: 45 },
  { name: 'gross_margin', display: 'Gross Margin', category: 'fundamental', formula: '$gross_profit/$revenue', rate: 0.69, sel: 31, ev: 45 },
  { name: 'price_to_book', display: 'Price / Book', category: 'fundamental', formula: '$close/$book_value', rate: 0.67, sel: 30, ev: 45 },
  { name: 'mom_63d', display: '63-Day Momentum', category: 'technical', formula: 'Ref($close,-63)/$close-1', rate: 0.64, sel: 29, ev: 45 },
  { name: 'volatility_20', display: '20-Day Volatility', category: 'technical', formula: 'Std($return,20)', rate: 0.62, sel: 28, ev: 45 },
  { name: 'roe', display: 'Return on Equity', category: 'fundamental', formula: '$net_income/$equity', rate: 0.58, sel: 26, ev: 45 },
  { name: 'amihud_illiq', display: 'Amihud Illiquidity', category: 'volume', formula: 'Mean(Abs($return)/$dollar_vol,20)', rate: 0.56, sel: 25, ev: 45 },
  { name: 'macd_signal', display: 'MACD Signal', category: 'technical', formula: 'EMA($close,12)-EMA($close,26)', rate: 0.53, sel: 24, ev: 45 },
  { name: 'rev_growth_yoy', display: 'Revenue Growth YoY', category: 'fundamental', formula: '$revenue/Ref($revenue,252)-1', rate: 0.49, sel: 22, ev: 45 },
  { name: 'bollinger_pct', display: 'Bollinger %B', category: 'technical', formula: '($close-LowBB)/(UpBB-LowBB)', rate: 0.44, sel: 20, ev: 45 },
  { name: 'short_interest', display: 'Short Interest %', category: 'fundamental', formula: '$shares_short/$float', rate: 0.40, sel: 18, ev: 45 },
  { name: 'mom_252d', display: '252-Day Momentum', category: 'technical', formula: 'Ref($close,-252)/$close-1', rate: 0.36, sel: 16, ev: 45 },
  { name: 'cash_flow_yield', display: 'Cash Flow Yield', category: 'fundamental', formula: '$fcf/$market_cap', rate: 0.31, sel: 14, ev: 45 },
  { name: 'obv_slope', display: 'OBV Slope', category: 'volume', formula: 'Slope(OBV,20)', rate: 0.27, sel: 12, ev: 45 },
  { name: 'debt_to_equity', display: 'Debt / Equity', category: 'fundamental', formula: '$total_debt/$equity', rate: 0.22, sel: 10, ev: 45 },
  { name: 'price_gap', display: 'Overnight Gap', category: 'technical', formula: '$open/Ref($close,-1)-1', rate: 0.18, sel: 8, ev: 45 },
  { name: 'accruals', display: 'Accruals Ratio', category: 'fundamental', formula: '($net_income-$cfo)/$assets', rate: 0.13, sel: 6, ev: 45 },
  { name: 'high_low_range', display: 'High-Low Range', category: 'technical', formula: '($high-$low)/$close', rate: 0.09, sel: 4, ev: 45 },
  { name: 'vol_of_vol', display: 'Vol-of-Vol', category: 'technical', formula: 'Std(Std($return,5),20)', rate: 0.04, sel: 2, ev: 45 },
]

const factorItems = FACTORS.map((f, idx) => ({
  id: `f${idx + 1}`,
  name: f.name,
  display_name: f.display,
  category: f.category,
  description: null,
  formula: f.formula,
  selection_rate: f.rate,
  times_selected: f.sel,
  times_evaluated: f.ev,
  enabled: f.rate >= 0.2,
  created_at: '2024-01-02T09:30:00Z',
}))

const equityCurve = weekly.map((p) => ({
  date: weekDate(p.i),
  equity: p.equity,
  benchmark: p.benchmark,
  drawdown: p.drawdown,
}))

const weeklyPoints = weekly.map((p) => ({
  predict_week: p.predict_week,
  live_ic: p.live_ic,
  week_return: p.week_return,
  market_return: p.market_return,
  cumulative_return: p.cumulative_return,
  cumulative_market: p.cumulative_market,
}))

const weeklyDetails = weekly.map((p) => ({
  predict_week: p.predict_week,
  model_week: p.model_week,
  model_name: p.model_name,
  valid_ic: p.valid_ic,
  live_ic: p.live_ic,
  ic_decay: p.ic_decay,
  week_return: p.week_return,
  market_return: p.market_return,
  is_fallback: p.is_fallback,
  incremental_days: p.incremental_days,
}))

const config = {
  initial_capital: START_CAPITAL,
  max_positions: 10,
  trade_price: 'open',
  enable_incremental: false,
  strategy: 'topk',
}

const returnMetrics = {
  cumulative_return: last.cumulative_return,
  market_return: last.cumulative_market,
  excess_return: Number((last.cumulative_return - last.cumulative_market).toFixed(2)),
  sharpe_ratio: 1.62,
  max_drawdown: maxDrawdown,
  win_rate: winRate,
  total_trades: 524,
}

const icAnalysis = {
  avg_valid_ic: Number((weekly.reduce((s, p) => s + p.valid_ic, 0) / WEEKS).toFixed(4)),
  avg_live_ic: meanIc,
  ic_decay: 26.2,
  ic_correlation: 0.58,
}

const summary = {
  backtest_id: 3,
  start_week_id: weekId(0),
  end_week_id: weekId(WEEKS - 1),
  config,
  total_weeks: WEEKS,
  mean_ic: meanIc,
  icir,
  ic_positive_rate: icPositiveRate,
  annualized_return: Number((last.cumulative_return).toFixed(2)),
  annualized_excess: returnMetrics.excess_return,
  cumulative_return: last.cumulative_return,
  market_return: last.cumulative_market,
  excess_return: returnMetrics.excess_return,
  sharpe_ratio: 1.62,
  max_drawdown: maxDrawdown,
  win_rate: winRate,
  total_trades: 524,
  weekly_points: weeklyPoints,
  equity_curve: equityCurve,
  created_at: '2024-12-30T18:02:00Z',
  completed_at: '2024-12-30T18:09:00Z',
}

const backtestList = {
  items: [
    { id: 3, start_week_id: weekId(0), end_week_id: weekId(WEEKS - 1), status: 'completed', config, created_at: '2024-12-30T18:02:00Z', completed_at: '2024-12-30T18:09:00Z' },
    { id: 2, start_week_id: weekId(0), end_week_id: weekId(25), status: 'completed', config, created_at: '2024-09-14T11:20:00Z', completed_at: '2024-09-14T11:24:00Z' },
    { id: 1, start_week_id: weekId(0), end_week_id: weekId(12), status: 'completed', config, created_at: '2024-06-01T10:05:00Z', completed_at: '2024-06-01T10:08:00Z' },
  ],
  total: 3,
}

const backtestDetail = {
  ...backtestList.items[0],
  ic_analysis: icAnalysis,
  return_metrics: returnMetrics,
  weekly_details: weeklyDetails,
  equity_curve: equityCurve,
}

const availableWeeks = {
  current_week_id: weekId(WEEKS - 1),
  weeks: Array.from({ length: 14 }, (_, k) => {
    const i = WEEKS - 14 + k
    return {
      week_id: weekId(i),
      status: (k === 13 ? 'not_allowed' : k % 7 === 5 ? 'missing' : 'available') as 'available' | 'missing' | 'not_allowed',
      model_name: `usl_${weekId(i)}`,
      valid_ic: Number((0.05 + rnd() * 0.02).toFixed(4)),
    }
  }),
}

const dashboardSummary = {
  factors: { total: factorItems.length, enabled: factorItems.filter((f) => f.enabled).length, low_selection_count: 3 },
  model: {
    last_trained_at: '2024-12-30T06:00:00Z',
    days_since_training: 4,
    needs_retrain: false,
    factor_count: 14,
    ic: meanIc,
    icir,
  },
  prediction: {
    date: '2024-12-31',
    buy_signals: 10,
    sell_signals: 8,
    top_pick: { symbol: 'NVDA', score: 0.89 },
  },
  data_status: { is_complete: true, last_updated: '2024-12-31T21:05:00Z', missing_count: 0 },
  performance: { today_return: 0.0042, mtd_return: 0.021, ytd_return: 0.184, total_return: last.cumulative_return / 100 },
}

export const MOCK = {
  dashboardSummary,
  factorList: { items: factorItems, total: factorItems.length },
  backtestList,
  backtestDetail,
  availableWeeks,
  summary,
  jobs: { items: [], total: 0 },
}
