from transformers import pipeline

classifier = pipeline("zero-shot-classification")

res = classifier(
    "This is a business which does loans",
    candidate_labels=["finance", "tech", "industrial", "automotive"],
)

print(res)

print()

res = classifier(
    "This is a business which sells tires, wheels, and other parts",
    candidate_labels=["finance", "tech", "industrial", "automotive"],
)

print(res)
