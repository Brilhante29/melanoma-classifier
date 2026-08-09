from melanoma_classifier.domain import Evaluation


def test_evaluation_serializes_confusion_matrix_counts() -> None:
    result = Evaluation(0.7, 0.8, 0.6, 0.62, 0.3, 100, 20, 10, 40)
    assert result.to_dict()["true_positive"] == 40
    assert result.to_dict()["auc"] == 0.7
