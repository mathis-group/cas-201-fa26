import kagglehub
import os
# Download latest version
path = kagglehub.dataset_download("willianoliveiragibin/modeling-wine")

print("Path to dataset files:", path)
