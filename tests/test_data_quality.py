import unittest
import tempfile
import os
from unittest.mock import patch, MagicMock

from src.metrics.data_quality import DatasetQualityMetric


class TestDatasetQualityMetric(unittest.TestCase):
    def setUp(self):
        self.metric = DatasetQualityMetric()

    def test_initialization(self):
        """Test metric initialization"""
        self.assertEqual(self.metric.dataset_quality, 0.0)
        self.assertEqual(self.metric.dataset_quality_latency, 0.0)

    def test_example_count_extraction(self):
        """Test example count extraction"""
        test_data = {
            "category": "DATASET",
            "cardData": {
                "dataset_info": {
                    "splits": [
                        {"name": "train", "num_examples": 1000},
                        {"name": "test", "num_examples": 200},
                    ]
                }
            },
        }

        result = self.metric.get_example_count(test_data)
        self.assertEqual(result, 1200)

    def test_metadata_completeness(self):
        """Test metadata completeness calculation"""
        test_data = {
            "cardData": {
                "task_categories": ["text-classification"],
                "language": ["en"],
                "size_categories": ["1K<n<10K"],
                "source_datasets": ["original"],
            }
        }

        result = self.metric.get_metadata_completeness(test_data)
        # Should have 4 out of 6 metadata fields
        self.assertAlmostEqual(result, 4 / 6, places=2)

    def test_non_dataset_returns_zero(self):
        """Test that non-dataset categories return 0"""
        test_data = {"category": "MODEL"}
        data = self.metric.get_data(test_data)
        self.assertIsNone(data)
