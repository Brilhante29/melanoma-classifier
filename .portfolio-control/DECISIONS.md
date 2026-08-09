# Decision Register: #6 melanoma-classifier

| Decision | Selected option | Reason | Revisit trigger |
|---|---|---|---|
| Architecture | leakage-safe evaluation pipeline | split ownership and evaluation order dominate | multiple independently deployed consumers appear |
| Dataset | committed DermaMNIST v2.1 archive | official splits, published checksum and small offline footprint | license or dataset version changes |
| Model | class-balanced logistic regression | transparent CPU baseline isolates evaluation rigor | a deep model has a measured hypothesis |
| Threshold | validation-only selection | keeps the final test split untouched | clinical operating policy is externally specified |
| Interface | CLI in pinned Docker | one offline benchmark is the product | serving becomes a separate repository |
| Messaging/cloud | none | no delivery or provider behavior exists | dataset lifecycle becomes a measured system concern |

No metric is a clinical-safety claim. Dataset licensing and non-commercial constraints travel with every result.
