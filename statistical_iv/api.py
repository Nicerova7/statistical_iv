import numpy as np
from optbinning import OptimalBinning
from scipy.stats import norm
import pandas as pd
from typing import List
from .helpers.consts import BinningParameters, Configuration, OutPut



def statistical_iv(df: pd.DataFrame, variables_names: List, var_y: str, type_vars:str, max_bins:int = 10)-> pd.DataFrame:
    """
    Calculates the Information Value (IV) for a set of predictor variables in relation to a target variable.

    Args:
        df (pd.DataFrame): DataFrame containing the data.
        variables_names (List): List of predictor variable names.
        var_y (str): Name of the target variable.
        type_vars (str): Type of variables ('categorical' or 'numerical').
        max_bins (int, optional): Maximum number of bins for discretization (default: 10).

    Returns:
        pd.DataFrame: A DataFrame with the results of the Statistical IV calculation for each variable.
            - variable: Variable name.
            - Ĵ-Estimate: Estimated Statistical IV value.
            - Std-error: Standard error.
            - p-value: Associated p-value.
    """
        
    variables = []
    js = []
    rvs = []
    pvls = []

    for var in variables_names:

        x_ = df[var].values
        y_ = df[var_y].values
        optb = OptimalBinning(name=var, dtype=type_vars, max_n_bins=max_bins)
        optb.fit(x_, y_)
        resume_table = optb.binning_table.build()
        
        if resume_table[BinningParameters.bin_column].loc[0] == BinningParameters.one_bin_fail and len(resume_table) == BinningParameters.max_table_one_bin_fail:
            variables.append(var)
            js.append(0)
            rvs.append(0)
            pvls.append(None)
        
        else:
            p = (resume_table[BinningParameters.event_column] / resume_table[BinningParameters.event_column][BinningParameters.totals_column]).iloc[:-3].values.reshape(-1, 1)
            q = (resume_table[BinningParameters.nonevent_column] / resume_table[BinningParameters.nonevent_column][BinningParameters.totals_column]).iloc[:-3].values.reshape(-1, 1)
        
            ## STEP 1: J-normal
            J = np.zeros((1, 1))
            J[:, 0] = np.sum((p-q) * np.log(p / q), axis=0) # Definition 1 in article

            # STEP 2: Calculating Sigma, corollary 1
            V1 = np.zeros((1, 1))
            V2 = np.zeros((1, 1))

            p_ = p[:, 0]
            q_ = q[:, 0]
            diag = 1
                
            matriz_productos = np.outer(p_, p_)
            matriz_log = 1 + np.log(p_ / q_)
            cross_matriz_log = np.outer(matriz_log, matriz_log)
            cross_matriz_log = np.triu(cross_matriz_log, k=diag)
            matriz_productos = np.triu(matriz_productos, k=diag)
            matriz_productos_q = np.outer(q_, q_)
            matriz_productos_q = np.triu(matriz_productos_q, k=diag)
            matriz_final = matriz_productos * cross_matriz_log + matriz_productos_q
            V1[0, 0] = np.sum(matriz_final)
            V1[:, 0] = np.sum(p * (1 - p) * ((1 + np.log(p / q)) ** 2 + (q / p) ** 2), axis=0) - 2 * V1[:, 0] # Theorem 2, (11)

            matriz_productos = np.outer(q_, q_)
            matriz_log = 1 + np.log(q_ / p_)
            cross_matriz_log = np.outer(matriz_log, matriz_log)
            cross_matriz_log = np.triu(cross_matriz_log, k=diag)
            matriz_productos = np.triu(matriz_productos, k=diag)
            matriz_productos_p = np.outer(p_, p_)
            matriz_productos_p = np.triu(matriz_productos_p, k=diag)
            matriz_final = matriz_productos * cross_matriz_log + matriz_productos_p
            V2[0, 0] = np.sum(matriz_final)
            V2[:, 0] = np.sum(q * (1 - q) * ((1 + np.log(q / p)) ** 2 + (p / q) ** 2), axis=0) - 2 * V2[:, 0] # Theorem 2, (12)

            n = resume_table[BinningParameters.event_column][BinningParameters.totals_column]
            m = resume_table[BinningParameters.nonevent_column][BinningParameters.totals_column]

            Sigma = (m * V1 + n * V2) / (n + m)

            ## STEP 3 : Variance
            Var = ((n + m) / (n * m)) * Sigma

            ## STEP 4 : Quantile
            Raiz_Var = np.sqrt(Var)
            rvs.append(np.round(Raiz_Var[0][0], Configuration.max_decimals))
            #alpha = 0.05
            #Q = norm.ppf(1 - alpha, loc=0, scale=Raiz_Var)
        
            variables.append(var)
            js.append(np.round(J[0][0], Configuration.max_decimals))

            ## STEP 5:
            mean = 0
            pvls.append(2*norm.cdf(-J[0][0], loc=mean, scale=Raiz_Var)[0][0])


    out_df = pd.DataFrame()
    out_df[OutPut.variable_column] = variables
    out_df[OutPut.jhat_column] = js
    out_df[OutPut.stderror_column] = rvs
    out_df[OutPut.pvalue_column] = pvls
    return out_df