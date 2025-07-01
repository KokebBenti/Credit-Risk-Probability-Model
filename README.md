# Credit Risk Probability Model
**Credit Scoring Business Understanding**

	• Through its pillars, the Basel II Accord places a strong emphasis on risk measurement by aligning  a bank’s capital requirements more closely with the actual risks it faces. It allows banks to use internal models for calculating risks and it also requires that models used to measure risk be interpretable, validated, and well-documented.  This means our work must clearly explain how model works, we need to justify the inputs, assumptions, and outputs, and we need to prepare proper documentation.  
	• We need a proxy variable because training data should be labelled for our machine learning model to work correctly. The risks of using a proxy variable can be: the proxy not exactly reflecting actual default behavior, making our model learn the wrong thing, introducing bias into our model,  and not generalizing well.
	

|Factor|	Simple & Interpretable Model|	Complex & High-Performance Model|
|----------|----------|----------|
|Interpretability|	Highly interpretable, explains individual predictions clearly, Easy to justify to regulators and internal stakeholders|	Often a "black box", Requires post-hoc tools (e.g., SHAP, LIME), Less intuitive for non-technical users|
| Performance | May underperform on highly non-linear or high-dimensional data|	significantly higher predictive power, can capture complex, non-linear patterns|
|Regulatory Acceptance|	Trusted and widely used in regulatory models (Basel II, IFRS 9, etc.), Easier model governance, audit, and documentation	| Scrutinized more by regulators, Requires extra documentation, validation, and justification|
|Generalizability| Tends to generalize better in stable environments	Higher risk of overfitting|	May not generalize well across time or customer segments.|
		
