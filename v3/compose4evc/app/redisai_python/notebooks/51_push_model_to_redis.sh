cat ./tmp/IrisDatasetModel.pt | redis-cli -x AI.MODELSTORE mymodel TORCH CPU TAG iris images OUTPUTS 1 output BLOB