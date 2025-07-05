# Credit Risk Probability Model

# Introduction
This week, we worked on behalf of Bati Bank to assess if customers qualify for a buy-now-pay-later service. We are developing a credit scoring model. We explored reasoning with business context, data exploration, predictive analysis, machine learning, hyperparameter tuning, and model comparison. 
Credit scoring assigns a numerical score to a borrower based on their past financial behavior and current financial situation, helping lenders make informed lending decisions. There are a lot of ways we could do this. For this specific dataset, by analyzing customers' Recency, Frequency, and Monetary (RFM) patterns, we engineer a proxy for credit risk. This behavioral signal serves as the foundation for training a model that produces a risk probability score—a vital metric for informing loan approvals and terms.

#Credit Scoring Business Understanding

	• Through its pillars, the Basel II Accord places a strong emphasis on risk measurement by aligning  a bank’s capital requirements more closely with the actual risks it faces. It allows banks to use internal models for calculating risks and it also requires that models used to measure risk be interpretable, validated, and well-documented.  This means our work must clearly explain how model works, we need to justify the inputs, assumptions, and outputs, and we need to prepare proper documentation.  
	• We need a proxy variable because training data should be labelled for our machine learning model to work correctly. The risks of using a proxy variable can be: the proxy not exactly reflecting actual default behavior, making our model learn the wrong thing, introducing bias into our model,  and not generalizing well.
	

|Factor|	Simple & Interpretable Model|	Complex & High-Performance Model|
|----------|----------|----------|
|Interpretability|	Highly interpretable, explains individual predictions clearly, Easy to justify to regulators and internal stakeholders|	Often a "black box", Requires post-hoc tools (e.g., SHAP, LIME), Less intuitive for non-technical users|
| Performance | May underperform on highly non-linear or high-dimensional data|	significantly higher predictive power, can capture complex, non-linear patterns|
|Regulatory Acceptance|	Trusted and widely used in regulatory models (Basel II, IFRS 9, etc.), Easier model governance, audit, and documentation	| Scrutinized more by regulators, Requires extra documentation, validation, and justification|
|Generalizability| Tends to generalize better in stable environments	Higher risk of overfitting|	May not generalize well across time or customer segments.|
		
# Methodology
To complete the project and find the necessary answers, we followed the following steps.  
**1.	Understanding Credit Risk**  
Using the given references, we tried to understand the concepts behind the process of credit scoring. We found answers to the given questions as well.

**2.	Exploratory Data Analysis (EDA)**  
The next step was exploring the data to find some valuable insights. This included:
1.	Overview of the Data and Summary Statistics: understand the structure of the dataset and shape of the dataset’s distribution.
2.	Visualizing the distribution of numerical features to identify patterns
 
3.	Analyzing the distribution of categorical features to see the frequency and variability of categories.
 
4.	Understanding the relationship (correlation) between numerical features.  
 
5. Identifying Missing Values and Outlier Detection using box plots to identify outliers.  
**3. Feature Engineering**  
Feature engineering is the process of transforming raw data into meaningful features that improve the performance of machine learning models. It’s about choosing, modifying, or creating variables that help your model learn patterns better. 
We performed the following tasks.
• Created new features from existing ones.
• Encoded categorical variables using label encoding.
• Handled missing data using imputers.
• Scaled the data
• Put the steps in a pipeline of sklearn.  
**4. Proxy Target Variable Engineering**  
Proxy Target Variable Engineering for credit risk is the process of creating a substitute target variable when the true label (e.g., actual loan default) is unavailable, delayed, or incomplete. Since our data does not have a target variable we created one for it. We calculated RFM for each customer. After that we used K-Means clustering algorithm to segment customers into 3 distinct groups based on their RFM profiles. We determined which group represents the least engaged and therefore highest-risk customer segment and created our target column based on that.
 
**5.	Model Training and Tracking**  
Finally we uploaded the cleaned data and tried two machine learning models to evaluate data. We used Logistic regression and Gradient boosting. We calculated various metrics to evaluate our model. We used grid search to find the best parameters. The gradient boosting has the best results based on accuracy.


# Challenges and Recommendations  

• One challenge that was faced during this week was inability to install the software needed for task 6. 
# Conclusion  
Our focus this week was on determining customer eligibility for a buy-now-pay-later service through the development of a credit scoring model. The project spanned multiple stages, including understanding the business context, exploring the data, conducting predictive analysis, building and tuning machine learning models, and comparing their performance to identify the most effective approach.

