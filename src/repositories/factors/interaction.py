"""
Interaction factors

Cross-category combination factors: price-volume, flow-price, valuation-momentum, etc.
~55 factors total.
"""

# =============================================================================
# 價量交互因子
# =============================================================================

# 量價相關性
VOL_PRICE_CORR_FACTORS = [
    {
        "name": "vol_price_corr_5",
        "display_name": "Volume-Price Correlation 5d",
        "category": "interaction",
        "expression": "Corr($close, Log($volume + 1), 5)",
        "description": "5-Day Volume-Price Correlation",
    },
    {
        "name": "vol_price_corr_10",
        "display_name": "Volume-Price Correlation 10d",
        "category": "interaction",
        "expression": "Corr($close, Log($volume + 1), 10)",
        "description": "10-Day Volume-Price Correlation",
    },
    {
        "name": "vol_price_corr_20",
        "display_name": "Volume-Price Correlation 20d",
        "category": "interaction",
        "expression": "Corr($close, Log($volume + 1), 20)",
        "description": "20-Day Volume-Price Correlation",
    },
    {
        "name": "vol_price_corr_60",
        "display_name": "Volume-Price Correlation 60d",
        "category": "interaction",
        "expression": "Corr($close, Log($volume + 1), 60)",
        "description": "60-Day Volume-Price Correlation",
    },
]

# 收益與量變相關
RET_VOL_CORR_FACTORS = [
    {
        "name": "ret_vol_corr_5",
        "display_name": "Return vs Volume-Change Correlation 5d",
        "category": "interaction",
        "expression": "Corr($close / Ref($close, 1) - 1, $volume / (Ref($volume, 1) + 1e-8) - 1, 5)",
        "description": "5-Day Return vs Volume-Change Correlation",
    },
    {
        "name": "ret_vol_corr_20",
        "display_name": "Return vs Volume-Change Correlation 20d",
        "category": "interaction",
        "expression": "Corr($close / Ref($close, 1) - 1, $volume / (Ref($volume, 1) + 1e-8) - 1, 20)",
        "description": "20-Day Return vs Volume-Change Correlation",
    },
]

# 量能分佈
VOL_DISTRIBUTION_FACTORS = [
    {
        "name": "vol_up_down_ratio",
        "display_name": "Up-Volume Ratio",
        "category": "interaction",
        "expression": "Sum($volume * Greater($close - Ref($close, 1), 0), 20) / (Sum($volume * Greater(Ref($close, 1) - $close, 0), 20) + 1e-8)",
        "description": "20-Day Up-Volume / Down-Volume",
    },
    {
        "name": "vol_weighted_ret",
        "display_name": "Volume-Weighted Return",
        "category": "interaction",
        "expression": "Sum(($close / Ref($close, 1) - 1) * $volume, 20) / (Sum($volume, 20) + 1e-8)",
        "description": "20-Day Volume-Weighted Average Return",
    },
]

# OBV 類
OBV_FACTORS = [
    {
        "name": "obv_5",
        "display_name": "OBV 5d",
        "category": "interaction",
        "expression": "Sum($volume * Sign($close - Ref($close, 1)), 5)",
        "description": "5-Day OBV",
    },
    {
        "name": "obv_20",
        "display_name": "OBV 20d",
        "category": "interaction",
        "expression": "Sum($volume * Sign($close - Ref($close, 1)), 20)",
        "description": "20-Day OBV",
    },
    {
        "name": "obv_ratio",
        "display_name": "OBV Ratio",
        "category": "interaction",
        "expression": "Sum($volume * Sign($close - Ref($close, 1)), 5) / (Abs(Sum($volume * Sign($close - Ref($close, 1)), 20)) + 1e-8)",
        "description": "OBV Short/Long Ratio",
    },
]

# 成交金額
AMOUNT_FACTORS = [
    {
        "name": "amount_5",
        "display_name": "Dollar Volume 5d",
        "category": "interaction",
        "expression": "Mean($close * $volume, 5)",
        "description": "5-Day Average Dollar Volume",
    },
    {
        "name": "amount_ratio",
        "display_name": "Dollar Volume Ratio",
        "category": "interaction",
        "expression": "Mean($close * $volume, 5) / (Mean($close * $volume, 20) + 1e-8)",
        "description": "Dollar Volume Short/Long Ratio",
    },
]

# 高低量
HIGH_LOW_VOL_FACTORS = [
    {
        "name": "high_vol_corr",
        "display_name": "High-Volume Correlation",
        "category": "interaction",
        "expression": "Corr($high, $volume, 20)",
        "description": "High vs Volume 20-Day Correlation",
    },
    {
        "name": "low_vol_corr",
        "display_name": "Low-Volume Correlation",
        "category": "interaction",
        "expression": "Corr($low, $volume, 20)",
        "description": "Low vs Volume 20-Day Correlation",
    },
]

# 振幅量
RANGE_VOL_FACTORS = [
    {
        "name": "range_vol_ratio",
        "display_name": "Range-Volume Ratio",
        "category": "interaction",
        "expression": "(($high - $low) / $close) / ($volume / (Mean($volume, 20) + 1e-8) + 1e-8)",
        "description": "Range / Volume Ratio",
    },
    {
        "name": "range_vol_corr",
        "display_name": "Range-Volume Correlation",
        "category": "interaction",
        "expression": "Corr(($high - $low) / $close, $volume, 20)",
        "description": "Range vs Volume Correlation",
    },
]


# =============================================================================
# 籌碼價格交互因子
# =============================================================================

# 外資與價格
FOREIGN_PRICE_FACTORS = [
    {
        "name": "foreign_price_corr",
        "display_name": "Foreign-Price Correlation",
        "category": "interaction",
        "expression": "Corr($foreign_buy - $foreign_sell, $close, 20)",
        "description": "Foreign Net Buy vs Price 20-Day Correlation",
    },
    {
        "name": "foreign_ret_corr",
        "display_name": "Foreign-Return Correlation",
        "category": "interaction",
        "expression": "Corr($foreign_buy - $foreign_sell, $close / Ref($close, 1) - 1, 20)",
        "description": "Foreign Net Buy vs Return 20-Day Correlation",
    },
    {
        "name": "foreign_lead_ret",
        "display_name": "Foreign Lead vs Return",
        "category": "interaction",
        "expression": "Corr(Ref($foreign_buy - $foreign_sell, 1), $close / Ref($close, 1) - 1, 20)",
        "description": "Foreign Lead 1-Day vs Return Correlation",
    },
]

# 投信與價格
TRUST_PRICE_FACTORS = [
    {
        "name": "trust_price_corr",
        "display_name": "Investment Trust-Price Correlation",
        "category": "interaction",
        "expression": "Corr($trust_buy - $trust_sell, $close, 20)",
        "description": "Investment Trust Net Buy vs Price 20-Day Correlation",
    },
    {
        "name": "trust_ret_corr",
        "display_name": "Investment Trust-Return Correlation",
        "category": "interaction",
        "expression": "Corr($trust_buy - $trust_sell, $close / Ref($close, 1) - 1, 20)",
        "description": "Investment Trust Net Buy vs Return 20-Day Correlation",
    },
]

# 法人與量
INST_VOL_CORR_FACTORS = [
    {
        "name": "foreign_vol_corr",
        "display_name": "Foreign-Volume Correlation",
        "category": "interaction",
        "expression": "Corr($foreign_buy - $foreign_sell, $volume, 20)",
        "description": "Foreign Net Buy vs Volume 20-Day Correlation",
    },
    {
        "name": "trust_vol_corr",
        "display_name": "Investment Trust-Volume Correlation",
        "category": "interaction",
        "expression": "Corr($trust_buy - $trust_sell, $volume, 20)",
        "description": "Investment Trust Net Buy vs Volume 20-Day Correlation",
    },
]

# 融資與價格
MARGIN_PRICE_FACTORS = [
    {
        "name": "margin_price_corr",
        "display_name": "Margin-Price Correlation",
        "category": "interaction",
        "expression": "Corr($margin_balance, $close, 20)",
        "description": "Margin Balance vs Price 20-Day Correlation",
    },
    {
        "name": "margin_ret_corr",
        "display_name": "Margin-Return Correlation",
        "category": "interaction",
        "expression": "Corr($margin_balance - Ref($margin_balance, 1), $close / Ref($close, 1) - 1, 20)",
        "description": "Margin Change vs Return 20-Day Correlation",
    },
]

# 融券與價格
SHORT_PRICE_FACTORS = [
    {
        "name": "short_price_corr",
        "display_name": "Short-Price Correlation",
        "category": "interaction",
        "expression": "Corr($short_balance, $close, 20)",
        "description": "Short Balance vs Price 20-Day Correlation",
    },
    {
        "name": "short_ret_corr",
        "display_name": "Short-Return Correlation",
        "category": "interaction",
        "expression": "Corr($short_balance - Ref($short_balance, 1), $close / Ref($close, 1) - 1, 20)",
        "description": "Short Change vs Return 20-Day Correlation",
    },
]

# 外資持股與價格
FOREIGN_RATIO_PRICE_FACTORS = [
    {
        "name": "fh_ratio_price_corr",
        "display_name": "Holdings-Price Correlation",
        "category": "interaction",
        "expression": "Corr($foreign_ratio, $close, 60)",
        "description": "Foreign Holdings vs Price 60-Day Correlation",
    },
    {
        "name": "fh_ratio_ret_corr",
        "display_name": "Holdings-Return Correlation",
        "category": "interaction",
        "expression": "Corr($foreign_ratio - Ref($foreign_ratio, 1), $close / Ref($close, 1) - 1, 20)",
        "description": "Holdings Change vs Return 20-Day Correlation",
    },
]

# 法人與波動
INST_VOLATILITY_FACTORS = [
    {
        "name": "foreign_volatility_corr",
        "display_name": "Foreign-Volatility Correlation",
        "category": "interaction",
        "expression": "Corr(Abs($foreign_buy - $foreign_sell), Std($close / Ref($close, 1) - 1, 5), 20)",
        "description": "Foreign Strength vs Volatility Correlation",
    },
    {
        "name": "margin_volatility_corr",
        "display_name": "Margin-Volatility Correlation",
        "category": "interaction",
        "expression": "Corr(Abs($margin_balance - Ref($margin_balance, 1)), Std($close / Ref($close, 1) - 1, 5), 20)",
        "description": "Margin Change vs Volatility Correlation",
    },
]

# 法人順勢逆勢
INST_MOMENTUM_SYNC_FACTORS = [
    {
        "name": "foreign_momentum_sync",
        "display_name": "Foreign Trend-Following Degree",
        "category": "interaction",
        "expression": "Sum(Sign($foreign_buy - $foreign_sell) * Sign($close - Ref($close, 1)), 20) / 20",
        "description": "Foreign-Price Same-Direction Ratio",
    },
    {
        "name": "trust_momentum_sync",
        "display_name": "Investment Trust Trend-Following Degree",
        "category": "interaction",
        "expression": "Sum(Sign($trust_buy - $trust_sell) * Sign($close - Ref($close, 1)), 20) / 20",
        "description": "Investment Trust-Price Same-Direction Ratio",
    },
    {
        "name": "margin_contrarian_sync",
        "display_name": "Retail Contrarian Degree",
        "category": "interaction",
        "expression": "Sum(Sign($margin_balance - Ref($margin_balance, 1)) * Sign($close - Ref($close, 1)) * -1, 20) / 20",
        "description": "Margin-Price Opposite-Direction Ratio",
    },
]

# 籌碼集中度與收益
INST_CONCENTRATION_FACTORS = [
    {
        "name": "inst_concentration_ret",
        "display_name": "Institutional Concentration Return",
        "category": "interaction",
        "expression": "(($foreign_buy + $trust_buy + $dealer_buy) - ($foreign_sell + $trust_sell + $dealer_sell)) / ($volume + 1e-8) * ($close / Ref($close, 1) - 1)",
        "description": "product of institutional concentration and return",
    },
]


# =============================================================================
# 估值動能交互因子
# =============================================================================

# 估值與動能（注意：pe_momentum 已在基礎因子中，這裡使用不同命名）
VALUATION_MOMENTUM_FACTORS = [
    {
        "name": "pe_momentum_ext",
        "display_name": "PE Momentum Extension",
        "category": "interaction",
        "expression": "$pe_ratio / (Mean($pe_ratio, 60) + 1e-8) - 1",
        "description": "PE Deviation from 60-Day Mean",
    },
    {
        "name": "pb_momentum_ext",
        "display_name": "PB Momentum Extension",
        "category": "interaction",
        "expression": "$pb_ratio / (Mean($pb_ratio, 60) + 1e-8) - 1",
        "description": "PB Deviation from 60-Day Mean",
    },
    {
        "name": "yield_momentum",
        "display_name": "Dividend Yield Momentum",
        "category": "interaction",
        "expression": "$dividend_yield - Mean($dividend_yield, 60)",
        "description": "Dividend Yield Deviation from 60-Day Mean",
    },
]

# 估值與收益
VALUATION_RET_FACTORS = [
    {
        "name": "pe_ret_corr",
        "display_name": "PE-Return Correlation",
        "category": "interaction",
        "expression": "Corr($pe_ratio, $close / Ref($close, 1) - 1, 60)",
        "description": "PE vs Return 60-Day Correlation",
    },
    {
        "name": "pb_ret_corr",
        "display_name": "PB-Return Correlation",
        "category": "interaction",
        "expression": "Corr($pb_ratio, $close / Ref($close, 1) - 1, 60)",
        "description": "PB vs Return 60-Day Correlation",
    },
]

# 估值變化
VALUATION_CHG_FACTORS = [
    {
        "name": "pe_chg_5d",
        "display_name": "PE Change 5d",
        "category": "interaction",
        "expression": "$pe_ratio - Ref($pe_ratio, 5)",
        "description": "PE 5-Day Change",
    },
    {
        "name": "pe_chg_20d",
        "display_name": "PE Change 20d",
        "category": "interaction",
        "expression": "$pe_ratio - Ref($pe_ratio, 20)",
        "description": "PE 20-Day Change",
    },
    {
        "name": "pb_chg_5d",
        "display_name": "PB Change 5d",
        "category": "interaction",
        "expression": "$pb_ratio - Ref($pb_ratio, 5)",
        "description": "PB 5-Day Change",
    },
    {
        "name": "pb_chg_20d",
        "display_name": "PB Change 20d",
        "category": "interaction",
        "expression": "$pb_ratio - Ref($pb_ratio, 20)",
        "description": "PB 20-Day Change",
    },
]

# 估值排名
VALUATION_RANK_FACTORS = [
    {
        "name": "pe_rank_60d",
        "display_name": "PE Rank 60d",
        "category": "interaction",
        "expression": "Rank($pe_ratio, 60)",
        "description": "PE Rank within 60 Days",
    },
    {
        "name": "pb_rank_60d",
        "display_name": "PB Rank 60d",
        "category": "interaction",
        "expression": "Rank($pb_ratio, 60)",
        "description": "PB Rank within 60 Days",
    },
]

# 價值動能組合
VALUE_MOMENTUM_COMBO_FACTORS = [
    {
        "name": "value_momentum_combo",
        "display_name": "Value-Momentum Combination",
        "category": "interaction",
        "expression": "Rank(1 / ($pe_ratio + 1e-8), 60) * ($close / Ref($close, 20) - 1)",
        "description": "value rank times momentum",
    },
    {
        "name": "growth_value_score",
        "display_name": "Growth-Value Score",
        "category": "interaction",
        "expression": "Rank($revenue / (Ref($revenue, 252) + 1e-8) - 1, 60) + Rank(1 / ($pe_ratio + 1e-8), 60)",
        "description": "growth rank + value rank",
    },
]

# 估值與外資
VALUATION_FOREIGN_FACTORS = [
    {
        "name": "pe_foreign_sync",
        "display_name": "PE-Foreign Same-Direction",
        "category": "interaction",
        "expression": "Corr($pe_ratio, $foreign_ratio, 60)",
        "description": "PE vs Foreign Holdings 60-Day Correlation",
    },
]


# =============================================================================
# 匯出所有交互因子
# =============================================================================

INTERACTION_FACTORS = (
    # 價量交互（約 18 個）
    VOL_PRICE_CORR_FACTORS
    + RET_VOL_CORR_FACTORS
    + VOL_DISTRIBUTION_FACTORS
    + OBV_FACTORS
    + AMOUNT_FACTORS
    + HIGH_LOW_VOL_FACTORS
    + RANGE_VOL_FACTORS
    # 籌碼價格交互（約 22 個）
    + FOREIGN_PRICE_FACTORS
    + TRUST_PRICE_FACTORS
    + INST_VOL_CORR_FACTORS
    + MARGIN_PRICE_FACTORS
    + SHORT_PRICE_FACTORS
    + FOREIGN_RATIO_PRICE_FACTORS
    + INST_VOLATILITY_FACTORS
    + INST_MOMENTUM_SYNC_FACTORS
    + INST_CONCENTRATION_FACTORS
    # 估值動能交互（約 15 個）
    + VALUATION_MOMENTUM_FACTORS
    + VALUATION_RET_FACTORS
    + VALUATION_CHG_FACTORS
    + VALUATION_RANK_FACTORS
    + VALUE_MOMENTUM_COMBO_FACTORS
    + VALUATION_FOREIGN_FACTORS
)
