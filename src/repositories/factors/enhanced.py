"""
Enhanced factors

Supplementary factors designed to address model weaknesses:
- Volatility regime factors (7) - low IC in bull markets
- Long-term momentum / mean reversion (8) - low Top-10 stability
- Liquidity factors (6) - signal stability
- Valuation-dynamics factors (8) - Q1 seasonal weakness
- Market-microstructure factors (8) - poor quantile monotonicity
"""

# =============================================================================
# 1. 波動率 Regime 因子（7 個）
# 幫助模型識別市場 regime，改善 bull market 表現
# =============================================================================

VOLATILITY_REGIME_FACTORS = [
    {
        "name": "vol_regime_20d",
        "display_name": "Volatility Regime 20d",
        "category": "technical",
        "expression": "Std($close / Ref($close, 1) - 1, 20) / (Std($close / Ref($close, 1) - 1, 60) + 1e-8)",
        "description": "20-day volatility / 60-day volatility",
    },
    {
        "name": "vol_regime_5d",
        "display_name": "Volatility Regime 5d",
        "category": "technical",
        "expression": "Std($close / Ref($close, 1) - 1, 5) / (Std($close / Ref($close, 1) - 1, 20) + 1e-8)",
        "description": "5-day volatility / 20-day volatility",
    },
    {
        "name": "realized_vol_20d",
        "display_name": "Realized Volatility 20d",
        "category": "technical",
        "expression": "Std($close / Ref($close, 1) - 1, 20)",
        "description": "20-day return std dev",
    },
    {
        "name": "realized_vol_60d",
        "display_name": "Realized Volatility 60d",
        "category": "technical",
        "expression": "Std($close / Ref($close, 1) - 1, 60)",
        "description": "60-day return std dev",
    },
    {
        "name": "high_low_vol_20d",
        "display_name": "Range Volatility 20d",
        "category": "technical",
        "expression": "Mean(($high - $low) / $close, 20)",
        "description": "20-day average intraday range",
    },
    {
        "name": "vol_trend",
        "display_name": "Volatility Trend",
        "category": "technical",
        "expression": "Slope(Std($close / Ref($close, 1) - 1, 10), 20)",
        "description": "20-day trend slope of 10-day volatility",
    },
    {
        "name": "vol_skew_20d",
        "display_name": "Volatility Skew 20d",
        "category": "technical",
        "expression": "(Mean(Greater($close / Ref($close, 1) - 1, 0), 20) - Mean(Greater(Ref($close, 1) / $close - 1, 0), 20)) / (Std($close / Ref($close, 1) - 1, 20) + 1e-8)",
        "description": "asymmetry between upside and downside volatility",
    },
]

# =============================================================================
# 2. 長期動量/均值回歸因子（8 個）
# 提供更穩定的長期信號，改善 Top-10 穩定性
# =============================================================================

LONG_MOMENTUM_FACTORS = [
    {
        "name": "roc_120",
        "display_name": "ROC 120d",
        "category": "technical",
        "expression": "Ref($close, 120) / $close - 1",
        "description": "120-day rate of price change",
    },
    {
        "name": "roc_250",
        "display_name": "ROC 250d",
        "category": "technical",
        "expression": "Ref($close, 250) / $close - 1",
        "description": "250-day rate of price change (about one year)",
    },
    {
        "name": "ma_120",
        "display_name": "MA Ratio 120d",
        "category": "technical",
        "expression": "Mean($close, 120) / $close",
        "description": "120-day MA / close",
    },
    {
        "name": "ma_250",
        "display_name": "MA Ratio 250d",
        "category": "technical",
        "expression": "Mean($close, 250) / $close",
        "description": "250-day MA / close (annual MA)",
    },
    {
        "name": "ma_cross_20_60",
        "display_name": "MA Cross 20/60",
        "category": "technical",
        "expression": "Mean($close, 20) / Mean($close, 60) - 1",
        "description": "20-day MA deviation from 60-day MA",
    },
    {
        "name": "ma_cross_60_120",
        "display_name": "MA Cross 60/120",
        "category": "technical",
        "expression": "Mean($close, 60) / Mean($close, 120) - 1",
        "description": "60-day MA deviation from 120-day MA",
    },
    {
        "name": "momentum_quality",
        "display_name": "Momentum Quality",
        "category": "technical",
        "expression": "($close / Ref($close, 60) - 1) / (Std($close / Ref($close, 1) - 1, 60) + 1e-8)",
        "description": "60-day return / 60-day volatility (momentum Sharpe ratio)",
    },
    {
        "name": "mean_reversion_20d",
        "display_name": "Mean Reversion 20d",
        "category": "technical",
        "expression": "($close - Mean($close, 20)) / (Std($close, 20) + 1e-8)",
        "description": "close deviation from 20-day MA in std devs",
    },
]

# =============================================================================
# 3. 流動性因子（6 個）
# 提高信號穩定性，低流動性股票信號噪音大
# =============================================================================

LIQUIDITY_FACTORS = [
    {
        "name": "amihud_20d",
        "display_name": "Amihud Illiquidity 20d",
        "category": "technical",
        "expression": "Mean(Abs($close / Ref($close, 1) - 1) / (Log($volume + 1) + 1e-8), 20)",
        "description": "20-day Amihud illiquidity",
    },
    {
        "name": "amihud_60d",
        "display_name": "Amihud Illiquidity 60d",
        "category": "technical",
        "expression": "Mean(Abs($close / Ref($close, 1) - 1) / (Log($volume + 1) + 1e-8), 60)",
        "description": "60-day Amihud illiquidity",
    },
    {
        "name": "turnover_20d",
        "display_name": "Turnover 20d",
        "category": "technical",
        "expression": "Mean($volume / ($total_shares + 1e-8), 20)",
        "description": "20-day average turnover",
    },
    {
        "name": "turnover_momentum",
        "display_name": "Turnover Momentum",
        "category": "technical",
        "expression": "Mean($volume / ($total_shares + 1e-8), 5) / (Mean($volume / ($total_shares + 1e-8), 20) + 1e-8)",
        "description": "Turnover Short/Long Ratio (liquidity change)",
    },
    {
        "name": "liquidity_improvement",
        "display_name": "Liquidity Improvement",
        "category": "technical",
        "expression": "Mean($volume, 10) / (Mean($volume, 60) + 1e-8) - 1",
        "description": "10-day volume deviation from 60-day average volume",
    },
    {
        "name": "vol_concentration",
        "display_name": "Volume Concentration",
        "category": "technical",
        "expression": "Max($volume, 5) / (Sum($volume, 5) + 1e-8)",
        "description": "5-day max daily volume share",
    },
]

# =============================================================================
# 4. 估值動態因子（8 個）
# 捕捉估值時序變化，改善 Q1 季節性弱勢
# =============================================================================

VALUATION_DYNAMIC_FACTORS = [
    {
        "name": "pe_percentile_120d",
        "display_name": "PE Quantile 120d",
        "category": "interaction",
        "expression": "Rank($pe_ratio, 120)",
        "description": "PE time-series quantile within 120 days",
    },
    {
        "name": "pe_percentile_250d",
        "display_name": "PE Quantile 250d",
        "category": "interaction",
        "expression": "Rank($pe_ratio, 250)",
        "description": "PE time-series quantile within 250 days",
    },
    {
        "name": "pb_percentile_120d",
        "display_name": "PB Quantile 120d",
        "category": "interaction",
        "expression": "Rank($pb_ratio, 120)",
        "description": "PB time-series quantile within 120 days",
    },
    {
        "name": "pb_percentile_250d",
        "display_name": "PB Quantile 250d",
        "category": "interaction",
        "expression": "Rank($pb_ratio, 250)",
        "description": "PB time-series quantile within 250 days",
    },
    {
        "name": "pe_mean_reversion",
        "display_name": "PE Mean Reversion",
        "category": "interaction",
        "expression": "($pe_ratio - Mean($pe_ratio, 120)) / (Std($pe_ratio, 120) + 1e-8)",
        "description": "PE deviation from 120-day mean in std devs",
    },
    {
        "name": "dy_momentum_20d",
        "display_name": "Dividend Yield Momentum 20d",
        "category": "interaction",
        "expression": "$dividend_yield / (Mean($dividend_yield, 20) + 1e-8) - 1",
        "description": "dividend yield deviation from 20-day mean",
    },
    {
        "name": "dy_rank_120d",
        "display_name": "Dividend Yield Rank 120d",
        "category": "interaction",
        "expression": "Rank($dividend_yield, 120)",
        "description": "dividend yield time-series quantile within 120 days",
    },
    {
        "name": "pe_momentum_20d",
        "display_name": "PE Momentum 20d",
        "category": "interaction",
        "expression": "$pe_ratio / (Mean($pe_ratio, 20) + 1e-8) - 1",
        "description": "PE Deviation from 20-Day Mean",
    },
]

# =============================================================================
# 5. 市場微結構因子（8 個）
# 提供更細粒度的信息，改善 quantile 單調性
# =============================================================================

MICROSTRUCTURE_FACTORS = [
    {
        "name": "intraday_range_stability",
        "display_name": "intraday range stability",
        "category": "technical",
        "expression": "Std(($high - $low) / $close, 20) / (Mean(($high - $low) / $close, 20) + 1e-8)",
        "description": "coefficient of variation of range",
    },
    {
        "name": "close_position",
        "display_name": "Close Position",
        "category": "technical",
        "expression": "Mean(($close - $low) / ($high - $low + 1e-8), 10)",
        "description": "10-day average close position within intraday range",
    },
    {
        "name": "open_close_gap",
        "display_name": "Gap",
        "category": "technical",
        "expression": "Mean(Abs($open / Ref($close, 1) - 1), 20)",
        "description": "20-day average gap size",
    },
    {
        "name": "price_vol_divergence",
        "display_name": "Volume-Price Divergence",
        "category": "interaction",
        "expression": "($close / Ref($close, 10) - 1) * -1 * ($volume / (Mean($volume, 10) + 1e-8) - 1)",
        "description": "inverse product of price and volume change",
    },
    {
        "name": "volume_surprise",
        "display_name": "Volume Surprise",
        "category": "technical",
        "expression": "($volume - Mean($volume, 20)) / (Std($volume, 20) + 1e-8)",
        "description": "volume Z-score vs 20-day mean",
    },
    {
        "name": "up_volume_ratio_10d",
        "display_name": "Up-Volume Ratio 10d",
        "category": "interaction",
        "expression": "Sum($volume * Greater($close - Ref($close, 1), 0), 10) / (Sum($volume, 10) + 1e-8)",
        "description": "10-day up-volume share of total volume",
    },
    {
        "name": "high_low_ratio_trend",
        "display_name": "Range Trend",
        "category": "technical",
        "expression": "Mean(($high - $low) / $close, 5) / (Mean(($high - $low) / $close, 20) + 1e-8)",
        "description": "short-term range / long-term range trend",
    },
    {
        "name": "consecutive_up_days",
        "display_name": "Up-Day Streak 20d",
        "category": "technical",
        "expression": "Sum(Greater($close - Ref($close, 1), 0), 20) / 20",
        "description": "20-day up-day ratio",
    },
]

# =============================================================================
# 匯出
# =============================================================================

ENHANCED_FACTORS = (
    VOLATILITY_REGIME_FACTORS
    + LONG_MOMENTUM_FACTORS
    + LIQUIDITY_FACTORS
    + VALUATION_DYNAMIC_FACTORS
    + MICROSTRUCTURE_FACTORS
)
