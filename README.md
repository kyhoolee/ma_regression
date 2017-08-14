54 11  
(54,)  
(54, 10)  
(LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False), '  ')  
Logarithm mean squared error: 43.97  
Variance score: 0.96  

(KernelRidge(alpha=1.0, coef0=1, degree=3, gamma=None, kernel='linear',
      kernel_params=None), '  ')  
Logarithm mean squared error: 44.31  
Variance score: 0.94  

(RandomForestRegressor(bootstrap=True, criterion='mse', max_depth=8,
           max_features='auto', max_leaf_nodes=None,
           min_impurity_split=1e-07, min_samples_leaf=1,
           min_samples_split=2, min_weight_fraction_leaf=0.0,
           n_estimators=10, n_jobs=1, oob_score=False, random_state=0,
           verbose=0, warm_start=False), '  ')  
Logarithm mean squared error: 44.50  
Variance score: 0.93  

(DecisionTreeRegressor(criterion='mse', max_depth=8, max_features=None,
           max_leaf_nodes=None, min_impurity_split=1e-07,
           min_samples_leaf=1, min_samples_split=2,
           min_weight_fraction_leaf=0.0, presort=False, random_state=None,
           splitter='best'), '  ')  
Logarithm mean squared error: 40.40  
Variance score: 1.00  

(AdaBoostRegressor(base_estimator=None, learning_rate=1.0, loss='linear',
         n_estimators=50, random_state=None), '  ')  
Logarithm mean squared error: 43.06  
Variance score: 0.98  
    
the variables are x1- revenue,   
x2-products (if this company has an existing drug on the market or not - Y.N)   
x3-R&D (If this company has their own R&D team or not)   
x4 - Leading position (If this company has a leading position on the market or not)   
x5-sales channels (if this company has its own selling channel - hospital, patient or not),   
x6 manufacturing base (if this company manufacture the drugs themselves or not)   
x7-patent (if this company has any patent or not)   
x8-licenses (if this company has any active license or not)   
x9-years of operation (years of the company enter into this industry)   
x10 is number of employees (number of employees the target company has while the acquisition happened)  
