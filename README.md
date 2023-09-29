### Statistical IV

Statistical_IV: J-Divergence Hypothesis Test for the Information Value (IV). Calculation of the Information Value with specific limits to the predictive power.

Using optimalBinning, We created a specific way to calculate a predicitive power for each particular variable.

1. **Provide a DataFrame as Input:**
   - Supply a DataFrame `df` containing your data for IV calculation.

2. **Specify Predictor Variables:**
   - Prived a list of predictor variable names (`variables_names`) to analyze.

3. **Define the Target Variable:**
   - Specify the name of the target variable (`var_y`) in your DataFrame.

4. **Indicate Variable Types:**
   - Define the type of your predictor variables as 'categorical' or 'numerical' using the `type_vars` parameter.

5. **Optional: Set Maximum Bins:**
   - Adjust the maximum number of bins for discretization (optional) using the `max_bins` parameter.

6. **Call the `statistical_iv` Function:**
   - Calculate IV by calling the `statistical_iv` function with the specified parameters (That is used for OptimalBinning package).

   ```python
   result_df = statistical_iv(df, variables_names, var_y, type_vars, max_bins)

#### Example Result:

![Output Example](images/output_example.png)