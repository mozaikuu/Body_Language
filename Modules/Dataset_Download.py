import kagglehub

def download_data():
  # Download latest version
  path = kagglehub.dataset_download("atulanandjha/lfwpeople")

  print("Path to dataset files:", path)

  # Download latest version
  path = kagglehub.dataset_download("ashwingupta3012/human-faces")

  print("Path to dataset files:", path)