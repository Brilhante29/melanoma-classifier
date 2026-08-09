# Architecture Decision

Decision: leakage-aware data pipeline.

The dominant risk is methodological, not infrastructure. Dataset verification, feature extraction, training, validation threshold selection, and untouched test evaluation are explicit stages. Hexagonal, MVC, microservices, brokers, and cloud add no useful boundary to this offline experiment.

SRP separates data, features, model policy, and evidence. OCP allows another estimator behind the same feature/evaluation arrays. LSP/ISP remain narrow because no broad framework interface is invented. DIP is expressed by benchmark orchestration depending on stage functions rather than CLI or Docker. KISS rejects a GPU model until it is compared under the same protocol.
