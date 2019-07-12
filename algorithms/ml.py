import numpy as np
from sklearn.metrics import brier_score_loss
y_true = np.array([0, 1, 1, 0])
y_true_categorical = np.array(["spam", "ham", "ham", "spam"])
y_prob = np.array([0.1, 0.9, 0.8, 0.3])
print(brier_score_loss(y_true, y_prob)  )

print(brier_score_loss(y_true, 1-y_prob, pos_label=0)  )

# brier_score_loss(y_true_categorical, y_prob,pos_label="ham")  

# brier_score_loss(y_true, np.array(y_prob) > 0.5)
