import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline

# Load generated data sheet
df = pd.read_csv('data.csv')

# Separate dependent & independent variables
X = df.drop(columns=['price'])
y = df['price']

# Track categorical and numerical columns explicitly
categorical_features = ['location', 'property_type', 'furnishing_status']
numerical_features = [col for col in X.columns if col not in categorical_features]

# Create preprocessor structure to avoid pipeline shape misalignments
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ],
    remainder='passthrough'
)

# Bundle preprocessor with an optimized high-depth tree regressor
model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=150, random_state=42, max_depth=20))
])

# Fit Pipeline Structure
print("⚡ Training your pipeline estimation engine...")
model_pipeline.fit(X, y)

# Save pipeline object completely
with open('house_model.pkl', 'wb') as file:
    pickle.dump(model_pipeline, file)

print("💾 Saved production-ready assembly system profile to: 'house_model.pkl'")