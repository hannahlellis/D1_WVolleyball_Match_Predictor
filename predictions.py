import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import seaborn as sns

# Config
data_path = os.path.join(os.path.dirname(__file__), 'combined_data.csv')
target = 'Pct._WLP'

# Hyperparameters (tweak these at the top of the file)
n_estimators = 100
random_state = 42
test_size = 0.2


data_df = pd.read_csv(data_path)

# Remove unwanted columns if present
data_df.drop(columns=['W', 'L'], errors='ignore', inplace=True)

# Features and target
X = data_df.drop(columns=[target], errors='ignore')
if 'Team' in X.columns:
    X = X.drop(columns=['Team'])
y = data_df[target].astype(float)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

# Model (bare-bones)
model = RandomForestRegressor(n_estimators=n_estimators, random_state=random_state)
model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, preds))
r2 = r2_score(y_test, preds)
print(f"Test RMSE: {rmse:.4f}")
print(f"Test R^2:  {r2:.4f}")

# Visualize results
feature_importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
top_n = min(20, len(feature_importances))

plt.figure(figsize=(8, max(4, top_n * 0.3)))
ax = sns.barplot(
    x=feature_importances.iloc[:top_n].values,
    y=feature_importances.iloc[:top_n].index,
    hue=feature_importances.iloc[:top_n].index,
    palette='viridis',
    dodge=False,
)
# remove legend to match previous appearance
if ax.get_legend() is not None:
    ax.legend_.remove()
plt.title('Top feature importances')
plt.xlabel('Importance')
plt.tight_layout()
plt.savefig('feature_importances.png')
print('Saved feature importances to feature_importances.png')
plt.show(block=False)
plt.pause(0.1)

plt.figure(figsize=(6,6))
sns.scatterplot(x=y_test, y=preds, alpha=0.6)
mn = min(y_test.min(), preds.min())
mx = max(y_test.max(), preds.max())
plt.plot([mn, mx], [mn, mx], color='red', linestyle='--')
plt.xlabel('Actual')
plt.ylabel('Predicted')
plt.title('Predicted vs Actual')
plt.tight_layout()
plt.savefig('pred_vs_actual.png')
print('Saved predicted vs actual plot to pred_vs_actual.png')
plt.show(block=False)
plt.pause(0.1)
