"""
Alpha158 price/volume factors

Based on the Qlib Alpha158 factor set; uses price and volume data only.
~95 factors total.
"""

# Time windows
WINDOWS = [5, 10, 20, 30, 60]

# =============================================================================
# KBAR 類因子（9 個）
# K 線形態因子，描述單日 K 棒特徵
# =============================================================================

KBAR_FACTORS = [
    {
        "name": "kbar_kmid",
        "display_name": "K-bar Mid",
        "category": "technical",
        "expression": "($close - $open) / $open",
        "description": "rate of change of close vs open",
    },
    {
        "name": "kbar_klen",
        "display_name": "K-bar Length",
        "category": "technical",
        "expression": "($high - $low) / $open",
        "description": "intraday range relative to open",
    },
    {
        "name": "kbar_kmid2",
        "display_name": "K-bar Mid 2",
        "category": "technical",
        "expression": "($close - $open) / ($high - $low + 1e-8)",
        "description": "close-open difference as share of range",
    },
    {
        "name": "kbar_kup",
        "display_name": "Upper Shadow",
        "category": "technical",
        "expression": "($high - Greater($open, $close)) / $open",
        "description": "Upper Shadow Length Ratio",
    },
    {
        "name": "kbar_kup2",
        "display_name": "Upper Shadow 2",
        "category": "technical",
        "expression": "($high - Greater($open, $close)) / ($high - $low + 1e-8)",
        "description": "Upper Shadow to Range Ratio",
    },
    {
        "name": "kbar_klow",
        "display_name": "Lower Shadow",
        "category": "technical",
        "expression": "(Less($open, $close) - $low) / $open",
        "description": "Lower Shadow Length Ratio",
    },
    {
        "name": "kbar_klow2",
        "display_name": "Lower Shadow 2",
        "category": "technical",
        "expression": "(Less($open, $close) - $low) / ($high - $low + 1e-8)",
        "description": "Lower Shadow to Range Ratio",
    },
    {
        "name": "kbar_ksft",
        "display_name": "K-bar Shift",
        "category": "technical",
        "expression": "(2 * $close - $high - $low) / $open",
        "description": "close deviation from mid ratio",
    },
    {
        "name": "kbar_ksft2",
        "display_name": "K-bar Shift 2",
        "category": "technical",
        "expression": "(2 * $close - $high - $low) / ($high - $low + 1e-8)",
        "description": "close deviation from mid as share of range",
    },
]


# =============================================================================
# ROC 類因子（5 個）
# 價格變化率
# =============================================================================

ROC_FACTORS = [
    {
        "name": f"roc_{w}",
        "display_name": f"ROC {w}d",
        "category": "technical",
        "expression": f"Ref($close, {w}) / $close - 1",
        "description": f"{w}-day price rate of change (past/current)",
    }
    for w in WINDOWS
]


# =============================================================================
# MA_RATIO 類因子（5 個）
# 均線比率
# =============================================================================

MA_RATIO_FACTORS = [
    {
        "name": f"ma_{w}",
        "display_name": f"MA Ratio {w}d",
        "category": "technical",
        "expression": f"Mean($close, {w}) / $close",
        "description": f"{w}-day MA / close",
    }
    for w in WINDOWS
]


# =============================================================================
# STD 類因子（5 個）
# 波動率
# =============================================================================

STD_FACTORS = [
    {
        "name": f"std_{w}",
        "display_name": f"Volatility {w}d",
        "category": "technical",
        "expression": f"Std($close, {w}) / $close",
        "description": f"{w}-day price std dev / close",
    }
    for w in WINDOWS
]


# =============================================================================
# BETA 類因子（5 個）
# 價格趨勢斜率
# =============================================================================

BETA_FACTORS = [
    {
        "name": f"beta_{w}",
        "display_name": f"Slope {w}d",
        "category": "technical",
        "expression": f"Slope($close, {w}) / $close",
        "description": f"{w}-day price regression slope / close",
    }
    for w in WINDOWS
]


# =============================================================================
# RSQR 類因子（5 個）
# 趨勢擬合度
# =============================================================================

RSQR_FACTORS = [
    {
        "name": f"rsqr_{w}",
        "display_name": f"R-squared {w}d",
        "category": "technical",
        "expression": f"Rsquare($close, {w})",
        "description": f"{w}-day trend fit (R2)",
    }
    for w in WINDOWS
]


# =============================================================================
# RESI 類因子（5 個）
# 殘差
# =============================================================================

RESI_FACTORS = [
    {
        "name": f"resi_{w}",
        "display_name": f"Residual {w}d",
        "category": "technical",
        "expression": f"Resi($close, {w}) / $close",
        "description": f"{w}-day regression residual / close",
    }
    for w in WINDOWS
]


# =============================================================================
# MAX 類因子（5 個）
# 最高價比
# =============================================================================

MAX_FACTORS = [
    {
        "name": f"max_{w}",
        "display_name": f"High Ratio {w}d",
        "category": "technical",
        "expression": f"Max($high, {w}) / $close",
        "description": f"{w}-day high / close",
    }
    for w in WINDOWS
]


# =============================================================================
# MIN 類因子（5 個）
# 最低價比
# =============================================================================

MIN_FACTORS = [
    {
        "name": f"min_{w}",
        "display_name": f"Low Ratio {w}d",
        "category": "technical",
        "expression": f"Min($low, {w}) / $close",
        "description": f"{w}-day low / close",
    }
    for w in WINDOWS
]


# =============================================================================
# QTLU 類因子（5 個）
# 80 分位數
# =============================================================================

QTLU_FACTORS = [
    {
        "name": f"qtlu_{w}",
        "display_name": f"80th Pct {w}d",
        "category": "technical",
        "expression": f"Quantile($close, {w}, 0.8) / $close",
        "description": f"{w}-day 80th percentile / close",
    }
    for w in WINDOWS
]


# =============================================================================
# QTLD 類因子（5 個）
# 20 分位數
# =============================================================================

QTLD_FACTORS = [
    {
        "name": f"qtld_{w}",
        "display_name": f"20th Pct {w}d",
        "category": "technical",
        "expression": f"Quantile($close, {w}, 0.2) / $close",
        "description": f"{w}-day 20th percentile / close",
    }
    for w in WINDOWS
]


# =============================================================================
# RANK 類因子（5 個）
# 時序排名
# =============================================================================

RANK_FACTORS = [
    {
        "name": f"tsrank_{w}",
        "display_name": f"Time-series Rank {w}d",
        "category": "technical",
        "expression": f"Rank($close, {w})",
        "description": f"close rank within {w} days",
    }
    for w in WINDOWS
]


# =============================================================================
# RSV 類因子（5 個）
# 相對強弱值
# =============================================================================

RSV_FACTORS = [
    {
        "name": f"rsv_{w}",
        "display_name": f"RSV {w}d",
        "category": "technical",
        "expression": f"($close - Min($low, {w})) / (Max($high, {w}) - Min($low, {w}) + 1e-8)",
        "description": f"{w}-day relative strength value",
    }
    for w in WINDOWS
]


# =============================================================================
# CNTP 類因子（5 個）
# 上漲天數佔比
# =============================================================================

CNTP_FACTORS = [
    {
        "name": f"cntp_{w}",
        "display_name": f"Up-Day Ratio {w}d",
        "category": "technical",
        "expression": f"Mean(Greater($close - Ref($close, 1), 0), {w})",
        "description": f"{w}-day up-day ratio",
    }
    for w in WINDOWS
]


# =============================================================================
# CNTN 類因子（5 個）
# 下跌天數佔比
# =============================================================================

CNTN_FACTORS = [
    {
        "name": f"cntn_{w}",
        "display_name": f"Down-Day Ratio {w}d",
        "category": "technical",
        "expression": f"Mean(Greater(Ref($close, 1) - $close, 0), {w})",
        "description": f"{w}-day down-day ratio",
    }
    for w in WINDOWS
]


# =============================================================================
# SUMP 類因子（5 個）
# 上漲幅度佔比
# =============================================================================

SUMP_FACTORS = [
    {
        "name": f"sump_{w}",
        "display_name": f"Up Magnitude {w}d",
        "category": "technical",
        "expression": f"Sum(Greater($close - Ref($close, 1), 0), {w}) / (Sum(Abs($close - Ref($close, 1)), {w}) + 1e-8)",
        "description": f"{w}-day up-move share",
    }
    for w in WINDOWS
]


# =============================================================================
# SUMN 類因子（5 個）
# 下跌幅度佔比
# =============================================================================

SUMN_FACTORS = [
    {
        "name": f"sumn_{w}",
        "display_name": f"Down Magnitude {w}d",
        "category": "technical",
        "expression": f"Sum(Greater(Ref($close, 1) - $close, 0), {w}) / (Sum(Abs($close - Ref($close, 1)), {w}) + 1e-8)",
        "description": f"{w}-day down-move share",
    }
    for w in WINDOWS
]


# =============================================================================
# SUMD 類因子（5 個）
# 漲跌差異
# =============================================================================

SUMD_FACTORS = [
    {
        "name": f"sumd_{w}",
        "display_name": f"Up-Down Diff {w}d",
        "category": "technical",
        "expression": (
            f"Sum(Greater($close - Ref($close, 1), 0), {w}) / (Sum(Abs($close - Ref($close, 1)), {w}) + 1e-8) "
            f"- Sum(Greater(Ref($close, 1) - $close, 0), {w}) / (Sum(Abs($close - Ref($close, 1)), {w}) + 1e-8)"
        ),
        "description": f"{w}-day up-down magnitude difference",
    }
    for w in WINDOWS
]


# =============================================================================
# VMA 類因子（5 個）
# 成交量均線比
# =============================================================================

VMA_FACTORS = [
    {
        "name": f"vma_{w}",
        "display_name": f"Volume MA Ratio {w}d",
        "category": "technical",
        "expression": f"Mean($volume, {w}) / ($volume + 1e-8)",
        "description": f"{w}-day volume MA / current volume",
    }
    for w in WINDOWS
]


# =============================================================================
# VSTD 類因子（5 個）
# 成交量波動率
# =============================================================================

VSTD_FACTORS = [
    {
        "name": f"vstd_{w}",
        "display_name": f"Volume Volatility {w}d",
        "category": "technical",
        "expression": f"Std($volume, {w}) / (Mean($volume, {w}) + 1e-8)",
        "description": f"{w}-day volume coefficient of variation",
    }
    for w in WINDOWS
]


# =============================================================================
# WVMA 類因子（5 個）
# 價量協方差
# =============================================================================

WVMA_FACTORS = [
    {
        "name": f"wvma_{w}",
        "display_name": f"Price-Volume Covariation {w}d",
        "category": "technical",
        "expression": f"Corr($close, Log($volume + 1), {w})",
        "description": f"{w}-day price-volume log correlation",
    }
    for w in WINDOWS
]


# =============================================================================
# 匯出所有 Alpha158 因子
# =============================================================================

ALPHA158_FACTORS = (
    KBAR_FACTORS
    + ROC_FACTORS
    + MA_RATIO_FACTORS
    + STD_FACTORS
    + BETA_FACTORS
    + RSQR_FACTORS
    + RESI_FACTORS
    + MAX_FACTORS
    + MIN_FACTORS
    + QTLU_FACTORS
    + QTLD_FACTORS
    + RANK_FACTORS
    + RSV_FACTORS
    + CNTP_FACTORS
    + CNTN_FACTORS
    + SUMP_FACTORS
    + SUMN_FACTORS
    + SUMD_FACTORS
    + VMA_FACTORS
    + VSTD_FACTORS
    + WVMA_FACTORS
)

# 因子數量統計
# KBAR: 9
# ROC: 5
# MA_RATIO: 5
# STD: 5
# BETA: 5
# RSQR: 5
# RESI: 5
# MAX: 5
# MIN: 5
# QTLU: 5
# QTLD: 5
# RANK: 5
# RSV: 5
# CNTP: 5
# CNTN: 5
# SUMP: 5
# SUMN: 5
# SUMD: 5
# VMA: 5
# VSTD: 5
# WVMA: 5
# 總計: 9 + 20 * 5 = 109 個
