## Statistical IV


Our J-Divergence test is under the next null hypothesis

H<sub>0</sub>: The predictive power of the variable is not significant.

The null hypothesis is tested using a two-tailed distribution, and this should be taken into consideration when interpreting the p-value.

### Explanation

Optimize your machine learning models with 'Statistical-IV'. Perform automated feature selection based on statistics and customize error control.


0. **Import package**
   ```python
   from statistical_iv import api
   ```
   
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
   - Calculate Statistical IV information by calling the `statistical_iv` function from api with the specified parameters (That is used for OptimalBinning package).

   ```python
   result_df = api.statistical_iv(df, variables_names, var_y, type_vars, max_bins)

#### Example Result:

![Output Example](https://github.com/Nicerova7/statistical_iv/blob/main/images/output_example.png?raw=true)


### Full Paper:

For a comprehensive exploration of the topic, we recommend perusing the contents of the article available at [this link](https://arxiv.org/abs/2309.13183).