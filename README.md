🌤️ SkyCast AI: AI-Powered Meteorological Forecasting System

APPLICATION LINK (Hugging Face / GitHub): 

https://huggingface.co/spaces/zeynepptkn/Precision-Rain-Forecaster   ----  https://github.com/ZeynepTekin-DS/Precision-Rain-Forecaster

PROJECT SUMMARY: 📖 This study was developed to analyze the effects of complex meteorological parameters on precipitation and to pre-detect rain probability. Rather than relying solely on raw data, the project transformed the physical consistency between atmospheric saturation and solar radiation into a mathematical model, constructing a meteorological decision-support mechanism.
METHODS USED:

Ensemble Learning: 🧠 Within the scope of the project, 8 different algorithms (Logistic Regression, XGBoost, LightGBM, CatBoost, etc.) were tested. Performance analysis showed that the Logistic Regression model exhibited the most balanced discriminatory power with a 0.8796 ROC-AUC score, while the RandomForestClassifier stood out in overall accuracy with 0.8652 Accuracy.

Class Sensitivity (Recall-Oriented): ⚖️ All models were optimized for capturing rain events (Recall). Specifically, the Logistic Regression and RandomForest models achieved a 0.9393 Recall score, successfully identifying nearly 94% of actual precipitation events.
DATA PREPROCESSING:

Feature Engineering: 🖇️ Features derived from raw data, such as humidity_cloud (humidity-cloud interaction) and dew_temp_diff (dew point-temperature difference), sharpened the signals in the dataset and maximized the model's predictive power.

Encoding & Scaling: 🧹 All categorical and numerical variables were normalized into a standard format, ensuring the algorithms could learn as quickly and stably as possible.

Feature Selection (Optimized Input): 🛠️ Analysis proved that parameters such as cloud cover, sunshine, humidity, and wind speed are the fundamental "critical triggers" determining the probability of rain.
KEY RESULTS:

Model Success: 🏆 The champion model results, with a 0.9131 F1-score and 0.8652 Accuracy, demonstrated that the outcomes are statistically significant rather than coincidental.

Critical Insights: 📊 It was determined that cases where cloud cover exceeds 80% and sunshine duration approaches zero are the highest risk factors for precipitation. The model verified the physical relationship between atmospheric saturation and solar radiation with a 0.8796 ROC-AUC success rate.
NOTES:

Interactive Interface: 🎨 Thanks to the dashboard prepared with Streamlit, users can input real-time meteorological data and receive visual alerts based on a 50% threshold value.

Production & Deployment: ☁️ The trained model (weather_model.joblib) has been deployed on Hugging Face Spaces, transforming data science into an operational meteorological tool.

    [!IMPORTANT]

    Model Storage Notice: Due to GitHub's file size limits, the trained model file could not be uploaded here. However, you can access the model file and the fully functional application via the Hugging Face link provided at the top of this page.

Prepared by: Zeynep Tekin

Date: April 6, 2026